# SNMP MIB module (ME1200-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-IP-MIB.mib
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

(ME1200InterfaceIndex,
 ME1200RowEditorState,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState",
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

me1200IpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102)
)
if mibBuilder.loadTexts:
    me1200IpMIB.setRevisions(
        ("2014-10-21 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-11-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200DhcpClientState(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("init", 1),
          ("selecting", 2),
          ("requesting", 3),
          ("rebinding", 4),
          ("bound", 5),
          ("renewing", 6),
          ("fallback", 7),
          ("arpCheck", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200IpMIBObjects_ObjectIdentity = ObjectIdentity
me1200IpMIBObjects = _Me1200IpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1)
)
_Me1200IpCapabilities_ObjectIdentity = ObjectIdentity
me1200IpCapabilities = _Me1200IpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1)
)
_Me1200IpCapabilitiesHasIpv4HostCapabilities_Type = TruthValue
_Me1200IpCapabilitiesHasIpv4HostCapabilities_Object = MibScalar
me1200IpCapabilitiesHasIpv4HostCapabilities = _Me1200IpCapabilitiesHasIpv4HostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 1),
    _Me1200IpCapabilitiesHasIpv4HostCapabilities_Type()
)
me1200IpCapabilitiesHasIpv4HostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesHasIpv4HostCapabilities.setStatus("current")
_Me1200IpCapabilitiesHasIpv6HostCapabilities_Type = TruthValue
_Me1200IpCapabilitiesHasIpv6HostCapabilities_Object = MibScalar
me1200IpCapabilitiesHasIpv6HostCapabilities = _Me1200IpCapabilitiesHasIpv6HostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 2),
    _Me1200IpCapabilitiesHasIpv6HostCapabilities_Type()
)
me1200IpCapabilitiesHasIpv6HostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesHasIpv6HostCapabilities.setStatus("current")
_Me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Type = TruthValue
_Me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Object = MibScalar
me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities = _Me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 3),
    _Me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Type()
)
me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities.setStatus("current")
_Me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Type = TruthValue
_Me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Object = MibScalar
me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities = _Me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 4),
    _Me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Type()
)
me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities.setStatus("current")
_Me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Type = TruthValue
_Me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Object = MibScalar
me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities = _Me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 5),
    _Me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Type()
)
me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities.setStatus("current")
_Me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Type = TruthValue
_Me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Object = MibScalar
me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities = _Me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 6),
    _Me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Type()
)
me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities.setStatus("current")
_Me1200IpCapabilitiesMaxNumberOfIpInterfaces_Type = Unsigned32
_Me1200IpCapabilitiesMaxNumberOfIpInterfaces_Object = MibScalar
me1200IpCapabilitiesMaxNumberOfIpInterfaces = _Me1200IpCapabilitiesMaxNumberOfIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 7),
    _Me1200IpCapabilitiesMaxNumberOfIpInterfaces_Type()
)
me1200IpCapabilitiesMaxNumberOfIpInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesMaxNumberOfIpInterfaces.setStatus("current")
_Me1200IpCapabilitiesMaxNumberOfStaticRoutes_Type = Unsigned32
_Me1200IpCapabilitiesMaxNumberOfStaticRoutes_Object = MibScalar
me1200IpCapabilitiesMaxNumberOfStaticRoutes = _Me1200IpCapabilitiesMaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 8),
    _Me1200IpCapabilitiesMaxNumberOfStaticRoutes_Type()
)
me1200IpCapabilitiesMaxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesMaxNumberOfStaticRoutes.setStatus("current")
_Me1200IpCapabilitiesNumberOfLpmHardwareEntries_Type = Unsigned32
_Me1200IpCapabilitiesNumberOfLpmHardwareEntries_Object = MibScalar
me1200IpCapabilitiesNumberOfLpmHardwareEntries = _Me1200IpCapabilitiesNumberOfLpmHardwareEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 1, 9),
    _Me1200IpCapabilitiesNumberOfLpmHardwareEntries_Type()
)
me1200IpCapabilitiesNumberOfLpmHardwareEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpCapabilitiesNumberOfLpmHardwareEntries.setStatus("current")
_Me1200IpConfig_ObjectIdentity = ObjectIdentity
me1200IpConfig = _Me1200IpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2)
)
_Me1200IpConfigGlobals_ObjectIdentity = ObjectIdentity
me1200IpConfigGlobals = _Me1200IpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1)
)
_Me1200IpConfigGlobalsMain_ObjectIdentity = ObjectIdentity
me1200IpConfigGlobalsMain = _Me1200IpConfigGlobalsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 1)
)
_Me1200IpConfigGlobalsMainEnableRouting_Type = TruthValue
_Me1200IpConfigGlobalsMainEnableRouting_Object = MibScalar
me1200IpConfigGlobalsMainEnableRouting = _Me1200IpConfigGlobalsMainEnableRouting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 1, 1),
    _Me1200IpConfigGlobalsMainEnableRouting_Type()
)
me1200IpConfigGlobalsMainEnableRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigGlobalsMainEnableRouting.setStatus("current")
_Me1200IpConfigInterfacesIpv6Table_Object = MibTable
me1200IpConfigInterfacesIpv6Table = _Me1200IpConfigInterfacesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6Table.setStatus("current")
_Me1200IpConfigInterfacesIpv6Entry_Object = MibTableRow
me1200IpConfigInterfacesIpv6Entry = _Me1200IpConfigInterfacesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 4, 1)
)
me1200IpConfigInterfacesIpv6Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6Entry.setStatus("current")
_Me1200IpConfigInterfacesIpv6IfIndex_Type = ME1200InterfaceIndex
_Me1200IpConfigInterfacesIpv6IfIndex_Object = MibTableColumn
me1200IpConfigInterfacesIpv6IfIndex = _Me1200IpConfigInterfacesIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 4, 1, 1),
    _Me1200IpConfigInterfacesIpv6IfIndex_Type()
)
me1200IpConfigInterfacesIpv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6IfIndex.setStatus("current")
_Me1200IpConfigInterfacesIpv6Active_Type = TruthValue
_Me1200IpConfigInterfacesIpv6Active_Object = MibTableColumn
me1200IpConfigInterfacesIpv6Active = _Me1200IpConfigInterfacesIpv6Active_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 4, 1, 2),
    _Me1200IpConfigInterfacesIpv6Active_Type()
)
me1200IpConfigInterfacesIpv6Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6Active.setStatus("current")
_Me1200IpConfigInterfacesIpv6Ipv6Address_Type = InetAddressIPv6
_Me1200IpConfigInterfacesIpv6Ipv6Address_Object = MibTableColumn
me1200IpConfigInterfacesIpv6Ipv6Address = _Me1200IpConfigInterfacesIpv6Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 4, 1, 3),
    _Me1200IpConfigInterfacesIpv6Ipv6Address_Type()
)
me1200IpConfigInterfacesIpv6Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6Ipv6Address.setStatus("current")
_Me1200IpConfigInterfacesIpv6PrefixSize_Type = Unsigned32
_Me1200IpConfigInterfacesIpv6PrefixSize_Object = MibTableColumn
me1200IpConfigInterfacesIpv6PrefixSize = _Me1200IpConfigInterfacesIpv6PrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 1, 4, 1, 4),
    _Me1200IpConfigInterfacesIpv6PrefixSize_Type()
)
me1200IpConfigInterfacesIpv6PrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6PrefixSize.setStatus("current")
_Me1200IpConfigInterfaces_ObjectIdentity = ObjectIdentity
me1200IpConfigInterfaces = _Me1200IpConfigInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2)
)
_Me1200IpConfigInterfacesTable_Object = MibTable
me1200IpConfigInterfacesTable = _Me1200IpConfigInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesTable.setStatus("current")
_Me1200IpConfigInterfacesEntry_Object = MibTableRow
me1200IpConfigInterfacesEntry = _Me1200IpConfigInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 1, 1)
)
me1200IpConfigInterfacesEntry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesEntry.setStatus("current")
_Me1200IpConfigInterfacesIfIndex_Type = ME1200InterfaceIndex
_Me1200IpConfigInterfacesIfIndex_Object = MibTableColumn
me1200IpConfigInterfacesIfIndex = _Me1200IpConfigInterfacesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 1, 1, 1),
    _Me1200IpConfigInterfacesIfIndex_Type()
)
me1200IpConfigInterfacesIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIfIndex.setStatus("current")
_Me1200IpConfigInterfacesAction_Type = ME1200RowEditorState
_Me1200IpConfigInterfacesAction_Object = MibTableColumn
me1200IpConfigInterfacesAction = _Me1200IpConfigInterfacesAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 1, 1, 100),
    _Me1200IpConfigInterfacesAction_Type()
)
me1200IpConfigInterfacesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesAction.setStatus("current")
_Me1200IpConfigInterfacesTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpConfigInterfacesTableRowEditor = _Me1200IpConfigInterfacesTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 2)
)
_Me1200IpConfigInterfacesTableRowEditorIfIndex_Type = ME1200InterfaceIndex
_Me1200IpConfigInterfacesTableRowEditorIfIndex_Object = MibScalar
me1200IpConfigInterfacesTableRowEditorIfIndex = _Me1200IpConfigInterfacesTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 2, 1),
    _Me1200IpConfigInterfacesTableRowEditorIfIndex_Type()
)
me1200IpConfigInterfacesTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesTableRowEditorIfIndex.setStatus("current")
_Me1200IpConfigInterfacesTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpConfigInterfacesTableRowEditorAction_Object = MibScalar
me1200IpConfigInterfacesTableRowEditorAction = _Me1200IpConfigInterfacesTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 2, 100),
    _Me1200IpConfigInterfacesTableRowEditorAction_Type()
)
me1200IpConfigInterfacesTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesTableRowEditorAction.setStatus("current")
_Me1200IpConfigInterfacesIpv4Table_Object = MibTable
me1200IpConfigInterfacesIpv4Table = _Me1200IpConfigInterfacesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4Table.setStatus("current")
_Me1200IpConfigInterfacesIpv4Entry_Object = MibTableRow
me1200IpConfigInterfacesIpv4Entry = _Me1200IpConfigInterfacesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1)
)
me1200IpConfigInterfacesIpv4Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4Entry.setStatus("current")
_Me1200IpConfigInterfacesIpv4IfIndex_Type = ME1200InterfaceIndex
_Me1200IpConfigInterfacesIpv4IfIndex_Object = MibTableColumn
me1200IpConfigInterfacesIpv4IfIndex = _Me1200IpConfigInterfacesIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1, 1),
    _Me1200IpConfigInterfacesIpv4IfIndex_Type()
)
me1200IpConfigInterfacesIpv4IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4IfIndex.setStatus("current")
_Me1200IpConfigInterfacesIpv4Active_Type = TruthValue
_Me1200IpConfigInterfacesIpv4Active_Object = MibTableColumn
me1200IpConfigInterfacesIpv4Active = _Me1200IpConfigInterfacesIpv4Active_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1, 2),
    _Me1200IpConfigInterfacesIpv4Active_Type()
)
me1200IpConfigInterfacesIpv4Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4Active.setStatus("current")
_Me1200IpConfigInterfacesIpv4EnableDhcpClient_Type = TruthValue
_Me1200IpConfigInterfacesIpv4EnableDhcpClient_Object = MibTableColumn
me1200IpConfigInterfacesIpv4EnableDhcpClient = _Me1200IpConfigInterfacesIpv4EnableDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1, 3),
    _Me1200IpConfigInterfacesIpv4EnableDhcpClient_Type()
)
me1200IpConfigInterfacesIpv4EnableDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4EnableDhcpClient.setStatus("current")
_Me1200IpConfigInterfacesIpv4Ipv4Address_Type = IpAddress
_Me1200IpConfigInterfacesIpv4Ipv4Address_Object = MibTableColumn
me1200IpConfigInterfacesIpv4Ipv4Address = _Me1200IpConfigInterfacesIpv4Ipv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1, 4),
    _Me1200IpConfigInterfacesIpv4Ipv4Address_Type()
)
me1200IpConfigInterfacesIpv4Ipv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4Ipv4Address.setStatus("current")
_Me1200IpConfigInterfacesIpv4PrefixSize_Type = Unsigned32
_Me1200IpConfigInterfacesIpv4PrefixSize_Object = MibTableColumn
me1200IpConfigInterfacesIpv4PrefixSize = _Me1200IpConfigInterfacesIpv4PrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1, 5),
    _Me1200IpConfigInterfacesIpv4PrefixSize_Type()
)
me1200IpConfigInterfacesIpv4PrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4PrefixSize.setStatus("current")
_Me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Type = Unsigned32
_Me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Object = MibTableColumn
me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout = _Me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 2, 3, 1, 6),
    _Me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Type()
)
me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout.setStatus("current")
_Me1200IpConfigRoutes_ObjectIdentity = ObjectIdentity
me1200IpConfigRoutes = _Me1200IpConfigRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3)
)
_Me1200IpConfigInterfacesRoutesIpv4Table_Object = MibTable
me1200IpConfigInterfacesRoutesIpv4Table = _Me1200IpConfigInterfacesRoutesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4Table.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4Entry_Object = MibTableRow
me1200IpConfigInterfacesRoutesIpv4Entry = _Me1200IpConfigInterfacesRoutesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 1, 1)
)
me1200IpConfigInterfacesRoutesIpv4Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4NetworkAddress"),
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize"),
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4NextHop"),
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4Entry.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4NetworkAddress_Type = IpAddress
_Me1200IpConfigInterfacesRoutesIpv4NetworkAddress_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv4NetworkAddress = _Me1200IpConfigInterfacesRoutesIpv4NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 1, 1, 1),
    _Me1200IpConfigInterfacesRoutesIpv4NetworkAddress_Type()
)
me1200IpConfigInterfacesRoutesIpv4NetworkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4NetworkAddress.setStatus("current")


class _Me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize_Type(Integer32):
    """Custom type me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize_Type.__name__ = "Integer32"
_Me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize = _Me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 1, 1, 2),
    _Me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize_Type()
)
me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4NextHop_Type = IpAddress
_Me1200IpConfigInterfacesRoutesIpv4NextHop_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv4NextHop = _Me1200IpConfigInterfacesRoutesIpv4NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 1, 1, 3),
    _Me1200IpConfigInterfacesRoutesIpv4NextHop_Type()
)
me1200IpConfigInterfacesRoutesIpv4NextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4NextHop.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4Action_Type = ME1200RowEditorState
_Me1200IpConfigInterfacesRoutesIpv4Action_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv4Action = _Me1200IpConfigInterfacesRoutesIpv4Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 1, 1, 100),
    _Me1200IpConfigInterfacesRoutesIpv4Action_Type()
)
me1200IpConfigInterfacesRoutesIpv4Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4Action.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4RowEditor_ObjectIdentity = ObjectIdentity
me1200IpConfigInterfacesRoutesIpv4RowEditor = _Me1200IpConfigInterfacesRoutesIpv4RowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 2)
)
_Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress_Type = IpAddress
_Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress = _Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 2, 1),
    _Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress_Type()
)
me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress.setStatus("current")


class _Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize_Type(Integer32):
    """Custom type me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize_Type.__name__ = "Integer32"
_Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize = _Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 2, 2),
    _Me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize_Type()
)
me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop_Type = IpAddress
_Me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop = _Me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 2, 3),
    _Me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop_Type()
)
me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv4RowEditorAction_Type = ME1200RowEditorState
_Me1200IpConfigInterfacesRoutesIpv4RowEditorAction_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv4RowEditorAction = _Me1200IpConfigInterfacesRoutesIpv4RowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 2, 100),
    _Me1200IpConfigInterfacesRoutesIpv4RowEditorAction_Type()
)
me1200IpConfigInterfacesRoutesIpv4RowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4RowEditorAction.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6Table_Object = MibTable
me1200IpConfigInterfacesRoutesIpv6Table = _Me1200IpConfigInterfacesRoutesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6Table.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6Entry_Object = MibTableRow
me1200IpConfigInterfacesRoutesIpv6Entry = _Me1200IpConfigInterfacesRoutesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3, 1)
)
me1200IpConfigInterfacesRoutesIpv6Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6NetworkAddress"),
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize"),
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6NextHop"),
    (0, "ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6NextHopInterface"),
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6Entry.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6NetworkAddress_Type = InetAddressIPv6
_Me1200IpConfigInterfacesRoutesIpv6NetworkAddress_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv6NetworkAddress = _Me1200IpConfigInterfacesRoutesIpv6NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3, 1, 1),
    _Me1200IpConfigInterfacesRoutesIpv6NetworkAddress_Type()
)
me1200IpConfigInterfacesRoutesIpv6NetworkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6NetworkAddress.setStatus("current")


class _Me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize_Type(Integer32):
    """Custom type me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize_Type.__name__ = "Integer32"
_Me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize = _Me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3, 1, 2),
    _Me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize_Type()
)
me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6NextHop_Type = InetAddressIPv6
_Me1200IpConfigInterfacesRoutesIpv6NextHop_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv6NextHop = _Me1200IpConfigInterfacesRoutesIpv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3, 1, 3),
    _Me1200IpConfigInterfacesRoutesIpv6NextHop_Type()
)
me1200IpConfigInterfacesRoutesIpv6NextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6NextHop.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6NextHopInterface_Type = ME1200InterfaceIndex
_Me1200IpConfigInterfacesRoutesIpv6NextHopInterface_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv6NextHopInterface = _Me1200IpConfigInterfacesRoutesIpv6NextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3, 1, 4),
    _Me1200IpConfigInterfacesRoutesIpv6NextHopInterface_Type()
)
me1200IpConfigInterfacesRoutesIpv6NextHopInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6NextHopInterface.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6Action_Type = ME1200RowEditorState
_Me1200IpConfigInterfacesRoutesIpv6Action_Object = MibTableColumn
me1200IpConfigInterfacesRoutesIpv6Action = _Me1200IpConfigInterfacesRoutesIpv6Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 3, 1, 100),
    _Me1200IpConfigInterfacesRoutesIpv6Action_Type()
)
me1200IpConfigInterfacesRoutesIpv6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6Action.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6RowEditor_ObjectIdentity = ObjectIdentity
me1200IpConfigInterfacesRoutesIpv6RowEditor = _Me1200IpConfigInterfacesRoutesIpv6RowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 4)
)
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress_Type = InetAddressIPv6
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress = _Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 4, 1),
    _Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress_Type()
)
me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress.setStatus("current")


class _Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize_Type(Integer32):
    """Custom type me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize_Type.__name__ = "Integer32"
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize = _Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 4, 2),
    _Me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize_Type()
)
me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop_Type = InetAddressIPv6
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop = _Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 4, 3),
    _Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop_Type()
)
me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface_Type = ME1200InterfaceIndex
_Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface = _Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 4, 4),
    _Me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface_Type()
)
me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface.setStatus("current")
_Me1200IpConfigInterfacesRoutesIpv6RowEditorAction_Type = ME1200RowEditorState
_Me1200IpConfigInterfacesRoutesIpv6RowEditorAction_Object = MibScalar
me1200IpConfigInterfacesRoutesIpv6RowEditorAction = _Me1200IpConfigInterfacesRoutesIpv6RowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 2, 3, 4, 100),
    _Me1200IpConfigInterfacesRoutesIpv6RowEditorAction_Type()
)
me1200IpConfigInterfacesRoutesIpv6RowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6RowEditorAction.setStatus("current")
_Me1200IpStatus_ObjectIdentity = ObjectIdentity
me1200IpStatus = _Me1200IpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3)
)
_Me1200IpStatusGlobals_ObjectIdentity = ObjectIdentity
me1200IpStatusGlobals = _Me1200IpStatusGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1)
)
_Me1200IpStatusGlobalsIpv4NeighbourTable_Object = MibTable
me1200IpStatusGlobalsIpv4NeighbourTable = _Me1200IpStatusGlobalsIpv4NeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv4NeighbourTable.setStatus("current")
_Me1200IpStatusGlobalsIpv4NeighbourEntry_Object = MibTableRow
me1200IpStatusGlobalsIpv4NeighbourEntry = _Me1200IpStatusGlobalsIpv4NeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 1, 1)
)
me1200IpStatusGlobalsIpv4NeighbourEntry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusGlobalsIpv4NeighbourIpv4"),
)
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv4NeighbourEntry.setStatus("current")
_Me1200IpStatusGlobalsIpv4NeighbourIpv4_Type = IpAddress
_Me1200IpStatusGlobalsIpv4NeighbourIpv4_Object = MibTableColumn
me1200IpStatusGlobalsIpv4NeighbourIpv4 = _Me1200IpStatusGlobalsIpv4NeighbourIpv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 1, 1, 1),
    _Me1200IpStatusGlobalsIpv4NeighbourIpv4_Type()
)
me1200IpStatusGlobalsIpv4NeighbourIpv4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv4NeighbourIpv4.setStatus("current")
_Me1200IpStatusGlobalsIpv4NeighbourMacAddress_Type = MacAddress
_Me1200IpStatusGlobalsIpv4NeighbourMacAddress_Object = MibTableColumn
me1200IpStatusGlobalsIpv4NeighbourMacAddress = _Me1200IpStatusGlobalsIpv4NeighbourMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 1, 1, 2),
    _Me1200IpStatusGlobalsIpv4NeighbourMacAddress_Type()
)
me1200IpStatusGlobalsIpv4NeighbourMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv4NeighbourMacAddress.setStatus("current")
_Me1200IpStatusGlobalsIpv4NeighbourInterface_Type = Unsigned32
_Me1200IpStatusGlobalsIpv4NeighbourInterface_Object = MibTableColumn
me1200IpStatusGlobalsIpv4NeighbourInterface = _Me1200IpStatusGlobalsIpv4NeighbourInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 1, 1, 3),
    _Me1200IpStatusGlobalsIpv4NeighbourInterface_Type()
)
me1200IpStatusGlobalsIpv4NeighbourInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv4NeighbourInterface.setStatus("current")
_Me1200IpStatusGlobalsIpv6NeighbourTable_Object = MibTable
me1200IpStatusGlobalsIpv6NeighbourTable = _Me1200IpStatusGlobalsIpv6NeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourTable.setStatus("current")
_Me1200IpStatusGlobalsIpv6NeighbourEntry_Object = MibTableRow
me1200IpStatusGlobalsIpv6NeighbourEntry = _Me1200IpStatusGlobalsIpv6NeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 2, 1)
)
me1200IpStatusGlobalsIpv6NeighbourEntry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusGlobalsIpv6NeighbourIpAddress"),
    (0, "ME1200-IP-MIB", "me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery"),
)
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourEntry.setStatus("current")
_Me1200IpStatusGlobalsIpv6NeighbourIpAddress_Type = InetAddressIPv6
_Me1200IpStatusGlobalsIpv6NeighbourIpAddress_Object = MibTableColumn
me1200IpStatusGlobalsIpv6NeighbourIpAddress = _Me1200IpStatusGlobalsIpv6NeighbourIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 2, 1, 1),
    _Me1200IpStatusGlobalsIpv6NeighbourIpAddress_Type()
)
me1200IpStatusGlobalsIpv6NeighbourIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourIpAddress.setStatus("current")


class _Me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery_Type(Integer32):
    """Custom type me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery_Type.__name__ = "Integer32"
_Me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery_Object = MibTableColumn
me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery = _Me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 2, 1, 2),
    _Me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery_Type()
)
me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery.setStatus("current")
_Me1200IpStatusGlobalsIpv6NeighbourMacAddress_Type = MacAddress
_Me1200IpStatusGlobalsIpv6NeighbourMacAddress_Object = MibTableColumn
me1200IpStatusGlobalsIpv6NeighbourMacAddress = _Me1200IpStatusGlobalsIpv6NeighbourMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 2, 1, 3),
    _Me1200IpStatusGlobalsIpv6NeighbourMacAddress_Type()
)
me1200IpStatusGlobalsIpv6NeighbourMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourMacAddress.setStatus("current")
_Me1200IpStatusGlobalsIpv6NeighbourInterface_Type = Unsigned32
_Me1200IpStatusGlobalsIpv6NeighbourInterface_Object = MibTableColumn
me1200IpStatusGlobalsIpv6NeighbourInterface = _Me1200IpStatusGlobalsIpv6NeighbourInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 1, 2, 1, 4),
    _Me1200IpStatusGlobalsIpv6NeighbourInterface_Type()
)
me1200IpStatusGlobalsIpv6NeighbourInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourInterface.setStatus("current")
_Me1200IpStatusInterfaces_ObjectIdentity = ObjectIdentity
me1200IpStatusInterfaces = _Me1200IpStatusInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2)
)
_Me1200IpStatusInterfaceLinkTable_Object = MibTable
me1200IpStatusInterfaceLinkTable = _Me1200IpStatusInterfaceLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkTable.setStatus("current")
_Me1200IpStatusInterfaceLinkEntry_Object = MibTableRow
me1200IpStatusInterfaceLinkEntry = _Me1200IpStatusInterfaceLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1)
)
me1200IpStatusInterfaceLinkEntry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusInterfaceLinkIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkEntry.setStatus("current")
_Me1200IpStatusInterfaceLinkIfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatusInterfaceLinkIfIndex_Object = MibTableColumn
me1200IpStatusInterfaceLinkIfIndex = _Me1200IpStatusInterfaceLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 1),
    _Me1200IpStatusInterfaceLinkIfIndex_Type()
)
me1200IpStatusInterfaceLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkIfIndex.setStatus("current")
_Me1200IpStatusInterfaceLinkOsInterfaceIndex_Type = Unsigned32
_Me1200IpStatusInterfaceLinkOsInterfaceIndex_Object = MibTableColumn
me1200IpStatusInterfaceLinkOsInterfaceIndex = _Me1200IpStatusInterfaceLinkOsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 2),
    _Me1200IpStatusInterfaceLinkOsInterfaceIndex_Type()
)
me1200IpStatusInterfaceLinkOsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkOsInterfaceIndex.setStatus("current")
_Me1200IpStatusInterfaceLinkMtu_Type = Unsigned32
_Me1200IpStatusInterfaceLinkMtu_Object = MibTableColumn
me1200IpStatusInterfaceLinkMtu = _Me1200IpStatusInterfaceLinkMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 3),
    _Me1200IpStatusInterfaceLinkMtu_Type()
)
me1200IpStatusInterfaceLinkMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkMtu.setStatus("current")
_Me1200IpStatusInterfaceLinkMacAddress_Type = MacAddress
_Me1200IpStatusInterfaceLinkMacAddress_Object = MibTableColumn
me1200IpStatusInterfaceLinkMacAddress = _Me1200IpStatusInterfaceLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 4),
    _Me1200IpStatusInterfaceLinkMacAddress_Type()
)
me1200IpStatusInterfaceLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkMacAddress.setStatus("current")
_Me1200IpStatusInterfaceLinkUp_Type = TruthValue
_Me1200IpStatusInterfaceLinkUp_Object = MibTableColumn
me1200IpStatusInterfaceLinkUp = _Me1200IpStatusInterfaceLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 5),
    _Me1200IpStatusInterfaceLinkUp_Type()
)
me1200IpStatusInterfaceLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkUp.setStatus("current")
_Me1200IpStatusInterfaceLinkBroadcast_Type = TruthValue
_Me1200IpStatusInterfaceLinkBroadcast_Object = MibTableColumn
me1200IpStatusInterfaceLinkBroadcast = _Me1200IpStatusInterfaceLinkBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 6),
    _Me1200IpStatusInterfaceLinkBroadcast_Type()
)
me1200IpStatusInterfaceLinkBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkBroadcast.setStatus("current")
_Me1200IpStatusInterfaceLinkLoopback_Type = TruthValue
_Me1200IpStatusInterfaceLinkLoopback_Object = MibTableColumn
me1200IpStatusInterfaceLinkLoopback = _Me1200IpStatusInterfaceLinkLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 7),
    _Me1200IpStatusInterfaceLinkLoopback_Type()
)
me1200IpStatusInterfaceLinkLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkLoopback.setStatus("current")
_Me1200IpStatusInterfaceLinkRunning_Type = TruthValue
_Me1200IpStatusInterfaceLinkRunning_Object = MibTableColumn
me1200IpStatusInterfaceLinkRunning = _Me1200IpStatusInterfaceLinkRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 8),
    _Me1200IpStatusInterfaceLinkRunning_Type()
)
me1200IpStatusInterfaceLinkRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkRunning.setStatus("current")
_Me1200IpStatusInterfaceLinkNoarp_Type = TruthValue
_Me1200IpStatusInterfaceLinkNoarp_Object = MibTableColumn
me1200IpStatusInterfaceLinkNoarp = _Me1200IpStatusInterfaceLinkNoarp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 9),
    _Me1200IpStatusInterfaceLinkNoarp_Type()
)
me1200IpStatusInterfaceLinkNoarp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkNoarp.setStatus("current")
_Me1200IpStatusInterfaceLinkPromisc_Type = TruthValue
_Me1200IpStatusInterfaceLinkPromisc_Object = MibTableColumn
me1200IpStatusInterfaceLinkPromisc = _Me1200IpStatusInterfaceLinkPromisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 10),
    _Me1200IpStatusInterfaceLinkPromisc_Type()
)
me1200IpStatusInterfaceLinkPromisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkPromisc.setStatus("current")
_Me1200IpStatusInterfaceLinkMulticast_Type = TruthValue
_Me1200IpStatusInterfaceLinkMulticast_Object = MibTableColumn
me1200IpStatusInterfaceLinkMulticast = _Me1200IpStatusInterfaceLinkMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 1, 1, 11),
    _Me1200IpStatusInterfaceLinkMulticast_Type()
)
me1200IpStatusInterfaceLinkMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkMulticast.setStatus("current")
_Me1200IpStatusInterfaceIpv4Table_Object = MibTable
me1200IpStatusInterfaceIpv4Table = _Me1200IpStatusInterfaceIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4Table.setStatus("current")
_Me1200IpStatusInterfaceIpv4Entry_Object = MibTableRow
me1200IpStatusInterfaceIpv4Entry = _Me1200IpStatusInterfaceIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1)
)
me1200IpStatusInterfaceIpv4Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4Entry.setStatus("current")
_Me1200IpStatusInterfaceIpv4IfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatusInterfaceIpv4IfIndex_Object = MibTableColumn
me1200IpStatusInterfaceIpv4IfIndex = _Me1200IpStatusInterfaceIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1, 1),
    _Me1200IpStatusInterfaceIpv4IfIndex_Type()
)
me1200IpStatusInterfaceIpv4IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4IfIndex.setStatus("current")
_Me1200IpStatusInterfaceIpv4Address_Type = IpAddress
_Me1200IpStatusInterfaceIpv4Address_Object = MibTableColumn
me1200IpStatusInterfaceIpv4Address = _Me1200IpStatusInterfaceIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1, 2),
    _Me1200IpStatusInterfaceIpv4Address_Type()
)
me1200IpStatusInterfaceIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4Address.setStatus("current")
_Me1200IpStatusInterfaceIpv4Prefix_Type = Unsigned32
_Me1200IpStatusInterfaceIpv4Prefix_Object = MibTableColumn
me1200IpStatusInterfaceIpv4Prefix = _Me1200IpStatusInterfaceIpv4Prefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1, 3),
    _Me1200IpStatusInterfaceIpv4Prefix_Type()
)
me1200IpStatusInterfaceIpv4Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4Prefix.setStatus("current")
_Me1200IpStatusInterfaceIpv4Broadcast_Type = Unsigned32
_Me1200IpStatusInterfaceIpv4Broadcast_Object = MibTableColumn
me1200IpStatusInterfaceIpv4Broadcast = _Me1200IpStatusInterfaceIpv4Broadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1, 4),
    _Me1200IpStatusInterfaceIpv4Broadcast_Type()
)
me1200IpStatusInterfaceIpv4Broadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4Broadcast.setStatus("current")
_Me1200IpStatusInterfaceIpv4ReasmMaxSize_Type = Unsigned32
_Me1200IpStatusInterfaceIpv4ReasmMaxSize_Object = MibTableColumn
me1200IpStatusInterfaceIpv4ReasmMaxSize = _Me1200IpStatusInterfaceIpv4ReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1, 5),
    _Me1200IpStatusInterfaceIpv4ReasmMaxSize_Type()
)
me1200IpStatusInterfaceIpv4ReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4ReasmMaxSize.setStatus("current")
_Me1200IpStatusInterfaceIpv4ArpRetransmitTime_Type = Unsigned32
_Me1200IpStatusInterfaceIpv4ArpRetransmitTime_Object = MibTableColumn
me1200IpStatusInterfaceIpv4ArpRetransmitTime = _Me1200IpStatusInterfaceIpv4ArpRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 2, 1, 6),
    _Me1200IpStatusInterfaceIpv4ArpRetransmitTime_Type()
)
me1200IpStatusInterfaceIpv4ArpRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4ArpRetransmitTime.setStatus("current")
_Me1200IpStatusInterfaceDhcpClientV4Table_Object = MibTable
me1200IpStatusInterfaceDhcpClientV4Table = _Me1200IpStatusInterfaceDhcpClientV4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceDhcpClientV4Table.setStatus("current")
_Me1200IpStatusInterfaceDhcpClientV4Entry_Object = MibTableRow
me1200IpStatusInterfaceDhcpClientV4Entry = _Me1200IpStatusInterfaceDhcpClientV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 3, 1)
)
me1200IpStatusInterfaceDhcpClientV4Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusInterfaceDhcpClientV4IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceDhcpClientV4Entry.setStatus("current")
_Me1200IpStatusInterfaceDhcpClientV4IfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatusInterfaceDhcpClientV4IfIndex_Object = MibTableColumn
me1200IpStatusInterfaceDhcpClientV4IfIndex = _Me1200IpStatusInterfaceDhcpClientV4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 3, 1, 1),
    _Me1200IpStatusInterfaceDhcpClientV4IfIndex_Type()
)
me1200IpStatusInterfaceDhcpClientV4IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceDhcpClientV4IfIndex.setStatus("current")
_Me1200IpStatusInterfaceDhcpClientV4State_Type = ME1200DhcpClientState
_Me1200IpStatusInterfaceDhcpClientV4State_Object = MibTableColumn
me1200IpStatusInterfaceDhcpClientV4State = _Me1200IpStatusInterfaceDhcpClientV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 3, 1, 2),
    _Me1200IpStatusInterfaceDhcpClientV4State_Type()
)
me1200IpStatusInterfaceDhcpClientV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceDhcpClientV4State.setStatus("current")
_Me1200IpStatusInterfaceDhcpClientV4ServerIp_Type = Unsigned32
_Me1200IpStatusInterfaceDhcpClientV4ServerIp_Object = MibTableColumn
me1200IpStatusInterfaceDhcpClientV4ServerIp = _Me1200IpStatusInterfaceDhcpClientV4ServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 3, 1, 3),
    _Me1200IpStatusInterfaceDhcpClientV4ServerIp_Type()
)
me1200IpStatusInterfaceDhcpClientV4ServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceDhcpClientV4ServerIp.setStatus("current")
_Me1200IpStatusInterfaceIpv6Table_Object = MibTable
me1200IpStatusInterfaceIpv6Table = _Me1200IpStatusInterfaceIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Table.setStatus("current")
_Me1200IpStatusInterfaceIpv6Entry_Object = MibTableRow
me1200IpStatusInterfaceIpv6Entry = _Me1200IpStatusInterfaceIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1)
)
me1200IpStatusInterfaceIpv6Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Entry.setStatus("current")
_Me1200IpStatusInterfaceIpv6IfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatusInterfaceIpv6IfIndex_Object = MibTableColumn
me1200IpStatusInterfaceIpv6IfIndex = _Me1200IpStatusInterfaceIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 1),
    _Me1200IpStatusInterfaceIpv6IfIndex_Type()
)
me1200IpStatusInterfaceIpv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6IfIndex.setStatus("current")
_Me1200IpStatusInterfaceIpv6Address_Type = InetAddressIPv6
_Me1200IpStatusInterfaceIpv6Address_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Address = _Me1200IpStatusInterfaceIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 2),
    _Me1200IpStatusInterfaceIpv6Address_Type()
)
me1200IpStatusInterfaceIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Address.setStatus("current")
_Me1200IpStatusInterfaceIpv6Prefix_Type = Unsigned32
_Me1200IpStatusInterfaceIpv6Prefix_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Prefix = _Me1200IpStatusInterfaceIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 3),
    _Me1200IpStatusInterfaceIpv6Prefix_Type()
)
me1200IpStatusInterfaceIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Prefix.setStatus("current")
_Me1200IpStatusInterfaceIpv6Tentative_Type = TruthValue
_Me1200IpStatusInterfaceIpv6Tentative_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Tentative = _Me1200IpStatusInterfaceIpv6Tentative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 4),
    _Me1200IpStatusInterfaceIpv6Tentative_Type()
)
me1200IpStatusInterfaceIpv6Tentative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Tentative.setStatus("current")
_Me1200IpStatusInterfaceIpv6Duplicated_Type = TruthValue
_Me1200IpStatusInterfaceIpv6Duplicated_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Duplicated = _Me1200IpStatusInterfaceIpv6Duplicated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 5),
    _Me1200IpStatusInterfaceIpv6Duplicated_Type()
)
me1200IpStatusInterfaceIpv6Duplicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Duplicated.setStatus("current")
_Me1200IpStatusInterfaceIpv6Detached_Type = TruthValue
_Me1200IpStatusInterfaceIpv6Detached_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Detached = _Me1200IpStatusInterfaceIpv6Detached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 6),
    _Me1200IpStatusInterfaceIpv6Detached_Type()
)
me1200IpStatusInterfaceIpv6Detached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Detached.setStatus("current")
_Me1200IpStatusInterfaceIpv6Nodad_Type = TruthValue
_Me1200IpStatusInterfaceIpv6Nodad_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Nodad = _Me1200IpStatusInterfaceIpv6Nodad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 7),
    _Me1200IpStatusInterfaceIpv6Nodad_Type()
)
me1200IpStatusInterfaceIpv6Nodad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Nodad.setStatus("current")
_Me1200IpStatusInterfaceIpv6Autoconf_Type = TruthValue
_Me1200IpStatusInterfaceIpv6Autoconf_Object = MibTableColumn
me1200IpStatusInterfaceIpv6Autoconf = _Me1200IpStatusInterfaceIpv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 2, 4, 1, 8),
    _Me1200IpStatusInterfaceIpv6Autoconf_Type()
)
me1200IpStatusInterfaceIpv6Autoconf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6Autoconf.setStatus("current")
_Me1200IpStatusRoutes_ObjectIdentity = ObjectIdentity
me1200IpStatusRoutes = _Me1200IpStatusRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3)
)
_Me1200IpStatusRoutesIpv4Table_Object = MibTable
me1200IpStatusRoutesIpv4Table = _Me1200IpStatusRoutesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4Table.setStatus("current")
_Me1200IpStatusRoutesIpv4Entry_Object = MibTableRow
me1200IpStatusRoutesIpv4Entry = _Me1200IpStatusRoutesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1)
)
me1200IpStatusRoutesIpv4Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv4NetworkAddress"),
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv4NetworkPrefixSize"),
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv4NextHop"),
)
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4Entry.setStatus("current")
_Me1200IpStatusRoutesIpv4NetworkAddress_Type = IpAddress
_Me1200IpStatusRoutesIpv4NetworkAddress_Object = MibTableColumn
me1200IpStatusRoutesIpv4NetworkAddress = _Me1200IpStatusRoutesIpv4NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 1),
    _Me1200IpStatusRoutesIpv4NetworkAddress_Type()
)
me1200IpStatusRoutesIpv4NetworkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4NetworkAddress.setStatus("current")


class _Me1200IpStatusRoutesIpv4NetworkPrefixSize_Type(Integer32):
    """Custom type me1200IpStatusRoutesIpv4NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpStatusRoutesIpv4NetworkPrefixSize_Type.__name__ = "Integer32"
_Me1200IpStatusRoutesIpv4NetworkPrefixSize_Object = MibTableColumn
me1200IpStatusRoutesIpv4NetworkPrefixSize = _Me1200IpStatusRoutesIpv4NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 2),
    _Me1200IpStatusRoutesIpv4NetworkPrefixSize_Type()
)
me1200IpStatusRoutesIpv4NetworkPrefixSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4NetworkPrefixSize.setStatus("current")
_Me1200IpStatusRoutesIpv4NextHop_Type = IpAddress
_Me1200IpStatusRoutesIpv4NextHop_Object = MibTableColumn
me1200IpStatusRoutesIpv4NextHop = _Me1200IpStatusRoutesIpv4NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 3),
    _Me1200IpStatusRoutesIpv4NextHop_Type()
)
me1200IpStatusRoutesIpv4NextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4NextHop.setStatus("current")
_Me1200IpStatusRoutesIpv4DerivedNextHopInterface_Type = ME1200InterfaceIndex
_Me1200IpStatusRoutesIpv4DerivedNextHopInterface_Object = MibTableColumn
me1200IpStatusRoutesIpv4DerivedNextHopInterface = _Me1200IpStatusRoutesIpv4DerivedNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 4),
    _Me1200IpStatusRoutesIpv4DerivedNextHopInterface_Type()
)
me1200IpStatusRoutesIpv4DerivedNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4DerivedNextHopInterface.setStatus("current")
_Me1200IpStatusRoutesIpv4FlagUp_Type = TruthValue
_Me1200IpStatusRoutesIpv4FlagUp_Object = MibTableColumn
me1200IpStatusRoutesIpv4FlagUp = _Me1200IpStatusRoutesIpv4FlagUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 35),
    _Me1200IpStatusRoutesIpv4FlagUp_Type()
)
me1200IpStatusRoutesIpv4FlagUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4FlagUp.setStatus("current")
_Me1200IpStatusRoutesIpv4FlagHost_Type = TruthValue
_Me1200IpStatusRoutesIpv4FlagHost_Object = MibTableColumn
me1200IpStatusRoutesIpv4FlagHost = _Me1200IpStatusRoutesIpv4FlagHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 36),
    _Me1200IpStatusRoutesIpv4FlagHost_Type()
)
me1200IpStatusRoutesIpv4FlagHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4FlagHost.setStatus("current")
_Me1200IpStatusRoutesIpv4FlagGateway_Type = TruthValue
_Me1200IpStatusRoutesIpv4FlagGateway_Object = MibTableColumn
me1200IpStatusRoutesIpv4FlagGateway = _Me1200IpStatusRoutesIpv4FlagGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 37),
    _Me1200IpStatusRoutesIpv4FlagGateway_Type()
)
me1200IpStatusRoutesIpv4FlagGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4FlagGateway.setStatus("current")
_Me1200IpStatusRoutesIpv4OwnerConf_Type = TruthValue
_Me1200IpStatusRoutesIpv4OwnerConf_Object = MibTableColumn
me1200IpStatusRoutesIpv4OwnerConf = _Me1200IpStatusRoutesIpv4OwnerConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 67),
    _Me1200IpStatusRoutesIpv4OwnerConf_Type()
)
me1200IpStatusRoutesIpv4OwnerConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4OwnerConf.setStatus("current")
_Me1200IpStatusRoutesIpv4OwnerDhcp_Type = TruthValue
_Me1200IpStatusRoutesIpv4OwnerDhcp_Object = MibTableColumn
me1200IpStatusRoutesIpv4OwnerDhcp = _Me1200IpStatusRoutesIpv4OwnerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 68),
    _Me1200IpStatusRoutesIpv4OwnerDhcp_Type()
)
me1200IpStatusRoutesIpv4OwnerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4OwnerDhcp.setStatus("current")
_Me1200IpStatusRoutesIpv4OwnerDynamic_Type = TruthValue
_Me1200IpStatusRoutesIpv4OwnerDynamic_Object = MibTableColumn
me1200IpStatusRoutesIpv4OwnerDynamic = _Me1200IpStatusRoutesIpv4OwnerDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 1, 1, 69),
    _Me1200IpStatusRoutesIpv4OwnerDynamic_Type()
)
me1200IpStatusRoutesIpv4OwnerDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4OwnerDynamic.setStatus("current")
_Me1200IpStatusRoutesIpv6Table_Object = MibTable
me1200IpStatusRoutesIpv6Table = _Me1200IpStatusRoutesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6Table.setStatus("current")
_Me1200IpStatusRoutesIpv6Entry_Object = MibTableRow
me1200IpStatusRoutesIpv6Entry = _Me1200IpStatusRoutesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1)
)
me1200IpStatusRoutesIpv6Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv6NetworkAddress"),
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv6NetworkPrefixSize"),
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv6NextHop"),
    (0, "ME1200-IP-MIB", "me1200IpStatusRoutesIpv6NextHopInterface"),
)
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6Entry.setStatus("current")
_Me1200IpStatusRoutesIpv6NetworkAddress_Type = InetAddressIPv6
_Me1200IpStatusRoutesIpv6NetworkAddress_Object = MibTableColumn
me1200IpStatusRoutesIpv6NetworkAddress = _Me1200IpStatusRoutesIpv6NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 1),
    _Me1200IpStatusRoutesIpv6NetworkAddress_Type()
)
me1200IpStatusRoutesIpv6NetworkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6NetworkAddress.setStatus("current")


class _Me1200IpStatusRoutesIpv6NetworkPrefixSize_Type(Integer32):
    """Custom type me1200IpStatusRoutesIpv6NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpStatusRoutesIpv6NetworkPrefixSize_Type.__name__ = "Integer32"
_Me1200IpStatusRoutesIpv6NetworkPrefixSize_Object = MibTableColumn
me1200IpStatusRoutesIpv6NetworkPrefixSize = _Me1200IpStatusRoutesIpv6NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 2),
    _Me1200IpStatusRoutesIpv6NetworkPrefixSize_Type()
)
me1200IpStatusRoutesIpv6NetworkPrefixSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6NetworkPrefixSize.setStatus("current")
_Me1200IpStatusRoutesIpv6NextHop_Type = InetAddressIPv6
_Me1200IpStatusRoutesIpv6NextHop_Object = MibTableColumn
me1200IpStatusRoutesIpv6NextHop = _Me1200IpStatusRoutesIpv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 3),
    _Me1200IpStatusRoutesIpv6NextHop_Type()
)
me1200IpStatusRoutesIpv6NextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6NextHop.setStatus("current")
_Me1200IpStatusRoutesIpv6NextHopInterface_Type = ME1200InterfaceIndex
_Me1200IpStatusRoutesIpv6NextHopInterface_Object = MibTableColumn
me1200IpStatusRoutesIpv6NextHopInterface = _Me1200IpStatusRoutesIpv6NextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 4),
    _Me1200IpStatusRoutesIpv6NextHopInterface_Type()
)
me1200IpStatusRoutesIpv6NextHopInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6NextHopInterface.setStatus("current")
_Me1200IpStatusRoutesIpv6DerivedNextHopInterface_Type = ME1200InterfaceIndex
_Me1200IpStatusRoutesIpv6DerivedNextHopInterface_Object = MibTableColumn
me1200IpStatusRoutesIpv6DerivedNextHopInterface = _Me1200IpStatusRoutesIpv6DerivedNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 5),
    _Me1200IpStatusRoutesIpv6DerivedNextHopInterface_Type()
)
me1200IpStatusRoutesIpv6DerivedNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6DerivedNextHopInterface.setStatus("current")
_Me1200IpStatusRoutesIpv6FlagUp_Type = TruthValue
_Me1200IpStatusRoutesIpv6FlagUp_Object = MibTableColumn
me1200IpStatusRoutesIpv6FlagUp = _Me1200IpStatusRoutesIpv6FlagUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 36),
    _Me1200IpStatusRoutesIpv6FlagUp_Type()
)
me1200IpStatusRoutesIpv6FlagUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6FlagUp.setStatus("current")
_Me1200IpStatusRoutesIpv6FlagHost_Type = TruthValue
_Me1200IpStatusRoutesIpv6FlagHost_Object = MibTableColumn
me1200IpStatusRoutesIpv6FlagHost = _Me1200IpStatusRoutesIpv6FlagHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 37),
    _Me1200IpStatusRoutesIpv6FlagHost_Type()
)
me1200IpStatusRoutesIpv6FlagHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6FlagHost.setStatus("current")
_Me1200IpStatusRoutesIpv6FlagGateway_Type = TruthValue
_Me1200IpStatusRoutesIpv6FlagGateway_Object = MibTableColumn
me1200IpStatusRoutesIpv6FlagGateway = _Me1200IpStatusRoutesIpv6FlagGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 38),
    _Me1200IpStatusRoutesIpv6FlagGateway_Type()
)
me1200IpStatusRoutesIpv6FlagGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6FlagGateway.setStatus("current")
_Me1200IpStatusRoutesIpv6OwnerConf_Type = TruthValue
_Me1200IpStatusRoutesIpv6OwnerConf_Object = MibTableColumn
me1200IpStatusRoutesIpv6OwnerConf = _Me1200IpStatusRoutesIpv6OwnerConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 68),
    _Me1200IpStatusRoutesIpv6OwnerConf_Type()
)
me1200IpStatusRoutesIpv6OwnerConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6OwnerConf.setStatus("current")
_Me1200IpStatusRoutesIpv6OwnerDhcp_Type = TruthValue
_Me1200IpStatusRoutesIpv6OwnerDhcp_Object = MibTableColumn
me1200IpStatusRoutesIpv6OwnerDhcp = _Me1200IpStatusRoutesIpv6OwnerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 69),
    _Me1200IpStatusRoutesIpv6OwnerDhcp_Type()
)
me1200IpStatusRoutesIpv6OwnerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6OwnerDhcp.setStatus("current")
_Me1200IpStatusRoutesIpv6OwnerDynamic_Type = TruthValue
_Me1200IpStatusRoutesIpv6OwnerDynamic_Object = MibTableColumn
me1200IpStatusRoutesIpv6OwnerDynamic = _Me1200IpStatusRoutesIpv6OwnerDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 3, 3, 2, 1, 70),
    _Me1200IpStatusRoutesIpv6OwnerDynamic_Type()
)
me1200IpStatusRoutesIpv6OwnerDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6OwnerDynamic.setStatus("current")
_Me1200IpStatistics_ObjectIdentity = ObjectIdentity
me1200IpStatistics = _Me1200IpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4)
)
_Me1200IpStatisticsGlobals_ObjectIdentity = ObjectIdentity
me1200IpStatisticsGlobals = _Me1200IpStatisticsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1)
)
_Me1200IpStatisticsGlobalsIpv4_ObjectIdentity = ObjectIdentity
me1200IpStatisticsGlobalsIpv4 = _Me1200IpStatisticsGlobalsIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1)
)
_Me1200IpStatisticsGlobalsIpv4InReceives_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InReceives_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InReceives = _Me1200IpStatisticsGlobalsIpv4InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 1),
    _Me1200IpStatisticsGlobalsIpv4InReceives_Type()
)
me1200IpStatisticsGlobalsIpv4InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InReceives.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInReceives_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInReceives_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInReceives = _Me1200IpStatisticsGlobalsIpv4HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 2),
    _Me1200IpStatisticsGlobalsIpv4HCInReceives_Type()
)
me1200IpStatisticsGlobalsIpv4HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInReceives.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InOctets = _Me1200IpStatisticsGlobalsIpv4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 3),
    _Me1200IpStatisticsGlobalsIpv4InOctets_Type()
)
me1200IpStatisticsGlobalsIpv4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInOctets = _Me1200IpStatisticsGlobalsIpv4HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 4),
    _Me1200IpStatisticsGlobalsIpv4HCInOctets_Type()
)
me1200IpStatisticsGlobalsIpv4HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InHdrErrors_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InHdrErrors_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InHdrErrors = _Me1200IpStatisticsGlobalsIpv4InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 5),
    _Me1200IpStatisticsGlobalsIpv4InHdrErrors_Type()
)
me1200IpStatisticsGlobalsIpv4InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InHdrErrors.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InNoRoutes_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InNoRoutes_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InNoRoutes = _Me1200IpStatisticsGlobalsIpv4InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 6),
    _Me1200IpStatisticsGlobalsIpv4InNoRoutes_Type()
)
me1200IpStatisticsGlobalsIpv4InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InNoRoutes.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InAddrErrors_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InAddrErrors_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InAddrErrors = _Me1200IpStatisticsGlobalsIpv4InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 7),
    _Me1200IpStatisticsGlobalsIpv4InAddrErrors_Type()
)
me1200IpStatisticsGlobalsIpv4InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InAddrErrors.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InUnknownProtos_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InUnknownProtos_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InUnknownProtos = _Me1200IpStatisticsGlobalsIpv4InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 8),
    _Me1200IpStatisticsGlobalsIpv4InUnknownProtos_Type()
)
me1200IpStatisticsGlobalsIpv4InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InUnknownProtos.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InTruncatedPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InTruncatedPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InTruncatedPkts = _Me1200IpStatisticsGlobalsIpv4InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 9),
    _Me1200IpStatisticsGlobalsIpv4InTruncatedPkts_Type()
)
me1200IpStatisticsGlobalsIpv4InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InTruncatedPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InForwDatagrams = _Me1200IpStatisticsGlobalsIpv4InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 10),
    _Me1200IpStatisticsGlobalsIpv4InForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv4InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInForwDatagrams_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInForwDatagrams = _Me1200IpStatisticsGlobalsIpv4HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 11),
    _Me1200IpStatisticsGlobalsIpv4HCInForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv4HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4ReasmReqds_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4ReasmReqds_Object = MibScalar
me1200IpStatisticsGlobalsIpv4ReasmReqds = _Me1200IpStatisticsGlobalsIpv4ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 12),
    _Me1200IpStatisticsGlobalsIpv4ReasmReqds_Type()
)
me1200IpStatisticsGlobalsIpv4ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4ReasmReqds.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4ReasmOKs_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4ReasmOKs_Object = MibScalar
me1200IpStatisticsGlobalsIpv4ReasmOKs = _Me1200IpStatisticsGlobalsIpv4ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 13),
    _Me1200IpStatisticsGlobalsIpv4ReasmOKs_Type()
)
me1200IpStatisticsGlobalsIpv4ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4ReasmOKs.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4ReasmFails_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4ReasmFails_Object = MibScalar
me1200IpStatisticsGlobalsIpv4ReasmFails = _Me1200IpStatisticsGlobalsIpv4ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 14),
    _Me1200IpStatisticsGlobalsIpv4ReasmFails_Type()
)
me1200IpStatisticsGlobalsIpv4ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4ReasmFails.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InDiscards_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InDiscards_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InDiscards = _Me1200IpStatisticsGlobalsIpv4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 15),
    _Me1200IpStatisticsGlobalsIpv4InDiscards_Type()
)
me1200IpStatisticsGlobalsIpv4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InDiscards.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InDelivers_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InDelivers_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InDelivers = _Me1200IpStatisticsGlobalsIpv4InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 16),
    _Me1200IpStatisticsGlobalsIpv4InDelivers_Type()
)
me1200IpStatisticsGlobalsIpv4InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InDelivers.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInDelivers_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInDelivers_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInDelivers = _Me1200IpStatisticsGlobalsIpv4HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 17),
    _Me1200IpStatisticsGlobalsIpv4HCInDelivers_Type()
)
me1200IpStatisticsGlobalsIpv4HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInDelivers.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutRequests_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutRequests_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutRequests = _Me1200IpStatisticsGlobalsIpv4OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 18),
    _Me1200IpStatisticsGlobalsIpv4OutRequests_Type()
)
me1200IpStatisticsGlobalsIpv4OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutRequests.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutRequests_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutRequests_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutRequests = _Me1200IpStatisticsGlobalsIpv4HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 19),
    _Me1200IpStatisticsGlobalsIpv4HCOutRequests_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutRequests.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutNoRoutes_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutNoRoutes_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutNoRoutes = _Me1200IpStatisticsGlobalsIpv4OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 20),
    _Me1200IpStatisticsGlobalsIpv4OutNoRoutes_Type()
)
me1200IpStatisticsGlobalsIpv4OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutNoRoutes.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutForwDatagrams = _Me1200IpStatisticsGlobalsIpv4OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 21),
    _Me1200IpStatisticsGlobalsIpv4OutForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv4OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams = _Me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 22),
    _Me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutDiscards_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutDiscards_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutDiscards = _Me1200IpStatisticsGlobalsIpv4OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 23),
    _Me1200IpStatisticsGlobalsIpv4OutDiscards_Type()
)
me1200IpStatisticsGlobalsIpv4OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutDiscards.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutFragReqds_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutFragReqds_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutFragReqds = _Me1200IpStatisticsGlobalsIpv4OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 24),
    _Me1200IpStatisticsGlobalsIpv4OutFragReqds_Type()
)
me1200IpStatisticsGlobalsIpv4OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutFragReqds.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutFragOKs_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutFragOKs_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutFragOKs = _Me1200IpStatisticsGlobalsIpv4OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 25),
    _Me1200IpStatisticsGlobalsIpv4OutFragOKs_Type()
)
me1200IpStatisticsGlobalsIpv4OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutFragOKs.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutFragFails_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutFragFails_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutFragFails = _Me1200IpStatisticsGlobalsIpv4OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 26),
    _Me1200IpStatisticsGlobalsIpv4OutFragFails_Type()
)
me1200IpStatisticsGlobalsIpv4OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutFragFails.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutFragCreates_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutFragCreates_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutFragCreates = _Me1200IpStatisticsGlobalsIpv4OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 27),
    _Me1200IpStatisticsGlobalsIpv4OutFragCreates_Type()
)
me1200IpStatisticsGlobalsIpv4OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutFragCreates.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutTransmits_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutTransmits_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutTransmits = _Me1200IpStatisticsGlobalsIpv4OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 28),
    _Me1200IpStatisticsGlobalsIpv4OutTransmits_Type()
)
me1200IpStatisticsGlobalsIpv4OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutTransmits.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutTransmits_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutTransmits_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutTransmits = _Me1200IpStatisticsGlobalsIpv4HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 29),
    _Me1200IpStatisticsGlobalsIpv4HCOutTransmits_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutTransmits.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutOctets = _Me1200IpStatisticsGlobalsIpv4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 30),
    _Me1200IpStatisticsGlobalsIpv4OutOctets_Type()
)
me1200IpStatisticsGlobalsIpv4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutOctets = _Me1200IpStatisticsGlobalsIpv4HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 31),
    _Me1200IpStatisticsGlobalsIpv4HCOutOctets_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InMcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InMcastPkts = _Me1200IpStatisticsGlobalsIpv4InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 32),
    _Me1200IpStatisticsGlobalsIpv4InMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInMcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInMcastPkts = _Me1200IpStatisticsGlobalsIpv4HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 33),
    _Me1200IpStatisticsGlobalsIpv4HCInMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InMcastOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InMcastOctets = _Me1200IpStatisticsGlobalsIpv4InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 34),
    _Me1200IpStatisticsGlobalsIpv4InMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv4InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInMcastOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInMcastOctets = _Me1200IpStatisticsGlobalsIpv4HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 35),
    _Me1200IpStatisticsGlobalsIpv4HCInMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv4HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutMcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutMcastPkts = _Me1200IpStatisticsGlobalsIpv4OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 36),
    _Me1200IpStatisticsGlobalsIpv4OutMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutMcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutMcastPkts = _Me1200IpStatisticsGlobalsIpv4HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 37),
    _Me1200IpStatisticsGlobalsIpv4HCOutMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutMcastOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutMcastOctets = _Me1200IpStatisticsGlobalsIpv4OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 38),
    _Me1200IpStatisticsGlobalsIpv4OutMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv4OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutMcastOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutMcastOctets = _Me1200IpStatisticsGlobalsIpv4HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 39),
    _Me1200IpStatisticsGlobalsIpv4HCOutMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4InBcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4InBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4InBcastPkts = _Me1200IpStatisticsGlobalsIpv4InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 40),
    _Me1200IpStatisticsGlobalsIpv4InBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCInBcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCInBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCInBcastPkts = _Me1200IpStatisticsGlobalsIpv4HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 41),
    _Me1200IpStatisticsGlobalsIpv4HCInBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCInBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4OutBcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4OutBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4OutBcastPkts = _Me1200IpStatisticsGlobalsIpv4OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 42),
    _Me1200IpStatisticsGlobalsIpv4OutBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4OutBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4HCOutBcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4HCOutBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv4HCOutBcastPkts = _Me1200IpStatisticsGlobalsIpv4HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 43),
    _Me1200IpStatisticsGlobalsIpv4HCOutBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv4HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4HCOutBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4DiscontinuityTime_Type = Counter64
_Me1200IpStatisticsGlobalsIpv4DiscontinuityTime_Object = MibScalar
me1200IpStatisticsGlobalsIpv4DiscontinuityTime = _Me1200IpStatisticsGlobalsIpv4DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 44),
    _Me1200IpStatisticsGlobalsIpv4DiscontinuityTime_Type()
)
me1200IpStatisticsGlobalsIpv4DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4DiscontinuityTime.setStatus("current")
_Me1200IpStatisticsGlobalsIpv4RefreshRate_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv4RefreshRate_Object = MibScalar
me1200IpStatisticsGlobalsIpv4RefreshRate = _Me1200IpStatisticsGlobalsIpv4RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 1, 45),
    _Me1200IpStatisticsGlobalsIpv4RefreshRate_Type()
)
me1200IpStatisticsGlobalsIpv4RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4RefreshRate.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6_ObjectIdentity = ObjectIdentity
me1200IpStatisticsGlobalsIpv6 = _Me1200IpStatisticsGlobalsIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2)
)
_Me1200IpStatisticsGlobalsIpv6InReceives_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InReceives_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InReceives = _Me1200IpStatisticsGlobalsIpv6InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 1),
    _Me1200IpStatisticsGlobalsIpv6InReceives_Type()
)
me1200IpStatisticsGlobalsIpv6InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InReceives.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInReceives_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInReceives_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInReceives = _Me1200IpStatisticsGlobalsIpv6HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 2),
    _Me1200IpStatisticsGlobalsIpv6HCInReceives_Type()
)
me1200IpStatisticsGlobalsIpv6HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInReceives.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InOctets = _Me1200IpStatisticsGlobalsIpv6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 3),
    _Me1200IpStatisticsGlobalsIpv6InOctets_Type()
)
me1200IpStatisticsGlobalsIpv6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInOctets = _Me1200IpStatisticsGlobalsIpv6HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 4),
    _Me1200IpStatisticsGlobalsIpv6HCInOctets_Type()
)
me1200IpStatisticsGlobalsIpv6HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InHdrErrors_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InHdrErrors_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InHdrErrors = _Me1200IpStatisticsGlobalsIpv6InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 5),
    _Me1200IpStatisticsGlobalsIpv6InHdrErrors_Type()
)
me1200IpStatisticsGlobalsIpv6InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InHdrErrors.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InNoRoutes_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InNoRoutes_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InNoRoutes = _Me1200IpStatisticsGlobalsIpv6InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 6),
    _Me1200IpStatisticsGlobalsIpv6InNoRoutes_Type()
)
me1200IpStatisticsGlobalsIpv6InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InNoRoutes.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InAddrErrors_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InAddrErrors_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InAddrErrors = _Me1200IpStatisticsGlobalsIpv6InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 7),
    _Me1200IpStatisticsGlobalsIpv6InAddrErrors_Type()
)
me1200IpStatisticsGlobalsIpv6InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InAddrErrors.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InUnknownProtos_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InUnknownProtos_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InUnknownProtos = _Me1200IpStatisticsGlobalsIpv6InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 8),
    _Me1200IpStatisticsGlobalsIpv6InUnknownProtos_Type()
)
me1200IpStatisticsGlobalsIpv6InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InUnknownProtos.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InTruncatedPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InTruncatedPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InTruncatedPkts = _Me1200IpStatisticsGlobalsIpv6InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 9),
    _Me1200IpStatisticsGlobalsIpv6InTruncatedPkts_Type()
)
me1200IpStatisticsGlobalsIpv6InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InTruncatedPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InForwDatagrams = _Me1200IpStatisticsGlobalsIpv6InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 10),
    _Me1200IpStatisticsGlobalsIpv6InForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv6InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInForwDatagrams_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInForwDatagrams = _Me1200IpStatisticsGlobalsIpv6HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 11),
    _Me1200IpStatisticsGlobalsIpv6HCInForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv6HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6ReasmReqds_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6ReasmReqds_Object = MibScalar
me1200IpStatisticsGlobalsIpv6ReasmReqds = _Me1200IpStatisticsGlobalsIpv6ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 12),
    _Me1200IpStatisticsGlobalsIpv6ReasmReqds_Type()
)
me1200IpStatisticsGlobalsIpv6ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6ReasmReqds.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6ReasmOKs_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6ReasmOKs_Object = MibScalar
me1200IpStatisticsGlobalsIpv6ReasmOKs = _Me1200IpStatisticsGlobalsIpv6ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 13),
    _Me1200IpStatisticsGlobalsIpv6ReasmOKs_Type()
)
me1200IpStatisticsGlobalsIpv6ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6ReasmOKs.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6ReasmFails_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6ReasmFails_Object = MibScalar
me1200IpStatisticsGlobalsIpv6ReasmFails = _Me1200IpStatisticsGlobalsIpv6ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 14),
    _Me1200IpStatisticsGlobalsIpv6ReasmFails_Type()
)
me1200IpStatisticsGlobalsIpv6ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6ReasmFails.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InDiscards_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InDiscards_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InDiscards = _Me1200IpStatisticsGlobalsIpv6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 15),
    _Me1200IpStatisticsGlobalsIpv6InDiscards_Type()
)
me1200IpStatisticsGlobalsIpv6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InDiscards.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InDelivers_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InDelivers_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InDelivers = _Me1200IpStatisticsGlobalsIpv6InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 16),
    _Me1200IpStatisticsGlobalsIpv6InDelivers_Type()
)
me1200IpStatisticsGlobalsIpv6InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InDelivers.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInDelivers_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInDelivers_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInDelivers = _Me1200IpStatisticsGlobalsIpv6HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 17),
    _Me1200IpStatisticsGlobalsIpv6HCInDelivers_Type()
)
me1200IpStatisticsGlobalsIpv6HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInDelivers.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutRequests_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutRequests_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutRequests = _Me1200IpStatisticsGlobalsIpv6OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 18),
    _Me1200IpStatisticsGlobalsIpv6OutRequests_Type()
)
me1200IpStatisticsGlobalsIpv6OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutRequests.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutRequests_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutRequests_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutRequests = _Me1200IpStatisticsGlobalsIpv6HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 19),
    _Me1200IpStatisticsGlobalsIpv6HCOutRequests_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutRequests.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutNoRoutes_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutNoRoutes_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutNoRoutes = _Me1200IpStatisticsGlobalsIpv6OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 20),
    _Me1200IpStatisticsGlobalsIpv6OutNoRoutes_Type()
)
me1200IpStatisticsGlobalsIpv6OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutNoRoutes.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutForwDatagrams = _Me1200IpStatisticsGlobalsIpv6OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 21),
    _Me1200IpStatisticsGlobalsIpv6OutForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv6OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams = _Me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 22),
    _Me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutDiscards_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutDiscards_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutDiscards = _Me1200IpStatisticsGlobalsIpv6OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 23),
    _Me1200IpStatisticsGlobalsIpv6OutDiscards_Type()
)
me1200IpStatisticsGlobalsIpv6OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutDiscards.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutFragReqds_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutFragReqds_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutFragReqds = _Me1200IpStatisticsGlobalsIpv6OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 24),
    _Me1200IpStatisticsGlobalsIpv6OutFragReqds_Type()
)
me1200IpStatisticsGlobalsIpv6OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutFragReqds.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutFragOKs_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutFragOKs_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutFragOKs = _Me1200IpStatisticsGlobalsIpv6OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 25),
    _Me1200IpStatisticsGlobalsIpv6OutFragOKs_Type()
)
me1200IpStatisticsGlobalsIpv6OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutFragOKs.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutFragFails_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutFragFails_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutFragFails = _Me1200IpStatisticsGlobalsIpv6OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 26),
    _Me1200IpStatisticsGlobalsIpv6OutFragFails_Type()
)
me1200IpStatisticsGlobalsIpv6OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutFragFails.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutFragCreates_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutFragCreates_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutFragCreates = _Me1200IpStatisticsGlobalsIpv6OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 27),
    _Me1200IpStatisticsGlobalsIpv6OutFragCreates_Type()
)
me1200IpStatisticsGlobalsIpv6OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutFragCreates.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutTransmits_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutTransmits_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutTransmits = _Me1200IpStatisticsGlobalsIpv6OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 28),
    _Me1200IpStatisticsGlobalsIpv6OutTransmits_Type()
)
me1200IpStatisticsGlobalsIpv6OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutTransmits.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutTransmits_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutTransmits_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutTransmits = _Me1200IpStatisticsGlobalsIpv6HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 29),
    _Me1200IpStatisticsGlobalsIpv6HCOutTransmits_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutTransmits.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutOctets = _Me1200IpStatisticsGlobalsIpv6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 30),
    _Me1200IpStatisticsGlobalsIpv6OutOctets_Type()
)
me1200IpStatisticsGlobalsIpv6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutOctets = _Me1200IpStatisticsGlobalsIpv6HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 31),
    _Me1200IpStatisticsGlobalsIpv6HCOutOctets_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InMcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InMcastPkts = _Me1200IpStatisticsGlobalsIpv6InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 32),
    _Me1200IpStatisticsGlobalsIpv6InMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInMcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInMcastPkts = _Me1200IpStatisticsGlobalsIpv6HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 33),
    _Me1200IpStatisticsGlobalsIpv6HCInMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InMcastOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InMcastOctets = _Me1200IpStatisticsGlobalsIpv6InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 34),
    _Me1200IpStatisticsGlobalsIpv6InMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv6InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInMcastOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInMcastOctets = _Me1200IpStatisticsGlobalsIpv6HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 35),
    _Me1200IpStatisticsGlobalsIpv6HCInMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv6HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutMcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutMcastPkts = _Me1200IpStatisticsGlobalsIpv6OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 36),
    _Me1200IpStatisticsGlobalsIpv6OutMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutMcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutMcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutMcastPkts = _Me1200IpStatisticsGlobalsIpv6HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 37),
    _Me1200IpStatisticsGlobalsIpv6HCOutMcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutMcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutMcastOctets_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutMcastOctets = _Me1200IpStatisticsGlobalsIpv6OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 38),
    _Me1200IpStatisticsGlobalsIpv6OutMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv6OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutMcastOctets_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutMcastOctets_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutMcastOctets = _Me1200IpStatisticsGlobalsIpv6HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 39),
    _Me1200IpStatisticsGlobalsIpv6HCOutMcastOctets_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutMcastOctets.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6InBcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6InBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6InBcastPkts = _Me1200IpStatisticsGlobalsIpv6InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 40),
    _Me1200IpStatisticsGlobalsIpv6InBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCInBcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCInBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCInBcastPkts = _Me1200IpStatisticsGlobalsIpv6HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 41),
    _Me1200IpStatisticsGlobalsIpv6HCInBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCInBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6OutBcastPkts_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6OutBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6OutBcastPkts = _Me1200IpStatisticsGlobalsIpv6OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 42),
    _Me1200IpStatisticsGlobalsIpv6OutBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6OutBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6HCOutBcastPkts_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6HCOutBcastPkts_Object = MibScalar
me1200IpStatisticsGlobalsIpv6HCOutBcastPkts = _Me1200IpStatisticsGlobalsIpv6HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 43),
    _Me1200IpStatisticsGlobalsIpv6HCOutBcastPkts_Type()
)
me1200IpStatisticsGlobalsIpv6HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6HCOutBcastPkts.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6DiscontinuityTime_Type = Counter64
_Me1200IpStatisticsGlobalsIpv6DiscontinuityTime_Object = MibScalar
me1200IpStatisticsGlobalsIpv6DiscontinuityTime = _Me1200IpStatisticsGlobalsIpv6DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 44),
    _Me1200IpStatisticsGlobalsIpv6DiscontinuityTime_Type()
)
me1200IpStatisticsGlobalsIpv6DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6DiscontinuityTime.setStatus("current")
_Me1200IpStatisticsGlobalsIpv6RefreshRate_Type = Unsigned32
_Me1200IpStatisticsGlobalsIpv6RefreshRate_Object = MibScalar
me1200IpStatisticsGlobalsIpv6RefreshRate = _Me1200IpStatisticsGlobalsIpv6RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 1, 2, 45),
    _Me1200IpStatisticsGlobalsIpv6RefreshRate_Type()
)
me1200IpStatisticsGlobalsIpv6RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6RefreshRate.setStatus("current")
_Me1200IpStatisticsInterfaces_ObjectIdentity = ObjectIdentity
me1200IpStatisticsInterfaces = _Me1200IpStatisticsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2)
)
_Me1200IpStatisticsInterfaceLinkTable_Object = MibTable
me1200IpStatisticsInterfaceLinkTable = _Me1200IpStatisticsInterfaceLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkTable.setStatus("current")
_Me1200IpStatisticsInterfaceLinkEntry_Object = MibTableRow
me1200IpStatisticsInterfaceLinkEntry = _Me1200IpStatisticsInterfaceLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1)
)
me1200IpStatisticsInterfaceLinkEntry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkEntry.setStatus("current")
_Me1200IpStatisticsInterfaceLinkIfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatisticsInterfaceLinkIfIndex_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkIfIndex = _Me1200IpStatisticsInterfaceLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 1),
    _Me1200IpStatisticsInterfaceLinkIfIndex_Type()
)
me1200IpStatisticsInterfaceLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkIfIndex.setStatus("current")
_Me1200IpStatisticsInterfaceLinkInPackets_Type = Counter64
_Me1200IpStatisticsInterfaceLinkInPackets_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkInPackets = _Me1200IpStatisticsInterfaceLinkInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 2),
    _Me1200IpStatisticsInterfaceLinkInPackets_Type()
)
me1200IpStatisticsInterfaceLinkInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkInPackets.setStatus("current")
_Me1200IpStatisticsInterfaceLinkOutPackets_Type = Counter64
_Me1200IpStatisticsInterfaceLinkOutPackets_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkOutPackets = _Me1200IpStatisticsInterfaceLinkOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 3),
    _Me1200IpStatisticsInterfaceLinkOutPackets_Type()
)
me1200IpStatisticsInterfaceLinkOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkOutPackets.setStatus("current")
_Me1200IpStatisticsInterfaceLinkInBytes_Type = Counter64
_Me1200IpStatisticsInterfaceLinkInBytes_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkInBytes = _Me1200IpStatisticsInterfaceLinkInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 4),
    _Me1200IpStatisticsInterfaceLinkInBytes_Type()
)
me1200IpStatisticsInterfaceLinkInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkInBytes.setStatus("current")
_Me1200IpStatisticsInterfaceLinkOutBytes_Type = Counter64
_Me1200IpStatisticsInterfaceLinkOutBytes_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkOutBytes = _Me1200IpStatisticsInterfaceLinkOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 5),
    _Me1200IpStatisticsInterfaceLinkOutBytes_Type()
)
me1200IpStatisticsInterfaceLinkOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkOutBytes.setStatus("current")
_Me1200IpStatisticsInterfaceLinkInMulticasts_Type = Counter64
_Me1200IpStatisticsInterfaceLinkInMulticasts_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkInMulticasts = _Me1200IpStatisticsInterfaceLinkInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 6),
    _Me1200IpStatisticsInterfaceLinkInMulticasts_Type()
)
me1200IpStatisticsInterfaceLinkInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkInMulticasts.setStatus("current")
_Me1200IpStatisticsInterfaceLinkOutMulticasts_Type = Counter64
_Me1200IpStatisticsInterfaceLinkOutMulticasts_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkOutMulticasts = _Me1200IpStatisticsInterfaceLinkOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 7),
    _Me1200IpStatisticsInterfaceLinkOutMulticasts_Type()
)
me1200IpStatisticsInterfaceLinkOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkOutMulticasts.setStatus("current")
_Me1200IpStatisticsInterfaceLinkInBroadcasts_Type = Counter64
_Me1200IpStatisticsInterfaceLinkInBroadcasts_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkInBroadcasts = _Me1200IpStatisticsInterfaceLinkInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 8),
    _Me1200IpStatisticsInterfaceLinkInBroadcasts_Type()
)
me1200IpStatisticsInterfaceLinkInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkInBroadcasts.setStatus("current")
_Me1200IpStatisticsInterfaceLinkOutBroadcasts_Type = Counter64
_Me1200IpStatisticsInterfaceLinkOutBroadcasts_Object = MibTableColumn
me1200IpStatisticsInterfaceLinkOutBroadcasts = _Me1200IpStatisticsInterfaceLinkOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 1, 1, 9),
    _Me1200IpStatisticsInterfaceLinkOutBroadcasts_Type()
)
me1200IpStatisticsInterfaceLinkOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkOutBroadcasts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4Table_Object = MibTable
me1200IpStatisticsInterfaceIpv4Table = _Me1200IpStatisticsInterfaceIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4Table.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4Entry_Object = MibTableRow
me1200IpStatisticsInterfaceIpv4Entry = _Me1200IpStatisticsInterfaceIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1)
)
me1200IpStatisticsInterfaceIpv4Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4Entry.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4IfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatisticsInterfaceIpv4IfIndex_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4IfIndex = _Me1200IpStatisticsInterfaceIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 1),
    _Me1200IpStatisticsInterfaceIpv4IfIndex_Type()
)
me1200IpStatisticsInterfaceIpv4IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4IfIndex.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InReceives_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InReceives_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InReceives = _Me1200IpStatisticsInterfaceIpv4InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 2),
    _Me1200IpStatisticsInterfaceIpv4InReceives_Type()
)
me1200IpStatisticsInterfaceIpv4InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InReceives.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInReceives_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInReceives_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInReceives = _Me1200IpStatisticsInterfaceIpv4HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 3),
    _Me1200IpStatisticsInterfaceIpv4HCInReceives_Type()
)
me1200IpStatisticsInterfaceIpv4HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInReceives.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InOctets = _Me1200IpStatisticsInterfaceIpv4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 4),
    _Me1200IpStatisticsInterfaceIpv4InOctets_Type()
)
me1200IpStatisticsInterfaceIpv4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInOctets = _Me1200IpStatisticsInterfaceIpv4HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 5),
    _Me1200IpStatisticsInterfaceIpv4HCInOctets_Type()
)
me1200IpStatisticsInterfaceIpv4HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InHdrErrors_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InHdrErrors_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InHdrErrors = _Me1200IpStatisticsInterfaceIpv4InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 6),
    _Me1200IpStatisticsInterfaceIpv4InHdrErrors_Type()
)
me1200IpStatisticsInterfaceIpv4InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InHdrErrors.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InNoRoutes_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InNoRoutes_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InNoRoutes = _Me1200IpStatisticsInterfaceIpv4InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 7),
    _Me1200IpStatisticsInterfaceIpv4InNoRoutes_Type()
)
me1200IpStatisticsInterfaceIpv4InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InNoRoutes.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InAddrErrors_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InAddrErrors_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InAddrErrors = _Me1200IpStatisticsInterfaceIpv4InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 8),
    _Me1200IpStatisticsInterfaceIpv4InAddrErrors_Type()
)
me1200IpStatisticsInterfaceIpv4InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InAddrErrors.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InUnknownProtos_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InUnknownProtos_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InUnknownProtos = _Me1200IpStatisticsInterfaceIpv4InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 9),
    _Me1200IpStatisticsInterfaceIpv4InUnknownProtos_Type()
)
me1200IpStatisticsInterfaceIpv4InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InUnknownProtos.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InTruncatedPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InTruncatedPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InTruncatedPkts = _Me1200IpStatisticsInterfaceIpv4InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 10),
    _Me1200IpStatisticsInterfaceIpv4InTruncatedPkts_Type()
)
me1200IpStatisticsInterfaceIpv4InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InTruncatedPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InForwDatagrams = _Me1200IpStatisticsInterfaceIpv4InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 11),
    _Me1200IpStatisticsInterfaceIpv4InForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv4InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInForwDatagrams_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInForwDatagrams = _Me1200IpStatisticsInterfaceIpv4HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 12),
    _Me1200IpStatisticsInterfaceIpv4HCInForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv4HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4ReasmReqds_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4ReasmReqds_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4ReasmReqds = _Me1200IpStatisticsInterfaceIpv4ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 13),
    _Me1200IpStatisticsInterfaceIpv4ReasmReqds_Type()
)
me1200IpStatisticsInterfaceIpv4ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4ReasmReqds.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4ReasmOKs_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4ReasmOKs_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4ReasmOKs = _Me1200IpStatisticsInterfaceIpv4ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 14),
    _Me1200IpStatisticsInterfaceIpv4ReasmOKs_Type()
)
me1200IpStatisticsInterfaceIpv4ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4ReasmOKs.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4ReasmFails_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4ReasmFails_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4ReasmFails = _Me1200IpStatisticsInterfaceIpv4ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 15),
    _Me1200IpStatisticsInterfaceIpv4ReasmFails_Type()
)
me1200IpStatisticsInterfaceIpv4ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4ReasmFails.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InDiscards_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InDiscards_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InDiscards = _Me1200IpStatisticsInterfaceIpv4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 16),
    _Me1200IpStatisticsInterfaceIpv4InDiscards_Type()
)
me1200IpStatisticsInterfaceIpv4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InDiscards.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InDelivers_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InDelivers_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InDelivers = _Me1200IpStatisticsInterfaceIpv4InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 17),
    _Me1200IpStatisticsInterfaceIpv4InDelivers_Type()
)
me1200IpStatisticsInterfaceIpv4InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InDelivers.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInDelivers_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInDelivers_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInDelivers = _Me1200IpStatisticsInterfaceIpv4HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 18),
    _Me1200IpStatisticsInterfaceIpv4HCInDelivers_Type()
)
me1200IpStatisticsInterfaceIpv4HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInDelivers.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutRequests_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutRequests_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutRequests = _Me1200IpStatisticsInterfaceIpv4OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 19),
    _Me1200IpStatisticsInterfaceIpv4OutRequests_Type()
)
me1200IpStatisticsInterfaceIpv4OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutRequests.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutRequests_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutRequests_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutRequests = _Me1200IpStatisticsInterfaceIpv4HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 20),
    _Me1200IpStatisticsInterfaceIpv4HCOutRequests_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutRequests.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutNoRoutes_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutNoRoutes_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutNoRoutes = _Me1200IpStatisticsInterfaceIpv4OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 21),
    _Me1200IpStatisticsInterfaceIpv4OutNoRoutes_Type()
)
me1200IpStatisticsInterfaceIpv4OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutNoRoutes.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutForwDatagrams = _Me1200IpStatisticsInterfaceIpv4OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 22),
    _Me1200IpStatisticsInterfaceIpv4OutForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv4OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams = _Me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 23),
    _Me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutDiscards_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutDiscards_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutDiscards = _Me1200IpStatisticsInterfaceIpv4OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 24),
    _Me1200IpStatisticsInterfaceIpv4OutDiscards_Type()
)
me1200IpStatisticsInterfaceIpv4OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutDiscards.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutFragReqds_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutFragReqds_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutFragReqds = _Me1200IpStatisticsInterfaceIpv4OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 25),
    _Me1200IpStatisticsInterfaceIpv4OutFragReqds_Type()
)
me1200IpStatisticsInterfaceIpv4OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutFragReqds.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutFragOKs_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutFragOKs_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutFragOKs = _Me1200IpStatisticsInterfaceIpv4OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 26),
    _Me1200IpStatisticsInterfaceIpv4OutFragOKs_Type()
)
me1200IpStatisticsInterfaceIpv4OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutFragOKs.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutFragFails_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutFragFails_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutFragFails = _Me1200IpStatisticsInterfaceIpv4OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 27),
    _Me1200IpStatisticsInterfaceIpv4OutFragFails_Type()
)
me1200IpStatisticsInterfaceIpv4OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutFragFails.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutFragCreates_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutFragCreates_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutFragCreates = _Me1200IpStatisticsInterfaceIpv4OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 28),
    _Me1200IpStatisticsInterfaceIpv4OutFragCreates_Type()
)
me1200IpStatisticsInterfaceIpv4OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutFragCreates.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutTransmits_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutTransmits_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutTransmits = _Me1200IpStatisticsInterfaceIpv4OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 29),
    _Me1200IpStatisticsInterfaceIpv4OutTransmits_Type()
)
me1200IpStatisticsInterfaceIpv4OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutTransmits.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutTransmits_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutTransmits_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutTransmits = _Me1200IpStatisticsInterfaceIpv4HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 30),
    _Me1200IpStatisticsInterfaceIpv4HCOutTransmits_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutTransmits.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutOctets = _Me1200IpStatisticsInterfaceIpv4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 31),
    _Me1200IpStatisticsInterfaceIpv4OutOctets_Type()
)
me1200IpStatisticsInterfaceIpv4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutOctets = _Me1200IpStatisticsInterfaceIpv4HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 32),
    _Me1200IpStatisticsInterfaceIpv4HCOutOctets_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InMcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InMcastPkts = _Me1200IpStatisticsInterfaceIpv4InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 33),
    _Me1200IpStatisticsInterfaceIpv4InMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInMcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInMcastPkts = _Me1200IpStatisticsInterfaceIpv4HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 34),
    _Me1200IpStatisticsInterfaceIpv4HCInMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InMcastOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InMcastOctets = _Me1200IpStatisticsInterfaceIpv4InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 35),
    _Me1200IpStatisticsInterfaceIpv4InMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv4InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInMcastOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInMcastOctets = _Me1200IpStatisticsInterfaceIpv4HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 36),
    _Me1200IpStatisticsInterfaceIpv4HCInMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv4HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutMcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutMcastPkts = _Me1200IpStatisticsInterfaceIpv4OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 37),
    _Me1200IpStatisticsInterfaceIpv4OutMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutMcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutMcastPkts = _Me1200IpStatisticsInterfaceIpv4HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 38),
    _Me1200IpStatisticsInterfaceIpv4HCOutMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutMcastOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutMcastOctets = _Me1200IpStatisticsInterfaceIpv4OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 39),
    _Me1200IpStatisticsInterfaceIpv4OutMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv4OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutMcastOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutMcastOctets = _Me1200IpStatisticsInterfaceIpv4HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 40),
    _Me1200IpStatisticsInterfaceIpv4HCOutMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4InBcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4InBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4InBcastPkts = _Me1200IpStatisticsInterfaceIpv4InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 41),
    _Me1200IpStatisticsInterfaceIpv4InBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCInBcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCInBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCInBcastPkts = _Me1200IpStatisticsInterfaceIpv4HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 42),
    _Me1200IpStatisticsInterfaceIpv4HCInBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCInBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4OutBcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4OutBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4OutBcastPkts = _Me1200IpStatisticsInterfaceIpv4OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 43),
    _Me1200IpStatisticsInterfaceIpv4OutBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4OutBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4HCOutBcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4HCOutBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4HCOutBcastPkts = _Me1200IpStatisticsInterfaceIpv4HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 44),
    _Me1200IpStatisticsInterfaceIpv4HCOutBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv4HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4HCOutBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4DiscontinuityTime_Type = Counter64
_Me1200IpStatisticsInterfaceIpv4DiscontinuityTime_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4DiscontinuityTime = _Me1200IpStatisticsInterfaceIpv4DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 45),
    _Me1200IpStatisticsInterfaceIpv4DiscontinuityTime_Type()
)
me1200IpStatisticsInterfaceIpv4DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4DiscontinuityTime.setStatus("current")
_Me1200IpStatisticsInterfaceIpv4RefreshRate_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv4RefreshRate_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv4RefreshRate = _Me1200IpStatisticsInterfaceIpv4RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 2, 1, 46),
    _Me1200IpStatisticsInterfaceIpv4RefreshRate_Type()
)
me1200IpStatisticsInterfaceIpv4RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4RefreshRate.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6Table_Object = MibTable
me1200IpStatisticsInterfaceIpv6Table = _Me1200IpStatisticsInterfaceIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6Table.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6Entry_Object = MibTableRow
me1200IpStatisticsInterfaceIpv6Entry = _Me1200IpStatisticsInterfaceIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1)
)
me1200IpStatisticsInterfaceIpv6Entry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6Entry.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6IfIndex_Type = ME1200InterfaceIndex
_Me1200IpStatisticsInterfaceIpv6IfIndex_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6IfIndex = _Me1200IpStatisticsInterfaceIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 1),
    _Me1200IpStatisticsInterfaceIpv6IfIndex_Type()
)
me1200IpStatisticsInterfaceIpv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6IfIndex.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InReceives_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InReceives_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InReceives = _Me1200IpStatisticsInterfaceIpv6InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 2),
    _Me1200IpStatisticsInterfaceIpv6InReceives_Type()
)
me1200IpStatisticsInterfaceIpv6InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InReceives.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInReceives_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInReceives_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInReceives = _Me1200IpStatisticsInterfaceIpv6HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 3),
    _Me1200IpStatisticsInterfaceIpv6HCInReceives_Type()
)
me1200IpStatisticsInterfaceIpv6HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInReceives.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InOctets = _Me1200IpStatisticsInterfaceIpv6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 4),
    _Me1200IpStatisticsInterfaceIpv6InOctets_Type()
)
me1200IpStatisticsInterfaceIpv6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInOctets = _Me1200IpStatisticsInterfaceIpv6HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 5),
    _Me1200IpStatisticsInterfaceIpv6HCInOctets_Type()
)
me1200IpStatisticsInterfaceIpv6HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InHdrErrors_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InHdrErrors_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InHdrErrors = _Me1200IpStatisticsInterfaceIpv6InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 6),
    _Me1200IpStatisticsInterfaceIpv6InHdrErrors_Type()
)
me1200IpStatisticsInterfaceIpv6InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InHdrErrors.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InNoRoutes_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InNoRoutes_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InNoRoutes = _Me1200IpStatisticsInterfaceIpv6InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 7),
    _Me1200IpStatisticsInterfaceIpv6InNoRoutes_Type()
)
me1200IpStatisticsInterfaceIpv6InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InNoRoutes.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InAddrErrors_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InAddrErrors_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InAddrErrors = _Me1200IpStatisticsInterfaceIpv6InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 8),
    _Me1200IpStatisticsInterfaceIpv6InAddrErrors_Type()
)
me1200IpStatisticsInterfaceIpv6InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InAddrErrors.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InUnknownProtos_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InUnknownProtos_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InUnknownProtos = _Me1200IpStatisticsInterfaceIpv6InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 9),
    _Me1200IpStatisticsInterfaceIpv6InUnknownProtos_Type()
)
me1200IpStatisticsInterfaceIpv6InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InUnknownProtos.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InTruncatedPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InTruncatedPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InTruncatedPkts = _Me1200IpStatisticsInterfaceIpv6InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 10),
    _Me1200IpStatisticsInterfaceIpv6InTruncatedPkts_Type()
)
me1200IpStatisticsInterfaceIpv6InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InTruncatedPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InForwDatagrams = _Me1200IpStatisticsInterfaceIpv6InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 11),
    _Me1200IpStatisticsInterfaceIpv6InForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv6InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInForwDatagrams_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInForwDatagrams = _Me1200IpStatisticsInterfaceIpv6HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 12),
    _Me1200IpStatisticsInterfaceIpv6HCInForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv6HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6ReasmReqds_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6ReasmReqds_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6ReasmReqds = _Me1200IpStatisticsInterfaceIpv6ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 13),
    _Me1200IpStatisticsInterfaceIpv6ReasmReqds_Type()
)
me1200IpStatisticsInterfaceIpv6ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6ReasmReqds.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6ReasmOKs_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6ReasmOKs_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6ReasmOKs = _Me1200IpStatisticsInterfaceIpv6ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 14),
    _Me1200IpStatisticsInterfaceIpv6ReasmOKs_Type()
)
me1200IpStatisticsInterfaceIpv6ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6ReasmOKs.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6ReasmFails_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6ReasmFails_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6ReasmFails = _Me1200IpStatisticsInterfaceIpv6ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 15),
    _Me1200IpStatisticsInterfaceIpv6ReasmFails_Type()
)
me1200IpStatisticsInterfaceIpv6ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6ReasmFails.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InDiscards_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InDiscards_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InDiscards = _Me1200IpStatisticsInterfaceIpv6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 16),
    _Me1200IpStatisticsInterfaceIpv6InDiscards_Type()
)
me1200IpStatisticsInterfaceIpv6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InDiscards.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InDelivers_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InDelivers_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InDelivers = _Me1200IpStatisticsInterfaceIpv6InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 17),
    _Me1200IpStatisticsInterfaceIpv6InDelivers_Type()
)
me1200IpStatisticsInterfaceIpv6InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InDelivers.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInDelivers_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInDelivers_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInDelivers = _Me1200IpStatisticsInterfaceIpv6HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 18),
    _Me1200IpStatisticsInterfaceIpv6HCInDelivers_Type()
)
me1200IpStatisticsInterfaceIpv6HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInDelivers.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutRequests_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutRequests_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutRequests = _Me1200IpStatisticsInterfaceIpv6OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 19),
    _Me1200IpStatisticsInterfaceIpv6OutRequests_Type()
)
me1200IpStatisticsInterfaceIpv6OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutRequests.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutRequests_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutRequests_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutRequests = _Me1200IpStatisticsInterfaceIpv6HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 20),
    _Me1200IpStatisticsInterfaceIpv6HCOutRequests_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutRequests.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutNoRoutes_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutNoRoutes_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutNoRoutes = _Me1200IpStatisticsInterfaceIpv6OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 21),
    _Me1200IpStatisticsInterfaceIpv6OutNoRoutes_Type()
)
me1200IpStatisticsInterfaceIpv6OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutNoRoutes.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutForwDatagrams_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutForwDatagrams = _Me1200IpStatisticsInterfaceIpv6OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 22),
    _Me1200IpStatisticsInterfaceIpv6OutForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv6OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams = _Me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 23),
    _Me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutDiscards_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutDiscards_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutDiscards = _Me1200IpStatisticsInterfaceIpv6OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 24),
    _Me1200IpStatisticsInterfaceIpv6OutDiscards_Type()
)
me1200IpStatisticsInterfaceIpv6OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutDiscards.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutFragReqds_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutFragReqds_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutFragReqds = _Me1200IpStatisticsInterfaceIpv6OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 25),
    _Me1200IpStatisticsInterfaceIpv6OutFragReqds_Type()
)
me1200IpStatisticsInterfaceIpv6OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutFragReqds.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutFragOKs_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutFragOKs_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutFragOKs = _Me1200IpStatisticsInterfaceIpv6OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 26),
    _Me1200IpStatisticsInterfaceIpv6OutFragOKs_Type()
)
me1200IpStatisticsInterfaceIpv6OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutFragOKs.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutFragFails_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutFragFails_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutFragFails = _Me1200IpStatisticsInterfaceIpv6OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 27),
    _Me1200IpStatisticsInterfaceIpv6OutFragFails_Type()
)
me1200IpStatisticsInterfaceIpv6OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutFragFails.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutFragCreates_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutFragCreates_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutFragCreates = _Me1200IpStatisticsInterfaceIpv6OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 28),
    _Me1200IpStatisticsInterfaceIpv6OutFragCreates_Type()
)
me1200IpStatisticsInterfaceIpv6OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutFragCreates.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutTransmits_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutTransmits_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutTransmits = _Me1200IpStatisticsInterfaceIpv6OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 29),
    _Me1200IpStatisticsInterfaceIpv6OutTransmits_Type()
)
me1200IpStatisticsInterfaceIpv6OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutTransmits.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutTransmits_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutTransmits_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutTransmits = _Me1200IpStatisticsInterfaceIpv6HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 30),
    _Me1200IpStatisticsInterfaceIpv6HCOutTransmits_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutTransmits.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutOctets = _Me1200IpStatisticsInterfaceIpv6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 31),
    _Me1200IpStatisticsInterfaceIpv6OutOctets_Type()
)
me1200IpStatisticsInterfaceIpv6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutOctets = _Me1200IpStatisticsInterfaceIpv6HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 32),
    _Me1200IpStatisticsInterfaceIpv6HCOutOctets_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InMcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InMcastPkts = _Me1200IpStatisticsInterfaceIpv6InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 33),
    _Me1200IpStatisticsInterfaceIpv6InMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInMcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInMcastPkts = _Me1200IpStatisticsInterfaceIpv6HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 34),
    _Me1200IpStatisticsInterfaceIpv6HCInMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InMcastOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InMcastOctets = _Me1200IpStatisticsInterfaceIpv6InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 35),
    _Me1200IpStatisticsInterfaceIpv6InMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv6InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInMcastOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInMcastOctets = _Me1200IpStatisticsInterfaceIpv6HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 36),
    _Me1200IpStatisticsInterfaceIpv6HCInMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv6HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutMcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutMcastPkts = _Me1200IpStatisticsInterfaceIpv6OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 37),
    _Me1200IpStatisticsInterfaceIpv6OutMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutMcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutMcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutMcastPkts = _Me1200IpStatisticsInterfaceIpv6HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 38),
    _Me1200IpStatisticsInterfaceIpv6HCOutMcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutMcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutMcastOctets_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutMcastOctets = _Me1200IpStatisticsInterfaceIpv6OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 39),
    _Me1200IpStatisticsInterfaceIpv6OutMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv6OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutMcastOctets_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutMcastOctets_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutMcastOctets = _Me1200IpStatisticsInterfaceIpv6HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 40),
    _Me1200IpStatisticsInterfaceIpv6HCOutMcastOctets_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutMcastOctets.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6InBcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6InBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6InBcastPkts = _Me1200IpStatisticsInterfaceIpv6InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 41),
    _Me1200IpStatisticsInterfaceIpv6InBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCInBcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCInBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCInBcastPkts = _Me1200IpStatisticsInterfaceIpv6HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 42),
    _Me1200IpStatisticsInterfaceIpv6HCInBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCInBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6OutBcastPkts_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6OutBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6OutBcastPkts = _Me1200IpStatisticsInterfaceIpv6OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 43),
    _Me1200IpStatisticsInterfaceIpv6OutBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6OutBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6HCOutBcastPkts_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6HCOutBcastPkts_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6HCOutBcastPkts = _Me1200IpStatisticsInterfaceIpv6HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 44),
    _Me1200IpStatisticsInterfaceIpv6HCOutBcastPkts_Type()
)
me1200IpStatisticsInterfaceIpv6HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6HCOutBcastPkts.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6DiscontinuityTime_Type = Counter64
_Me1200IpStatisticsInterfaceIpv6DiscontinuityTime_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6DiscontinuityTime = _Me1200IpStatisticsInterfaceIpv6DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 45),
    _Me1200IpStatisticsInterfaceIpv6DiscontinuityTime_Type()
)
me1200IpStatisticsInterfaceIpv6DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6DiscontinuityTime.setStatus("current")
_Me1200IpStatisticsInterfaceIpv6RefreshRate_Type = Unsigned32
_Me1200IpStatisticsInterfaceIpv6RefreshRate_Object = MibTableColumn
me1200IpStatisticsInterfaceIpv6RefreshRate = _Me1200IpStatisticsInterfaceIpv6RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 4, 2, 3, 1, 46),
    _Me1200IpStatisticsInterfaceIpv6RefreshRate_Type()
)
me1200IpStatisticsInterfaceIpv6RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6RefreshRate.setStatus("current")
_Me1200IpControl_ObjectIdentity = ObjectIdentity
me1200IpControl = _Me1200IpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5)
)
_Me1200IpControlGlobals_ObjectIdentity = ObjectIdentity
me1200IpControlGlobals = _Me1200IpControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 1)
)
_Me1200IpControlGlobalsIpv4NeighbourTableClear_Type = TruthValue
_Me1200IpControlGlobalsIpv4NeighbourTableClear_Object = MibScalar
me1200IpControlGlobalsIpv4NeighbourTableClear = _Me1200IpControlGlobalsIpv4NeighbourTableClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 1, 1),
    _Me1200IpControlGlobalsIpv4NeighbourTableClear_Type()
)
me1200IpControlGlobalsIpv4NeighbourTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpControlGlobalsIpv4NeighbourTableClear.setStatus("current")
_Me1200IpControlGlobalsIpv6NeighbourTableClear_Type = TruthValue
_Me1200IpControlGlobalsIpv6NeighbourTableClear_Object = MibScalar
me1200IpControlGlobalsIpv6NeighbourTableClear = _Me1200IpControlGlobalsIpv6NeighbourTableClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 1, 2),
    _Me1200IpControlGlobalsIpv6NeighbourTableClear_Type()
)
me1200IpControlGlobalsIpv6NeighbourTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpControlGlobalsIpv6NeighbourTableClear.setStatus("current")
_Me1200IpControlGlobalsIpv4SystemStatisticsClear_Type = ME1200Unsigned8
_Me1200IpControlGlobalsIpv4SystemStatisticsClear_Object = MibScalar
me1200IpControlGlobalsIpv4SystemStatisticsClear = _Me1200IpControlGlobalsIpv4SystemStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 1, 3),
    _Me1200IpControlGlobalsIpv4SystemStatisticsClear_Type()
)
me1200IpControlGlobalsIpv4SystemStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpControlGlobalsIpv4SystemStatisticsClear.setStatus("current")
_Me1200IpControlGlobalsIpv6SystemStatisticsClear_Type = ME1200Unsigned8
_Me1200IpControlGlobalsIpv6SystemStatisticsClear_Object = MibScalar
me1200IpControlGlobalsIpv6SystemStatisticsClear = _Me1200IpControlGlobalsIpv6SystemStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 1, 4),
    _Me1200IpControlGlobalsIpv6SystemStatisticsClear_Type()
)
me1200IpControlGlobalsIpv6SystemStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpControlGlobalsIpv6SystemStatisticsClear.setStatus("current")
_Me1200IpControlInterface_ObjectIdentity = ObjectIdentity
me1200IpControlInterface = _Me1200IpControlInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 2)
)
_Me1200IpControlInterfaceDhcpClientTable_Object = MibTable
me1200IpControlInterfaceDhcpClientTable = _Me1200IpControlInterfaceDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    me1200IpControlInterfaceDhcpClientTable.setStatus("current")
_Me1200IpControlInterfaceDhcpClientEntry_Object = MibTableRow
me1200IpControlInterfaceDhcpClientEntry = _Me1200IpControlInterfaceDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 2, 1, 1)
)
me1200IpControlInterfaceDhcpClientEntry.setIndexNames(
    (0, "ME1200-IP-MIB", "me1200IpControlInterfaceDhcpClientIfIndex"),
)
if mibBuilder.loadTexts:
    me1200IpControlInterfaceDhcpClientEntry.setStatus("current")
_Me1200IpControlInterfaceDhcpClientIfIndex_Type = ME1200InterfaceIndex
_Me1200IpControlInterfaceDhcpClientIfIndex_Object = MibTableColumn
me1200IpControlInterfaceDhcpClientIfIndex = _Me1200IpControlInterfaceDhcpClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 2, 1, 1, 1),
    _Me1200IpControlInterfaceDhcpClientIfIndex_Type()
)
me1200IpControlInterfaceDhcpClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpControlInterfaceDhcpClientIfIndex.setStatus("current")
_Me1200IpControlInterfaceDhcpClientRestart_Type = TruthValue
_Me1200IpControlInterfaceDhcpClientRestart_Object = MibTableColumn
me1200IpControlInterfaceDhcpClientRestart = _Me1200IpControlInterfaceDhcpClientRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 1, 5, 2, 1, 1, 2),
    _Me1200IpControlInterfaceDhcpClientRestart_Type()
)
me1200IpControlInterfaceDhcpClientRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpControlInterfaceDhcpClientRestart.setStatus("current")
_Me1200IpMIBConformance_ObjectIdentity = ObjectIdentity
me1200IpMIBConformance = _Me1200IpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2)
)
_Me1200IpMIBCompliances_ObjectIdentity = ObjectIdentity
me1200IpMIBCompliances = _Me1200IpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 1)
)
_Me1200IpMIBGroups_ObjectIdentity = ObjectIdentity
me1200IpMIBGroups = _Me1200IpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2)
)

# Managed Objects groups

me1200IpCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 1)
)
me1200IpCapabilitiesInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpCapabilitiesHasIpv4HostCapabilities"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesHasIpv6HostCapabilities"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesMaxNumberOfIpInterfaces"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesMaxNumberOfStaticRoutes"),
        ("ME1200-IP-MIB", "me1200IpCapabilitiesNumberOfLpmHardwareEntries"))
)
if mibBuilder.loadTexts:
    me1200IpCapabilitiesInfoGroup.setStatus("current")

me1200IpConfigGlobalsMainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 2)
)
me1200IpConfigGlobalsMainInfoGroup.setObjects(
    ("ME1200-IP-MIB", "me1200IpConfigGlobalsMainEnableRouting")
)
if mibBuilder.loadTexts:
    me1200IpConfigGlobalsMainInfoGroup.setStatus("current")

me1200IpConfigInterfacesIpv6TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 3)
)
me1200IpConfigInterfacesIpv6TableInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv6Active"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv6Ipv6Address"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv6PrefixSize"))
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv6TableInfoGroup.setStatus("current")

me1200IpConfigInterfacesTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 4)
)
me1200IpConfigInterfacesTableInfoGroup.setObjects(
    ("ME1200-IP-MIB", "me1200IpConfigInterfacesAction")
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesTableInfoGroup.setStatus("current")

me1200IpConfigInterfacesTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 5)
)
me1200IpConfigInterfacesTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpConfigInterfacesTableRowEditorIfIndex"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesTableRowEditorInfoGroup.setStatus("current")

me1200IpConfigInterfacesIpv4TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 6)
)
me1200IpConfigInterfacesIpv4TableInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4Active"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4EnableDhcpClient"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4Ipv4Address"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4PrefixSize"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout"))
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesIpv4TableInfoGroup.setStatus("current")

me1200IpConfigInterfacesRoutesIpv4TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 7)
)
me1200IpConfigInterfacesRoutesIpv4TableInfoGroup.setObjects(
    ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4Action")
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4TableInfoGroup.setStatus("current")

me1200IpConfigInterfacesRoutesIpv4RowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 8)
)
me1200IpConfigInterfacesRoutesIpv4RowEditorInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4RowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv4RowEditorInfoGroup.setStatus("current")

me1200IpConfigInterfacesRoutesIpv6TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 9)
)
me1200IpConfigInterfacesRoutesIpv6TableInfoGroup.setObjects(
    ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6Action")
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6TableInfoGroup.setStatus("current")

me1200IpConfigInterfacesRoutesIpv6RowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 10)
)
me1200IpConfigInterfacesRoutesIpv6RowEditorInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6RowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpConfigInterfacesRoutesIpv6RowEditorInfoGroup.setStatus("current")

me1200IpStatusGlobalsIpv4NeighbourInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 11)
)
me1200IpStatusGlobalsIpv4NeighbourInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusGlobalsIpv4NeighbourMacAddress"),
        ("ME1200-IP-MIB", "me1200IpStatusGlobalsIpv4NeighbourInterface"))
)
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv4NeighbourInfoGroup.setStatus("current")

me1200IpStatusGlobalsIpv6NeighbourInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 12)
)
me1200IpStatusGlobalsIpv6NeighbourInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusGlobalsIpv6NeighbourMacAddress"),
        ("ME1200-IP-MIB", "me1200IpStatusGlobalsIpv6NeighbourInterface"))
)
if mibBuilder.loadTexts:
    me1200IpStatusGlobalsIpv6NeighbourInfoGroup.setStatus("current")

me1200IpStatusInterfaceLinkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 13)
)
me1200IpStatusInterfaceLinkInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkOsInterfaceIndex"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkMtu"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkMacAddress"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkUp"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkBroadcast"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkLoopback"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkRunning"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkNoarp"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkPromisc"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkMulticast"))
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceLinkInfoGroup.setStatus("current")

me1200IpStatusInterfaceIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 14)
)
me1200IpStatusInterfaceIpv4InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4Address"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4Prefix"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4Broadcast"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4ReasmMaxSize"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4ArpRetransmitTime"))
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv4InfoGroup.setStatus("current")

me1200IpStatusInterfaceDhcpClientV4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 15)
)
me1200IpStatusInterfaceDhcpClientV4InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusInterfaceDhcpClientV4State"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceDhcpClientV4ServerIp"))
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceDhcpClientV4InfoGroup.setStatus("current")

me1200IpStatusInterfaceIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 16)
)
me1200IpStatusInterfaceIpv6InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Address"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Prefix"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Tentative"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Duplicated"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Detached"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Nodad"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6Autoconf"))
)
if mibBuilder.loadTexts:
    me1200IpStatusInterfaceIpv6InfoGroup.setStatus("current")

me1200IpStatusRoutesIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 17)
)
me1200IpStatusRoutesIpv4InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4DerivedNextHopInterface"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4FlagUp"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4FlagHost"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4FlagGateway"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4OwnerConf"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4OwnerDhcp"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4OwnerDynamic"))
)
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv4InfoGroup.setStatus("current")

me1200IpStatusRoutesIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 18)
)
me1200IpStatusRoutesIpv6InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6DerivedNextHopInterface"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6FlagUp"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6FlagHost"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6FlagGateway"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6OwnerConf"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6OwnerDhcp"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6OwnerDynamic"))
)
if mibBuilder.loadTexts:
    me1200IpStatusRoutesIpv6InfoGroup.setStatus("current")

me1200IpStatisticsGlobalsIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 19)
)
me1200IpStatisticsGlobalsIpv4InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InHdrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InAddrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InUnknownProtos"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InTruncatedPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4ReasmReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4ReasmOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4ReasmFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutFragReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutFragOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutFragFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutFragCreates"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCInBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4OutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4HCOutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4DiscontinuityTime"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4RefreshRate"))
)
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv4InfoGroup.setStatus("current")

me1200IpStatisticsGlobalsIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 20)
)
me1200IpStatisticsGlobalsIpv6InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InHdrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InAddrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InUnknownProtos"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InTruncatedPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6ReasmReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6ReasmOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6ReasmFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutFragReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutFragOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutFragFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutFragCreates"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCInBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6OutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6HCOutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6DiscontinuityTime"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6RefreshRate"))
)
if mibBuilder.loadTexts:
    me1200IpStatisticsGlobalsIpv6InfoGroup.setStatus("current")

me1200IpStatisticsInterfaceLinkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 21)
)
me1200IpStatisticsInterfaceLinkInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkInPackets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkOutPackets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkInBytes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkOutBytes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkInMulticasts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkOutMulticasts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkInBroadcasts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkOutBroadcasts"))
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceLinkInfoGroup.setStatus("current")

me1200IpStatisticsInterfaceIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 22)
)
me1200IpStatisticsInterfaceIpv4InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InHdrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InAddrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InUnknownProtos"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InTruncatedPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4ReasmReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4ReasmOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4ReasmFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutFragReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutFragOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutFragFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutFragCreates"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCInBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4OutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4HCOutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4DiscontinuityTime"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4RefreshRate"))
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv4InfoGroup.setStatus("current")

me1200IpStatisticsInterfaceIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 23)
)
me1200IpStatisticsInterfaceIpv6InfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInReceives"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InHdrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InAddrErrors"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InUnknownProtos"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InTruncatedPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6ReasmReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6ReasmOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6ReasmFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInDelivers"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutRequests"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutNoRoutes"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutDiscards"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutFragReqds"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutFragOKs"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutFragFails"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutFragCreates"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutTransmits"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutMcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutMcastOctets"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCInBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6OutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6HCOutBcastPkts"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6DiscontinuityTime"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6RefreshRate"))
)
if mibBuilder.loadTexts:
    me1200IpStatisticsInterfaceIpv6InfoGroup.setStatus("current")

me1200IpControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 24)
)
me1200IpControlGlobalsInfoGroup.setObjects(
      *(("ME1200-IP-MIB", "me1200IpControlGlobalsIpv4NeighbourTableClear"),
        ("ME1200-IP-MIB", "me1200IpControlGlobalsIpv6NeighbourTableClear"),
        ("ME1200-IP-MIB", "me1200IpControlGlobalsIpv4SystemStatisticsClear"),
        ("ME1200-IP-MIB", "me1200IpControlGlobalsIpv6SystemStatisticsClear"))
)
if mibBuilder.loadTexts:
    me1200IpControlGlobalsInfoGroup.setStatus("current")

me1200IpControlInterfaceDhcpClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 2, 25)
)
me1200IpControlInterfaceDhcpClientInfoGroup.setObjects(
    ("ME1200-IP-MIB", "me1200IpControlInterfaceDhcpClientRestart")
)
if mibBuilder.loadTexts:
    me1200IpControlInterfaceDhcpClientInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200IpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 102, 2, 1, 1)
)
me1200IpMIBCompliance.setObjects(
      *(("ME1200-IP-MIB", "me1200IpCapabilitiesInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigGlobalsMainInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv6TableInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesTableInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesTableRowEditorInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesIpv4TableInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4TableInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv4RowEditorInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6TableInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpConfigInterfacesRoutesIpv6RowEditorInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusGlobalsIpv4NeighbourInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusGlobalsIpv6NeighbourInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceLinkInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv4InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceDhcpClientV4InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusInterfaceIpv6InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv4InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatusRoutesIpv6InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv4InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatisticsGlobalsIpv6InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceLinkInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv4InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpStatisticsInterfaceIpv6InfoGroup"),
        ("ME1200-IP-MIB", "me1200IpControlGlobalsInfoGroup"),
        ("ME1200-IP-MIB", "me1200IpControlInterfaceDhcpClientInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200IpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-IP-MIB",
    **{"ME1200DhcpClientState": ME1200DhcpClientState,
       "me1200IpMIB": me1200IpMIB,
       "me1200IpMIBObjects": me1200IpMIBObjects,
       "me1200IpCapabilities": me1200IpCapabilities,
       "me1200IpCapabilitiesHasIpv4HostCapabilities": me1200IpCapabilitiesHasIpv4HostCapabilities,
       "me1200IpCapabilitiesHasIpv6HostCapabilities": me1200IpCapabilitiesHasIpv6HostCapabilities,
       "me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities": me1200IpCapabilitiesHasIpv4UnicastRoutingCapabilities,
       "me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities": me1200IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities,
       "me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities": me1200IpCapabilitiesHasIpv6UnicastRoutingCapabilities,
       "me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities": me1200IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities,
       "me1200IpCapabilitiesMaxNumberOfIpInterfaces": me1200IpCapabilitiesMaxNumberOfIpInterfaces,
       "me1200IpCapabilitiesMaxNumberOfStaticRoutes": me1200IpCapabilitiesMaxNumberOfStaticRoutes,
       "me1200IpCapabilitiesNumberOfLpmHardwareEntries": me1200IpCapabilitiesNumberOfLpmHardwareEntries,
       "me1200IpConfig": me1200IpConfig,
       "me1200IpConfigGlobals": me1200IpConfigGlobals,
       "me1200IpConfigGlobalsMain": me1200IpConfigGlobalsMain,
       "me1200IpConfigGlobalsMainEnableRouting": me1200IpConfigGlobalsMainEnableRouting,
       "me1200IpConfigInterfacesIpv6Table": me1200IpConfigInterfacesIpv6Table,
       "me1200IpConfigInterfacesIpv6Entry": me1200IpConfigInterfacesIpv6Entry,
       "me1200IpConfigInterfacesIpv6IfIndex": me1200IpConfigInterfacesIpv6IfIndex,
       "me1200IpConfigInterfacesIpv6Active": me1200IpConfigInterfacesIpv6Active,
       "me1200IpConfigInterfacesIpv6Ipv6Address": me1200IpConfigInterfacesIpv6Ipv6Address,
       "me1200IpConfigInterfacesIpv6PrefixSize": me1200IpConfigInterfacesIpv6PrefixSize,
       "me1200IpConfigInterfaces": me1200IpConfigInterfaces,
       "me1200IpConfigInterfacesTable": me1200IpConfigInterfacesTable,
       "me1200IpConfigInterfacesEntry": me1200IpConfigInterfacesEntry,
       "me1200IpConfigInterfacesIfIndex": me1200IpConfigInterfacesIfIndex,
       "me1200IpConfigInterfacesAction": me1200IpConfigInterfacesAction,
       "me1200IpConfigInterfacesTableRowEditor": me1200IpConfigInterfacesTableRowEditor,
       "me1200IpConfigInterfacesTableRowEditorIfIndex": me1200IpConfigInterfacesTableRowEditorIfIndex,
       "me1200IpConfigInterfacesTableRowEditorAction": me1200IpConfigInterfacesTableRowEditorAction,
       "me1200IpConfigInterfacesIpv4Table": me1200IpConfigInterfacesIpv4Table,
       "me1200IpConfigInterfacesIpv4Entry": me1200IpConfigInterfacesIpv4Entry,
       "me1200IpConfigInterfacesIpv4IfIndex": me1200IpConfigInterfacesIpv4IfIndex,
       "me1200IpConfigInterfacesIpv4Active": me1200IpConfigInterfacesIpv4Active,
       "me1200IpConfigInterfacesIpv4EnableDhcpClient": me1200IpConfigInterfacesIpv4EnableDhcpClient,
       "me1200IpConfigInterfacesIpv4Ipv4Address": me1200IpConfigInterfacesIpv4Ipv4Address,
       "me1200IpConfigInterfacesIpv4PrefixSize": me1200IpConfigInterfacesIpv4PrefixSize,
       "me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout": me1200IpConfigInterfacesIpv4DhcpClientFallbackTimeout,
       "me1200IpConfigRoutes": me1200IpConfigRoutes,
       "me1200IpConfigInterfacesRoutesIpv4Table": me1200IpConfigInterfacesRoutesIpv4Table,
       "me1200IpConfigInterfacesRoutesIpv4Entry": me1200IpConfigInterfacesRoutesIpv4Entry,
       "me1200IpConfigInterfacesRoutesIpv4NetworkAddress": me1200IpConfigInterfacesRoutesIpv4NetworkAddress,
       "me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize": me1200IpConfigInterfacesRoutesIpv4NetworkPrefixSize,
       "me1200IpConfigInterfacesRoutesIpv4NextHop": me1200IpConfigInterfacesRoutesIpv4NextHop,
       "me1200IpConfigInterfacesRoutesIpv4Action": me1200IpConfigInterfacesRoutesIpv4Action,
       "me1200IpConfigInterfacesRoutesIpv4RowEditor": me1200IpConfigInterfacesRoutesIpv4RowEditor,
       "me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress": me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkAddress,
       "me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize": me1200IpConfigInterfacesRoutesIpv4RowEditorNetworkPrefixSize,
       "me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop": me1200IpConfigInterfacesRoutesIpv4RowEditorNextHop,
       "me1200IpConfigInterfacesRoutesIpv4RowEditorAction": me1200IpConfigInterfacesRoutesIpv4RowEditorAction,
       "me1200IpConfigInterfacesRoutesIpv6Table": me1200IpConfigInterfacesRoutesIpv6Table,
       "me1200IpConfigInterfacesRoutesIpv6Entry": me1200IpConfigInterfacesRoutesIpv6Entry,
       "me1200IpConfigInterfacesRoutesIpv6NetworkAddress": me1200IpConfigInterfacesRoutesIpv6NetworkAddress,
       "me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize": me1200IpConfigInterfacesRoutesIpv6NetworkPrefixSize,
       "me1200IpConfigInterfacesRoutesIpv6NextHop": me1200IpConfigInterfacesRoutesIpv6NextHop,
       "me1200IpConfigInterfacesRoutesIpv6NextHopInterface": me1200IpConfigInterfacesRoutesIpv6NextHopInterface,
       "me1200IpConfigInterfacesRoutesIpv6Action": me1200IpConfigInterfacesRoutesIpv6Action,
       "me1200IpConfigInterfacesRoutesIpv6RowEditor": me1200IpConfigInterfacesRoutesIpv6RowEditor,
       "me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress": me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkAddress,
       "me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize": me1200IpConfigInterfacesRoutesIpv6RowEditorNetworkPrefixSize,
       "me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop": me1200IpConfigInterfacesRoutesIpv6RowEditorNextHop,
       "me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface": me1200IpConfigInterfacesRoutesIpv6RowEditorNextHopInterface,
       "me1200IpConfigInterfacesRoutesIpv6RowEditorAction": me1200IpConfigInterfacesRoutesIpv6RowEditorAction,
       "me1200IpStatus": me1200IpStatus,
       "me1200IpStatusGlobals": me1200IpStatusGlobals,
       "me1200IpStatusGlobalsIpv4NeighbourTable": me1200IpStatusGlobalsIpv4NeighbourTable,
       "me1200IpStatusGlobalsIpv4NeighbourEntry": me1200IpStatusGlobalsIpv4NeighbourEntry,
       "me1200IpStatusGlobalsIpv4NeighbourIpv4": me1200IpStatusGlobalsIpv4NeighbourIpv4,
       "me1200IpStatusGlobalsIpv4NeighbourMacAddress": me1200IpStatusGlobalsIpv4NeighbourMacAddress,
       "me1200IpStatusGlobalsIpv4NeighbourInterface": me1200IpStatusGlobalsIpv4NeighbourInterface,
       "me1200IpStatusGlobalsIpv6NeighbourTable": me1200IpStatusGlobalsIpv6NeighbourTable,
       "me1200IpStatusGlobalsIpv6NeighbourEntry": me1200IpStatusGlobalsIpv6NeighbourEntry,
       "me1200IpStatusGlobalsIpv6NeighbourIpAddress": me1200IpStatusGlobalsIpv6NeighbourIpAddress,
       "me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery": me1200IpStatusGlobalsIpv6NeighbourInterfaceQuery,
       "me1200IpStatusGlobalsIpv6NeighbourMacAddress": me1200IpStatusGlobalsIpv6NeighbourMacAddress,
       "me1200IpStatusGlobalsIpv6NeighbourInterface": me1200IpStatusGlobalsIpv6NeighbourInterface,
       "me1200IpStatusInterfaces": me1200IpStatusInterfaces,
       "me1200IpStatusInterfaceLinkTable": me1200IpStatusInterfaceLinkTable,
       "me1200IpStatusInterfaceLinkEntry": me1200IpStatusInterfaceLinkEntry,
       "me1200IpStatusInterfaceLinkIfIndex": me1200IpStatusInterfaceLinkIfIndex,
       "me1200IpStatusInterfaceLinkOsInterfaceIndex": me1200IpStatusInterfaceLinkOsInterfaceIndex,
       "me1200IpStatusInterfaceLinkMtu": me1200IpStatusInterfaceLinkMtu,
       "me1200IpStatusInterfaceLinkMacAddress": me1200IpStatusInterfaceLinkMacAddress,
       "me1200IpStatusInterfaceLinkUp": me1200IpStatusInterfaceLinkUp,
       "me1200IpStatusInterfaceLinkBroadcast": me1200IpStatusInterfaceLinkBroadcast,
       "me1200IpStatusInterfaceLinkLoopback": me1200IpStatusInterfaceLinkLoopback,
       "me1200IpStatusInterfaceLinkRunning": me1200IpStatusInterfaceLinkRunning,
       "me1200IpStatusInterfaceLinkNoarp": me1200IpStatusInterfaceLinkNoarp,
       "me1200IpStatusInterfaceLinkPromisc": me1200IpStatusInterfaceLinkPromisc,
       "me1200IpStatusInterfaceLinkMulticast": me1200IpStatusInterfaceLinkMulticast,
       "me1200IpStatusInterfaceIpv4Table": me1200IpStatusInterfaceIpv4Table,
       "me1200IpStatusInterfaceIpv4Entry": me1200IpStatusInterfaceIpv4Entry,
       "me1200IpStatusInterfaceIpv4IfIndex": me1200IpStatusInterfaceIpv4IfIndex,
       "me1200IpStatusInterfaceIpv4Address": me1200IpStatusInterfaceIpv4Address,
       "me1200IpStatusInterfaceIpv4Prefix": me1200IpStatusInterfaceIpv4Prefix,
       "me1200IpStatusInterfaceIpv4Broadcast": me1200IpStatusInterfaceIpv4Broadcast,
       "me1200IpStatusInterfaceIpv4ReasmMaxSize": me1200IpStatusInterfaceIpv4ReasmMaxSize,
       "me1200IpStatusInterfaceIpv4ArpRetransmitTime": me1200IpStatusInterfaceIpv4ArpRetransmitTime,
       "me1200IpStatusInterfaceDhcpClientV4Table": me1200IpStatusInterfaceDhcpClientV4Table,
       "me1200IpStatusInterfaceDhcpClientV4Entry": me1200IpStatusInterfaceDhcpClientV4Entry,
       "me1200IpStatusInterfaceDhcpClientV4IfIndex": me1200IpStatusInterfaceDhcpClientV4IfIndex,
       "me1200IpStatusInterfaceDhcpClientV4State": me1200IpStatusInterfaceDhcpClientV4State,
       "me1200IpStatusInterfaceDhcpClientV4ServerIp": me1200IpStatusInterfaceDhcpClientV4ServerIp,
       "me1200IpStatusInterfaceIpv6Table": me1200IpStatusInterfaceIpv6Table,
       "me1200IpStatusInterfaceIpv6Entry": me1200IpStatusInterfaceIpv6Entry,
       "me1200IpStatusInterfaceIpv6IfIndex": me1200IpStatusInterfaceIpv6IfIndex,
       "me1200IpStatusInterfaceIpv6Address": me1200IpStatusInterfaceIpv6Address,
       "me1200IpStatusInterfaceIpv6Prefix": me1200IpStatusInterfaceIpv6Prefix,
       "me1200IpStatusInterfaceIpv6Tentative": me1200IpStatusInterfaceIpv6Tentative,
       "me1200IpStatusInterfaceIpv6Duplicated": me1200IpStatusInterfaceIpv6Duplicated,
       "me1200IpStatusInterfaceIpv6Detached": me1200IpStatusInterfaceIpv6Detached,
       "me1200IpStatusInterfaceIpv6Nodad": me1200IpStatusInterfaceIpv6Nodad,
       "me1200IpStatusInterfaceIpv6Autoconf": me1200IpStatusInterfaceIpv6Autoconf,
       "me1200IpStatusRoutes": me1200IpStatusRoutes,
       "me1200IpStatusRoutesIpv4Table": me1200IpStatusRoutesIpv4Table,
       "me1200IpStatusRoutesIpv4Entry": me1200IpStatusRoutesIpv4Entry,
       "me1200IpStatusRoutesIpv4NetworkAddress": me1200IpStatusRoutesIpv4NetworkAddress,
       "me1200IpStatusRoutesIpv4NetworkPrefixSize": me1200IpStatusRoutesIpv4NetworkPrefixSize,
       "me1200IpStatusRoutesIpv4NextHop": me1200IpStatusRoutesIpv4NextHop,
       "me1200IpStatusRoutesIpv4DerivedNextHopInterface": me1200IpStatusRoutesIpv4DerivedNextHopInterface,
       "me1200IpStatusRoutesIpv4FlagUp": me1200IpStatusRoutesIpv4FlagUp,
       "me1200IpStatusRoutesIpv4FlagHost": me1200IpStatusRoutesIpv4FlagHost,
       "me1200IpStatusRoutesIpv4FlagGateway": me1200IpStatusRoutesIpv4FlagGateway,
       "me1200IpStatusRoutesIpv4OwnerConf": me1200IpStatusRoutesIpv4OwnerConf,
       "me1200IpStatusRoutesIpv4OwnerDhcp": me1200IpStatusRoutesIpv4OwnerDhcp,
       "me1200IpStatusRoutesIpv4OwnerDynamic": me1200IpStatusRoutesIpv4OwnerDynamic,
       "me1200IpStatusRoutesIpv6Table": me1200IpStatusRoutesIpv6Table,
       "me1200IpStatusRoutesIpv6Entry": me1200IpStatusRoutesIpv6Entry,
       "me1200IpStatusRoutesIpv6NetworkAddress": me1200IpStatusRoutesIpv6NetworkAddress,
       "me1200IpStatusRoutesIpv6NetworkPrefixSize": me1200IpStatusRoutesIpv6NetworkPrefixSize,
       "me1200IpStatusRoutesIpv6NextHop": me1200IpStatusRoutesIpv6NextHop,
       "me1200IpStatusRoutesIpv6NextHopInterface": me1200IpStatusRoutesIpv6NextHopInterface,
       "me1200IpStatusRoutesIpv6DerivedNextHopInterface": me1200IpStatusRoutesIpv6DerivedNextHopInterface,
       "me1200IpStatusRoutesIpv6FlagUp": me1200IpStatusRoutesIpv6FlagUp,
       "me1200IpStatusRoutesIpv6FlagHost": me1200IpStatusRoutesIpv6FlagHost,
       "me1200IpStatusRoutesIpv6FlagGateway": me1200IpStatusRoutesIpv6FlagGateway,
       "me1200IpStatusRoutesIpv6OwnerConf": me1200IpStatusRoutesIpv6OwnerConf,
       "me1200IpStatusRoutesIpv6OwnerDhcp": me1200IpStatusRoutesIpv6OwnerDhcp,
       "me1200IpStatusRoutesIpv6OwnerDynamic": me1200IpStatusRoutesIpv6OwnerDynamic,
       "me1200IpStatistics": me1200IpStatistics,
       "me1200IpStatisticsGlobals": me1200IpStatisticsGlobals,
       "me1200IpStatisticsGlobalsIpv4": me1200IpStatisticsGlobalsIpv4,
       "me1200IpStatisticsGlobalsIpv4InReceives": me1200IpStatisticsGlobalsIpv4InReceives,
       "me1200IpStatisticsGlobalsIpv4HCInReceives": me1200IpStatisticsGlobalsIpv4HCInReceives,
       "me1200IpStatisticsGlobalsIpv4InOctets": me1200IpStatisticsGlobalsIpv4InOctets,
       "me1200IpStatisticsGlobalsIpv4HCInOctets": me1200IpStatisticsGlobalsIpv4HCInOctets,
       "me1200IpStatisticsGlobalsIpv4InHdrErrors": me1200IpStatisticsGlobalsIpv4InHdrErrors,
       "me1200IpStatisticsGlobalsIpv4InNoRoutes": me1200IpStatisticsGlobalsIpv4InNoRoutes,
       "me1200IpStatisticsGlobalsIpv4InAddrErrors": me1200IpStatisticsGlobalsIpv4InAddrErrors,
       "me1200IpStatisticsGlobalsIpv4InUnknownProtos": me1200IpStatisticsGlobalsIpv4InUnknownProtos,
       "me1200IpStatisticsGlobalsIpv4InTruncatedPkts": me1200IpStatisticsGlobalsIpv4InTruncatedPkts,
       "me1200IpStatisticsGlobalsIpv4InForwDatagrams": me1200IpStatisticsGlobalsIpv4InForwDatagrams,
       "me1200IpStatisticsGlobalsIpv4HCInForwDatagrams": me1200IpStatisticsGlobalsIpv4HCInForwDatagrams,
       "me1200IpStatisticsGlobalsIpv4ReasmReqds": me1200IpStatisticsGlobalsIpv4ReasmReqds,
       "me1200IpStatisticsGlobalsIpv4ReasmOKs": me1200IpStatisticsGlobalsIpv4ReasmOKs,
       "me1200IpStatisticsGlobalsIpv4ReasmFails": me1200IpStatisticsGlobalsIpv4ReasmFails,
       "me1200IpStatisticsGlobalsIpv4InDiscards": me1200IpStatisticsGlobalsIpv4InDiscards,
       "me1200IpStatisticsGlobalsIpv4InDelivers": me1200IpStatisticsGlobalsIpv4InDelivers,
       "me1200IpStatisticsGlobalsIpv4HCInDelivers": me1200IpStatisticsGlobalsIpv4HCInDelivers,
       "me1200IpStatisticsGlobalsIpv4OutRequests": me1200IpStatisticsGlobalsIpv4OutRequests,
       "me1200IpStatisticsGlobalsIpv4HCOutRequests": me1200IpStatisticsGlobalsIpv4HCOutRequests,
       "me1200IpStatisticsGlobalsIpv4OutNoRoutes": me1200IpStatisticsGlobalsIpv4OutNoRoutes,
       "me1200IpStatisticsGlobalsIpv4OutForwDatagrams": me1200IpStatisticsGlobalsIpv4OutForwDatagrams,
       "me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams": me1200IpStatisticsGlobalsIpv4HCOutForwDatagrams,
       "me1200IpStatisticsGlobalsIpv4OutDiscards": me1200IpStatisticsGlobalsIpv4OutDiscards,
       "me1200IpStatisticsGlobalsIpv4OutFragReqds": me1200IpStatisticsGlobalsIpv4OutFragReqds,
       "me1200IpStatisticsGlobalsIpv4OutFragOKs": me1200IpStatisticsGlobalsIpv4OutFragOKs,
       "me1200IpStatisticsGlobalsIpv4OutFragFails": me1200IpStatisticsGlobalsIpv4OutFragFails,
       "me1200IpStatisticsGlobalsIpv4OutFragCreates": me1200IpStatisticsGlobalsIpv4OutFragCreates,
       "me1200IpStatisticsGlobalsIpv4OutTransmits": me1200IpStatisticsGlobalsIpv4OutTransmits,
       "me1200IpStatisticsGlobalsIpv4HCOutTransmits": me1200IpStatisticsGlobalsIpv4HCOutTransmits,
       "me1200IpStatisticsGlobalsIpv4OutOctets": me1200IpStatisticsGlobalsIpv4OutOctets,
       "me1200IpStatisticsGlobalsIpv4HCOutOctets": me1200IpStatisticsGlobalsIpv4HCOutOctets,
       "me1200IpStatisticsGlobalsIpv4InMcastPkts": me1200IpStatisticsGlobalsIpv4InMcastPkts,
       "me1200IpStatisticsGlobalsIpv4HCInMcastPkts": me1200IpStatisticsGlobalsIpv4HCInMcastPkts,
       "me1200IpStatisticsGlobalsIpv4InMcastOctets": me1200IpStatisticsGlobalsIpv4InMcastOctets,
       "me1200IpStatisticsGlobalsIpv4HCInMcastOctets": me1200IpStatisticsGlobalsIpv4HCInMcastOctets,
       "me1200IpStatisticsGlobalsIpv4OutMcastPkts": me1200IpStatisticsGlobalsIpv4OutMcastPkts,
       "me1200IpStatisticsGlobalsIpv4HCOutMcastPkts": me1200IpStatisticsGlobalsIpv4HCOutMcastPkts,
       "me1200IpStatisticsGlobalsIpv4OutMcastOctets": me1200IpStatisticsGlobalsIpv4OutMcastOctets,
       "me1200IpStatisticsGlobalsIpv4HCOutMcastOctets": me1200IpStatisticsGlobalsIpv4HCOutMcastOctets,
       "me1200IpStatisticsGlobalsIpv4InBcastPkts": me1200IpStatisticsGlobalsIpv4InBcastPkts,
       "me1200IpStatisticsGlobalsIpv4HCInBcastPkts": me1200IpStatisticsGlobalsIpv4HCInBcastPkts,
       "me1200IpStatisticsGlobalsIpv4OutBcastPkts": me1200IpStatisticsGlobalsIpv4OutBcastPkts,
       "me1200IpStatisticsGlobalsIpv4HCOutBcastPkts": me1200IpStatisticsGlobalsIpv4HCOutBcastPkts,
       "me1200IpStatisticsGlobalsIpv4DiscontinuityTime": me1200IpStatisticsGlobalsIpv4DiscontinuityTime,
       "me1200IpStatisticsGlobalsIpv4RefreshRate": me1200IpStatisticsGlobalsIpv4RefreshRate,
       "me1200IpStatisticsGlobalsIpv6": me1200IpStatisticsGlobalsIpv6,
       "me1200IpStatisticsGlobalsIpv6InReceives": me1200IpStatisticsGlobalsIpv6InReceives,
       "me1200IpStatisticsGlobalsIpv6HCInReceives": me1200IpStatisticsGlobalsIpv6HCInReceives,
       "me1200IpStatisticsGlobalsIpv6InOctets": me1200IpStatisticsGlobalsIpv6InOctets,
       "me1200IpStatisticsGlobalsIpv6HCInOctets": me1200IpStatisticsGlobalsIpv6HCInOctets,
       "me1200IpStatisticsGlobalsIpv6InHdrErrors": me1200IpStatisticsGlobalsIpv6InHdrErrors,
       "me1200IpStatisticsGlobalsIpv6InNoRoutes": me1200IpStatisticsGlobalsIpv6InNoRoutes,
       "me1200IpStatisticsGlobalsIpv6InAddrErrors": me1200IpStatisticsGlobalsIpv6InAddrErrors,
       "me1200IpStatisticsGlobalsIpv6InUnknownProtos": me1200IpStatisticsGlobalsIpv6InUnknownProtos,
       "me1200IpStatisticsGlobalsIpv6InTruncatedPkts": me1200IpStatisticsGlobalsIpv6InTruncatedPkts,
       "me1200IpStatisticsGlobalsIpv6InForwDatagrams": me1200IpStatisticsGlobalsIpv6InForwDatagrams,
       "me1200IpStatisticsGlobalsIpv6HCInForwDatagrams": me1200IpStatisticsGlobalsIpv6HCInForwDatagrams,
       "me1200IpStatisticsGlobalsIpv6ReasmReqds": me1200IpStatisticsGlobalsIpv6ReasmReqds,
       "me1200IpStatisticsGlobalsIpv6ReasmOKs": me1200IpStatisticsGlobalsIpv6ReasmOKs,
       "me1200IpStatisticsGlobalsIpv6ReasmFails": me1200IpStatisticsGlobalsIpv6ReasmFails,
       "me1200IpStatisticsGlobalsIpv6InDiscards": me1200IpStatisticsGlobalsIpv6InDiscards,
       "me1200IpStatisticsGlobalsIpv6InDelivers": me1200IpStatisticsGlobalsIpv6InDelivers,
       "me1200IpStatisticsGlobalsIpv6HCInDelivers": me1200IpStatisticsGlobalsIpv6HCInDelivers,
       "me1200IpStatisticsGlobalsIpv6OutRequests": me1200IpStatisticsGlobalsIpv6OutRequests,
       "me1200IpStatisticsGlobalsIpv6HCOutRequests": me1200IpStatisticsGlobalsIpv6HCOutRequests,
       "me1200IpStatisticsGlobalsIpv6OutNoRoutes": me1200IpStatisticsGlobalsIpv6OutNoRoutes,
       "me1200IpStatisticsGlobalsIpv6OutForwDatagrams": me1200IpStatisticsGlobalsIpv6OutForwDatagrams,
       "me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams": me1200IpStatisticsGlobalsIpv6HCOutForwDatagrams,
       "me1200IpStatisticsGlobalsIpv6OutDiscards": me1200IpStatisticsGlobalsIpv6OutDiscards,
       "me1200IpStatisticsGlobalsIpv6OutFragReqds": me1200IpStatisticsGlobalsIpv6OutFragReqds,
       "me1200IpStatisticsGlobalsIpv6OutFragOKs": me1200IpStatisticsGlobalsIpv6OutFragOKs,
       "me1200IpStatisticsGlobalsIpv6OutFragFails": me1200IpStatisticsGlobalsIpv6OutFragFails,
       "me1200IpStatisticsGlobalsIpv6OutFragCreates": me1200IpStatisticsGlobalsIpv6OutFragCreates,
       "me1200IpStatisticsGlobalsIpv6OutTransmits": me1200IpStatisticsGlobalsIpv6OutTransmits,
       "me1200IpStatisticsGlobalsIpv6HCOutTransmits": me1200IpStatisticsGlobalsIpv6HCOutTransmits,
       "me1200IpStatisticsGlobalsIpv6OutOctets": me1200IpStatisticsGlobalsIpv6OutOctets,
       "me1200IpStatisticsGlobalsIpv6HCOutOctets": me1200IpStatisticsGlobalsIpv6HCOutOctets,
       "me1200IpStatisticsGlobalsIpv6InMcastPkts": me1200IpStatisticsGlobalsIpv6InMcastPkts,
       "me1200IpStatisticsGlobalsIpv6HCInMcastPkts": me1200IpStatisticsGlobalsIpv6HCInMcastPkts,
       "me1200IpStatisticsGlobalsIpv6InMcastOctets": me1200IpStatisticsGlobalsIpv6InMcastOctets,
       "me1200IpStatisticsGlobalsIpv6HCInMcastOctets": me1200IpStatisticsGlobalsIpv6HCInMcastOctets,
       "me1200IpStatisticsGlobalsIpv6OutMcastPkts": me1200IpStatisticsGlobalsIpv6OutMcastPkts,
       "me1200IpStatisticsGlobalsIpv6HCOutMcastPkts": me1200IpStatisticsGlobalsIpv6HCOutMcastPkts,
       "me1200IpStatisticsGlobalsIpv6OutMcastOctets": me1200IpStatisticsGlobalsIpv6OutMcastOctets,
       "me1200IpStatisticsGlobalsIpv6HCOutMcastOctets": me1200IpStatisticsGlobalsIpv6HCOutMcastOctets,
       "me1200IpStatisticsGlobalsIpv6InBcastPkts": me1200IpStatisticsGlobalsIpv6InBcastPkts,
       "me1200IpStatisticsGlobalsIpv6HCInBcastPkts": me1200IpStatisticsGlobalsIpv6HCInBcastPkts,
       "me1200IpStatisticsGlobalsIpv6OutBcastPkts": me1200IpStatisticsGlobalsIpv6OutBcastPkts,
       "me1200IpStatisticsGlobalsIpv6HCOutBcastPkts": me1200IpStatisticsGlobalsIpv6HCOutBcastPkts,
       "me1200IpStatisticsGlobalsIpv6DiscontinuityTime": me1200IpStatisticsGlobalsIpv6DiscontinuityTime,
       "me1200IpStatisticsGlobalsIpv6RefreshRate": me1200IpStatisticsGlobalsIpv6RefreshRate,
       "me1200IpStatisticsInterfaces": me1200IpStatisticsInterfaces,
       "me1200IpStatisticsInterfaceLinkTable": me1200IpStatisticsInterfaceLinkTable,
       "me1200IpStatisticsInterfaceLinkEntry": me1200IpStatisticsInterfaceLinkEntry,
       "me1200IpStatisticsInterfaceLinkIfIndex": me1200IpStatisticsInterfaceLinkIfIndex,
       "me1200IpStatisticsInterfaceLinkInPackets": me1200IpStatisticsInterfaceLinkInPackets,
       "me1200IpStatisticsInterfaceLinkOutPackets": me1200IpStatisticsInterfaceLinkOutPackets,
       "me1200IpStatisticsInterfaceLinkInBytes": me1200IpStatisticsInterfaceLinkInBytes,
       "me1200IpStatisticsInterfaceLinkOutBytes": me1200IpStatisticsInterfaceLinkOutBytes,
       "me1200IpStatisticsInterfaceLinkInMulticasts": me1200IpStatisticsInterfaceLinkInMulticasts,
       "me1200IpStatisticsInterfaceLinkOutMulticasts": me1200IpStatisticsInterfaceLinkOutMulticasts,
       "me1200IpStatisticsInterfaceLinkInBroadcasts": me1200IpStatisticsInterfaceLinkInBroadcasts,
       "me1200IpStatisticsInterfaceLinkOutBroadcasts": me1200IpStatisticsInterfaceLinkOutBroadcasts,
       "me1200IpStatisticsInterfaceIpv4Table": me1200IpStatisticsInterfaceIpv4Table,
       "me1200IpStatisticsInterfaceIpv4Entry": me1200IpStatisticsInterfaceIpv4Entry,
       "me1200IpStatisticsInterfaceIpv4IfIndex": me1200IpStatisticsInterfaceIpv4IfIndex,
       "me1200IpStatisticsInterfaceIpv4InReceives": me1200IpStatisticsInterfaceIpv4InReceives,
       "me1200IpStatisticsInterfaceIpv4HCInReceives": me1200IpStatisticsInterfaceIpv4HCInReceives,
       "me1200IpStatisticsInterfaceIpv4InOctets": me1200IpStatisticsInterfaceIpv4InOctets,
       "me1200IpStatisticsInterfaceIpv4HCInOctets": me1200IpStatisticsInterfaceIpv4HCInOctets,
       "me1200IpStatisticsInterfaceIpv4InHdrErrors": me1200IpStatisticsInterfaceIpv4InHdrErrors,
       "me1200IpStatisticsInterfaceIpv4InNoRoutes": me1200IpStatisticsInterfaceIpv4InNoRoutes,
       "me1200IpStatisticsInterfaceIpv4InAddrErrors": me1200IpStatisticsInterfaceIpv4InAddrErrors,
       "me1200IpStatisticsInterfaceIpv4InUnknownProtos": me1200IpStatisticsInterfaceIpv4InUnknownProtos,
       "me1200IpStatisticsInterfaceIpv4InTruncatedPkts": me1200IpStatisticsInterfaceIpv4InTruncatedPkts,
       "me1200IpStatisticsInterfaceIpv4InForwDatagrams": me1200IpStatisticsInterfaceIpv4InForwDatagrams,
       "me1200IpStatisticsInterfaceIpv4HCInForwDatagrams": me1200IpStatisticsInterfaceIpv4HCInForwDatagrams,
       "me1200IpStatisticsInterfaceIpv4ReasmReqds": me1200IpStatisticsInterfaceIpv4ReasmReqds,
       "me1200IpStatisticsInterfaceIpv4ReasmOKs": me1200IpStatisticsInterfaceIpv4ReasmOKs,
       "me1200IpStatisticsInterfaceIpv4ReasmFails": me1200IpStatisticsInterfaceIpv4ReasmFails,
       "me1200IpStatisticsInterfaceIpv4InDiscards": me1200IpStatisticsInterfaceIpv4InDiscards,
       "me1200IpStatisticsInterfaceIpv4InDelivers": me1200IpStatisticsInterfaceIpv4InDelivers,
       "me1200IpStatisticsInterfaceIpv4HCInDelivers": me1200IpStatisticsInterfaceIpv4HCInDelivers,
       "me1200IpStatisticsInterfaceIpv4OutRequests": me1200IpStatisticsInterfaceIpv4OutRequests,
       "me1200IpStatisticsInterfaceIpv4HCOutRequests": me1200IpStatisticsInterfaceIpv4HCOutRequests,
       "me1200IpStatisticsInterfaceIpv4OutNoRoutes": me1200IpStatisticsInterfaceIpv4OutNoRoutes,
       "me1200IpStatisticsInterfaceIpv4OutForwDatagrams": me1200IpStatisticsInterfaceIpv4OutForwDatagrams,
       "me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams": me1200IpStatisticsInterfaceIpv4HCOutForwDatagrams,
       "me1200IpStatisticsInterfaceIpv4OutDiscards": me1200IpStatisticsInterfaceIpv4OutDiscards,
       "me1200IpStatisticsInterfaceIpv4OutFragReqds": me1200IpStatisticsInterfaceIpv4OutFragReqds,
       "me1200IpStatisticsInterfaceIpv4OutFragOKs": me1200IpStatisticsInterfaceIpv4OutFragOKs,
       "me1200IpStatisticsInterfaceIpv4OutFragFails": me1200IpStatisticsInterfaceIpv4OutFragFails,
       "me1200IpStatisticsInterfaceIpv4OutFragCreates": me1200IpStatisticsInterfaceIpv4OutFragCreates,
       "me1200IpStatisticsInterfaceIpv4OutTransmits": me1200IpStatisticsInterfaceIpv4OutTransmits,
       "me1200IpStatisticsInterfaceIpv4HCOutTransmits": me1200IpStatisticsInterfaceIpv4HCOutTransmits,
       "me1200IpStatisticsInterfaceIpv4OutOctets": me1200IpStatisticsInterfaceIpv4OutOctets,
       "me1200IpStatisticsInterfaceIpv4HCOutOctets": me1200IpStatisticsInterfaceIpv4HCOutOctets,
       "me1200IpStatisticsInterfaceIpv4InMcastPkts": me1200IpStatisticsInterfaceIpv4InMcastPkts,
       "me1200IpStatisticsInterfaceIpv4HCInMcastPkts": me1200IpStatisticsInterfaceIpv4HCInMcastPkts,
       "me1200IpStatisticsInterfaceIpv4InMcastOctets": me1200IpStatisticsInterfaceIpv4InMcastOctets,
       "me1200IpStatisticsInterfaceIpv4HCInMcastOctets": me1200IpStatisticsInterfaceIpv4HCInMcastOctets,
       "me1200IpStatisticsInterfaceIpv4OutMcastPkts": me1200IpStatisticsInterfaceIpv4OutMcastPkts,
       "me1200IpStatisticsInterfaceIpv4HCOutMcastPkts": me1200IpStatisticsInterfaceIpv4HCOutMcastPkts,
       "me1200IpStatisticsInterfaceIpv4OutMcastOctets": me1200IpStatisticsInterfaceIpv4OutMcastOctets,
       "me1200IpStatisticsInterfaceIpv4HCOutMcastOctets": me1200IpStatisticsInterfaceIpv4HCOutMcastOctets,
       "me1200IpStatisticsInterfaceIpv4InBcastPkts": me1200IpStatisticsInterfaceIpv4InBcastPkts,
       "me1200IpStatisticsInterfaceIpv4HCInBcastPkts": me1200IpStatisticsInterfaceIpv4HCInBcastPkts,
       "me1200IpStatisticsInterfaceIpv4OutBcastPkts": me1200IpStatisticsInterfaceIpv4OutBcastPkts,
       "me1200IpStatisticsInterfaceIpv4HCOutBcastPkts": me1200IpStatisticsInterfaceIpv4HCOutBcastPkts,
       "me1200IpStatisticsInterfaceIpv4DiscontinuityTime": me1200IpStatisticsInterfaceIpv4DiscontinuityTime,
       "me1200IpStatisticsInterfaceIpv4RefreshRate": me1200IpStatisticsInterfaceIpv4RefreshRate,
       "me1200IpStatisticsInterfaceIpv6Table": me1200IpStatisticsInterfaceIpv6Table,
       "me1200IpStatisticsInterfaceIpv6Entry": me1200IpStatisticsInterfaceIpv6Entry,
       "me1200IpStatisticsInterfaceIpv6IfIndex": me1200IpStatisticsInterfaceIpv6IfIndex,
       "me1200IpStatisticsInterfaceIpv6InReceives": me1200IpStatisticsInterfaceIpv6InReceives,
       "me1200IpStatisticsInterfaceIpv6HCInReceives": me1200IpStatisticsInterfaceIpv6HCInReceives,
       "me1200IpStatisticsInterfaceIpv6InOctets": me1200IpStatisticsInterfaceIpv6InOctets,
       "me1200IpStatisticsInterfaceIpv6HCInOctets": me1200IpStatisticsInterfaceIpv6HCInOctets,
       "me1200IpStatisticsInterfaceIpv6InHdrErrors": me1200IpStatisticsInterfaceIpv6InHdrErrors,
       "me1200IpStatisticsInterfaceIpv6InNoRoutes": me1200IpStatisticsInterfaceIpv6InNoRoutes,
       "me1200IpStatisticsInterfaceIpv6InAddrErrors": me1200IpStatisticsInterfaceIpv6InAddrErrors,
       "me1200IpStatisticsInterfaceIpv6InUnknownProtos": me1200IpStatisticsInterfaceIpv6InUnknownProtos,
       "me1200IpStatisticsInterfaceIpv6InTruncatedPkts": me1200IpStatisticsInterfaceIpv6InTruncatedPkts,
       "me1200IpStatisticsInterfaceIpv6InForwDatagrams": me1200IpStatisticsInterfaceIpv6InForwDatagrams,
       "me1200IpStatisticsInterfaceIpv6HCInForwDatagrams": me1200IpStatisticsInterfaceIpv6HCInForwDatagrams,
       "me1200IpStatisticsInterfaceIpv6ReasmReqds": me1200IpStatisticsInterfaceIpv6ReasmReqds,
       "me1200IpStatisticsInterfaceIpv6ReasmOKs": me1200IpStatisticsInterfaceIpv6ReasmOKs,
       "me1200IpStatisticsInterfaceIpv6ReasmFails": me1200IpStatisticsInterfaceIpv6ReasmFails,
       "me1200IpStatisticsInterfaceIpv6InDiscards": me1200IpStatisticsInterfaceIpv6InDiscards,
       "me1200IpStatisticsInterfaceIpv6InDelivers": me1200IpStatisticsInterfaceIpv6InDelivers,
       "me1200IpStatisticsInterfaceIpv6HCInDelivers": me1200IpStatisticsInterfaceIpv6HCInDelivers,
       "me1200IpStatisticsInterfaceIpv6OutRequests": me1200IpStatisticsInterfaceIpv6OutRequests,
       "me1200IpStatisticsInterfaceIpv6HCOutRequests": me1200IpStatisticsInterfaceIpv6HCOutRequests,
       "me1200IpStatisticsInterfaceIpv6OutNoRoutes": me1200IpStatisticsInterfaceIpv6OutNoRoutes,
       "me1200IpStatisticsInterfaceIpv6OutForwDatagrams": me1200IpStatisticsInterfaceIpv6OutForwDatagrams,
       "me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams": me1200IpStatisticsInterfaceIpv6HCOutForwDatagrams,
       "me1200IpStatisticsInterfaceIpv6OutDiscards": me1200IpStatisticsInterfaceIpv6OutDiscards,
       "me1200IpStatisticsInterfaceIpv6OutFragReqds": me1200IpStatisticsInterfaceIpv6OutFragReqds,
       "me1200IpStatisticsInterfaceIpv6OutFragOKs": me1200IpStatisticsInterfaceIpv6OutFragOKs,
       "me1200IpStatisticsInterfaceIpv6OutFragFails": me1200IpStatisticsInterfaceIpv6OutFragFails,
       "me1200IpStatisticsInterfaceIpv6OutFragCreates": me1200IpStatisticsInterfaceIpv6OutFragCreates,
       "me1200IpStatisticsInterfaceIpv6OutTransmits": me1200IpStatisticsInterfaceIpv6OutTransmits,
       "me1200IpStatisticsInterfaceIpv6HCOutTransmits": me1200IpStatisticsInterfaceIpv6HCOutTransmits,
       "me1200IpStatisticsInterfaceIpv6OutOctets": me1200IpStatisticsInterfaceIpv6OutOctets,
       "me1200IpStatisticsInterfaceIpv6HCOutOctets": me1200IpStatisticsInterfaceIpv6HCOutOctets,
       "me1200IpStatisticsInterfaceIpv6InMcastPkts": me1200IpStatisticsInterfaceIpv6InMcastPkts,
       "me1200IpStatisticsInterfaceIpv6HCInMcastPkts": me1200IpStatisticsInterfaceIpv6HCInMcastPkts,
       "me1200IpStatisticsInterfaceIpv6InMcastOctets": me1200IpStatisticsInterfaceIpv6InMcastOctets,
       "me1200IpStatisticsInterfaceIpv6HCInMcastOctets": me1200IpStatisticsInterfaceIpv6HCInMcastOctets,
       "me1200IpStatisticsInterfaceIpv6OutMcastPkts": me1200IpStatisticsInterfaceIpv6OutMcastPkts,
       "me1200IpStatisticsInterfaceIpv6HCOutMcastPkts": me1200IpStatisticsInterfaceIpv6HCOutMcastPkts,
       "me1200IpStatisticsInterfaceIpv6OutMcastOctets": me1200IpStatisticsInterfaceIpv6OutMcastOctets,
       "me1200IpStatisticsInterfaceIpv6HCOutMcastOctets": me1200IpStatisticsInterfaceIpv6HCOutMcastOctets,
       "me1200IpStatisticsInterfaceIpv6InBcastPkts": me1200IpStatisticsInterfaceIpv6InBcastPkts,
       "me1200IpStatisticsInterfaceIpv6HCInBcastPkts": me1200IpStatisticsInterfaceIpv6HCInBcastPkts,
       "me1200IpStatisticsInterfaceIpv6OutBcastPkts": me1200IpStatisticsInterfaceIpv6OutBcastPkts,
       "me1200IpStatisticsInterfaceIpv6HCOutBcastPkts": me1200IpStatisticsInterfaceIpv6HCOutBcastPkts,
       "me1200IpStatisticsInterfaceIpv6DiscontinuityTime": me1200IpStatisticsInterfaceIpv6DiscontinuityTime,
       "me1200IpStatisticsInterfaceIpv6RefreshRate": me1200IpStatisticsInterfaceIpv6RefreshRate,
       "me1200IpControl": me1200IpControl,
       "me1200IpControlGlobals": me1200IpControlGlobals,
       "me1200IpControlGlobalsIpv4NeighbourTableClear": me1200IpControlGlobalsIpv4NeighbourTableClear,
       "me1200IpControlGlobalsIpv6NeighbourTableClear": me1200IpControlGlobalsIpv6NeighbourTableClear,
       "me1200IpControlGlobalsIpv4SystemStatisticsClear": me1200IpControlGlobalsIpv4SystemStatisticsClear,
       "me1200IpControlGlobalsIpv6SystemStatisticsClear": me1200IpControlGlobalsIpv6SystemStatisticsClear,
       "me1200IpControlInterface": me1200IpControlInterface,
       "me1200IpControlInterfaceDhcpClientTable": me1200IpControlInterfaceDhcpClientTable,
       "me1200IpControlInterfaceDhcpClientEntry": me1200IpControlInterfaceDhcpClientEntry,
       "me1200IpControlInterfaceDhcpClientIfIndex": me1200IpControlInterfaceDhcpClientIfIndex,
       "me1200IpControlInterfaceDhcpClientRestart": me1200IpControlInterfaceDhcpClientRestart,
       "me1200IpMIBConformance": me1200IpMIBConformance,
       "me1200IpMIBCompliances": me1200IpMIBCompliances,
       "me1200IpMIBCompliance": me1200IpMIBCompliance,
       "me1200IpMIBGroups": me1200IpMIBGroups,
       "me1200IpCapabilitiesInfoGroup": me1200IpCapabilitiesInfoGroup,
       "me1200IpConfigGlobalsMainInfoGroup": me1200IpConfigGlobalsMainInfoGroup,
       "me1200IpConfigInterfacesIpv6TableInfoGroup": me1200IpConfigInterfacesIpv6TableInfoGroup,
       "me1200IpConfigInterfacesTableInfoGroup": me1200IpConfigInterfacesTableInfoGroup,
       "me1200IpConfigInterfacesTableRowEditorInfoGroup": me1200IpConfigInterfacesTableRowEditorInfoGroup,
       "me1200IpConfigInterfacesIpv4TableInfoGroup": me1200IpConfigInterfacesIpv4TableInfoGroup,
       "me1200IpConfigInterfacesRoutesIpv4TableInfoGroup": me1200IpConfigInterfacesRoutesIpv4TableInfoGroup,
       "me1200IpConfigInterfacesRoutesIpv4RowEditorInfoGroup": me1200IpConfigInterfacesRoutesIpv4RowEditorInfoGroup,
       "me1200IpConfigInterfacesRoutesIpv6TableInfoGroup": me1200IpConfigInterfacesRoutesIpv6TableInfoGroup,
       "me1200IpConfigInterfacesRoutesIpv6RowEditorInfoGroup": me1200IpConfigInterfacesRoutesIpv6RowEditorInfoGroup,
       "me1200IpStatusGlobalsIpv4NeighbourInfoGroup": me1200IpStatusGlobalsIpv4NeighbourInfoGroup,
       "me1200IpStatusGlobalsIpv6NeighbourInfoGroup": me1200IpStatusGlobalsIpv6NeighbourInfoGroup,
       "me1200IpStatusInterfaceLinkInfoGroup": me1200IpStatusInterfaceLinkInfoGroup,
       "me1200IpStatusInterfaceIpv4InfoGroup": me1200IpStatusInterfaceIpv4InfoGroup,
       "me1200IpStatusInterfaceDhcpClientV4InfoGroup": me1200IpStatusInterfaceDhcpClientV4InfoGroup,
       "me1200IpStatusInterfaceIpv6InfoGroup": me1200IpStatusInterfaceIpv6InfoGroup,
       "me1200IpStatusRoutesIpv4InfoGroup": me1200IpStatusRoutesIpv4InfoGroup,
       "me1200IpStatusRoutesIpv6InfoGroup": me1200IpStatusRoutesIpv6InfoGroup,
       "me1200IpStatisticsGlobalsIpv4InfoGroup": me1200IpStatisticsGlobalsIpv4InfoGroup,
       "me1200IpStatisticsGlobalsIpv6InfoGroup": me1200IpStatisticsGlobalsIpv6InfoGroup,
       "me1200IpStatisticsInterfaceLinkInfoGroup": me1200IpStatisticsInterfaceLinkInfoGroup,
       "me1200IpStatisticsInterfaceIpv4InfoGroup": me1200IpStatisticsInterfaceIpv4InfoGroup,
       "me1200IpStatisticsInterfaceIpv6InfoGroup": me1200IpStatisticsInterfaceIpv6InfoGroup,
       "me1200IpControlGlobalsInfoGroup": me1200IpControlGlobalsInfoGroup,
       "me1200IpControlInterfaceDhcpClientInfoGroup": me1200IpControlInterfaceDhcpClientInfoGroup}
)
