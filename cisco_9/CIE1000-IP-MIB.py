# SNMP MIB module (CIE1000-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-IP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000InterfaceIndex,
 CIE1000RowEditorState,
 CIE1000Unsigned8) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InterfaceIndex",
    "CIE1000RowEditorState",
    "CIE1000Unsigned8")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000IpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102)
)
if mibBuilder.loadTexts:
    cie1000IpMib.setRevisions(
        ("2015-08-24 00:00",
         "2014-10-29 00:00",
         "2014-10-21 00:00",
         "2014-09-11 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000IpDhcpClientState(TextualConvention, Integer32):
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

_Cie1000IpMibObjects_ObjectIdentity = ObjectIdentity
cie1000IpMibObjects = _Cie1000IpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1)
)
_Cie1000IpCapabilities_ObjectIdentity = ObjectIdentity
cie1000IpCapabilities = _Cie1000IpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1)
)
_Cie1000IpCapabilitiesHasIpv4HostCapabilities_Type = TruthValue
_Cie1000IpCapabilitiesHasIpv4HostCapabilities_Object = MibScalar
cie1000IpCapabilitiesHasIpv4HostCapabilities = _Cie1000IpCapabilitiesHasIpv4HostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 1),
    _Cie1000IpCapabilitiesHasIpv4HostCapabilities_Type()
)
cie1000IpCapabilitiesHasIpv4HostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasIpv4HostCapabilities.setStatus("current")
_Cie1000IpCapabilitiesHasIpv6HostCapabilities_Type = TruthValue
_Cie1000IpCapabilitiesHasIpv6HostCapabilities_Object = MibScalar
cie1000IpCapabilitiesHasIpv6HostCapabilities = _Cie1000IpCapabilitiesHasIpv6HostCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 2),
    _Cie1000IpCapabilitiesHasIpv6HostCapabilities_Type()
)
cie1000IpCapabilitiesHasIpv6HostCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasIpv6HostCapabilities.setStatus("current")
_Cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Type = TruthValue
_Cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Object = MibScalar
cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities = _Cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 3),
    _Cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities_Type()
)
cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities.setStatus("current")
_Cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Type = TruthValue
_Cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Object = MibScalar
cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities = _Cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 4),
    _Cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities_Type()
)
cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities.setStatus("current")
_Cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Type = TruthValue
_Cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Object = MibScalar
cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities = _Cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 5),
    _Cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities_Type()
)
cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities.setStatus("current")
_Cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Type = TruthValue
_Cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Object = MibScalar
cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities = _Cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 6),
    _Cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities_Type()
)
cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities.setStatus("current")
_Cie1000IpCapabilitiesMaxNumberOfIpInterfaces_Type = Unsigned32
_Cie1000IpCapabilitiesMaxNumberOfIpInterfaces_Object = MibScalar
cie1000IpCapabilitiesMaxNumberOfIpInterfaces = _Cie1000IpCapabilitiesMaxNumberOfIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 7),
    _Cie1000IpCapabilitiesMaxNumberOfIpInterfaces_Type()
)
cie1000IpCapabilitiesMaxNumberOfIpInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesMaxNumberOfIpInterfaces.setStatus("current")
_Cie1000IpCapabilitiesMaxNumberOfStaticRoutes_Type = Unsigned32
_Cie1000IpCapabilitiesMaxNumberOfStaticRoutes_Object = MibScalar
cie1000IpCapabilitiesMaxNumberOfStaticRoutes = _Cie1000IpCapabilitiesMaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 8),
    _Cie1000IpCapabilitiesMaxNumberOfStaticRoutes_Type()
)
cie1000IpCapabilitiesMaxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesMaxNumberOfStaticRoutes.setStatus("current")
_Cie1000IpCapabilitiesNumberOfLpmHardwareEntries_Type = Unsigned32
_Cie1000IpCapabilitiesNumberOfLpmHardwareEntries_Object = MibScalar
cie1000IpCapabilitiesNumberOfLpmHardwareEntries = _Cie1000IpCapabilitiesNumberOfLpmHardwareEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 9),
    _Cie1000IpCapabilitiesNumberOfLpmHardwareEntries_Type()
)
cie1000IpCapabilitiesNumberOfLpmHardwareEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesNumberOfLpmHardwareEntries.setStatus("current")
_Cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics_Type = TruthValue
_Cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics_Object = MibScalar
cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics = _Cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 10),
    _Cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics_Type()
)
cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics.setStatus("current")
_Cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics_Type = TruthValue
_Cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics_Object = MibScalar
cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics = _Cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 1, 11),
    _Cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics_Type()
)
cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics.setStatus("current")
_Cie1000IpConfig_ObjectIdentity = ObjectIdentity
cie1000IpConfig = _Cie1000IpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2)
)
_Cie1000IpConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000IpConfigGlobals = _Cie1000IpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 1)
)
_Cie1000IpConfigGlobalsMain_ObjectIdentity = ObjectIdentity
cie1000IpConfigGlobalsMain = _Cie1000IpConfigGlobalsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 1, 1)
)
_Cie1000IpConfigGlobalsMainEnableRouting_Type = TruthValue
_Cie1000IpConfigGlobalsMainEnableRouting_Object = MibScalar
cie1000IpConfigGlobalsMainEnableRouting = _Cie1000IpConfigGlobalsMainEnableRouting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 1, 1, 1),
    _Cie1000IpConfigGlobalsMainEnableRouting_Type()
)
cie1000IpConfigGlobalsMainEnableRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigGlobalsMainEnableRouting.setStatus("current")
_Cie1000IpConfigInterfaces_ObjectIdentity = ObjectIdentity
cie1000IpConfigInterfaces = _Cie1000IpConfigInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2)
)
_Cie1000IpConfigInterfacesTable_Object = MibTable
cie1000IpConfigInterfacesTable = _Cie1000IpConfigInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesTable.setStatus("current")
_Cie1000IpConfigInterfacesEntry_Object = MibTableRow
cie1000IpConfigInterfacesEntry = _Cie1000IpConfigInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 1, 1)
)
cie1000IpConfigInterfacesEntry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpConfigInterfacesIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesEntry.setStatus("current")
_Cie1000IpConfigInterfacesIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpConfigInterfacesIfIndex_Object = MibTableColumn
cie1000IpConfigInterfacesIfIndex = _Cie1000IpConfigInterfacesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 1, 1, 1),
    _Cie1000IpConfigInterfacesIfIndex_Type()
)
cie1000IpConfigInterfacesIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIfIndex.setStatus("current")
_Cie1000IpConfigInterfacesAction_Type = CIE1000RowEditorState
_Cie1000IpConfigInterfacesAction_Object = MibTableColumn
cie1000IpConfigInterfacesAction = _Cie1000IpConfigInterfacesAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 1, 1, 100),
    _Cie1000IpConfigInterfacesAction_Type()
)
cie1000IpConfigInterfacesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesAction.setStatus("current")
_Cie1000IpConfigInterfacesTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpConfigInterfacesTableRowEditor = _Cie1000IpConfigInterfacesTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 2)
)
_Cie1000IpConfigInterfacesTableRowEditorIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpConfigInterfacesTableRowEditorIfIndex_Object = MibScalar
cie1000IpConfigInterfacesTableRowEditorIfIndex = _Cie1000IpConfigInterfacesTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 2, 1),
    _Cie1000IpConfigInterfacesTableRowEditorIfIndex_Type()
)
cie1000IpConfigInterfacesTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesTableRowEditorIfIndex.setStatus("current")
_Cie1000IpConfigInterfacesTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpConfigInterfacesTableRowEditorAction_Object = MibScalar
cie1000IpConfigInterfacesTableRowEditorAction = _Cie1000IpConfigInterfacesTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 2, 100),
    _Cie1000IpConfigInterfacesTableRowEditorAction_Type()
)
cie1000IpConfigInterfacesTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesTableRowEditorAction.setStatus("current")
_Cie1000IpConfigInterfacesIpv4Table_Object = MibTable
cie1000IpConfigInterfacesIpv4Table = _Cie1000IpConfigInterfacesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4Table.setStatus("current")
_Cie1000IpConfigInterfacesIpv4Entry_Object = MibTableRow
cie1000IpConfigInterfacesIpv4Entry = _Cie1000IpConfigInterfacesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1)
)
cie1000IpConfigInterfacesIpv4Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4IfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4Entry.setStatus("current")
_Cie1000IpConfigInterfacesIpv4IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpConfigInterfacesIpv4IfIndex_Object = MibTableColumn
cie1000IpConfigInterfacesIpv4IfIndex = _Cie1000IpConfigInterfacesIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1, 1),
    _Cie1000IpConfigInterfacesIpv4IfIndex_Type()
)
cie1000IpConfigInterfacesIpv4IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4IfIndex.setStatus("current")
_Cie1000IpConfigInterfacesIpv4Active_Type = TruthValue
_Cie1000IpConfigInterfacesIpv4Active_Object = MibTableColumn
cie1000IpConfigInterfacesIpv4Active = _Cie1000IpConfigInterfacesIpv4Active_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1, 2),
    _Cie1000IpConfigInterfacesIpv4Active_Type()
)
cie1000IpConfigInterfacesIpv4Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4Active.setStatus("current")
_Cie1000IpConfigInterfacesIpv4EnableDhcpClient_Type = TruthValue
_Cie1000IpConfigInterfacesIpv4EnableDhcpClient_Object = MibTableColumn
cie1000IpConfigInterfacesIpv4EnableDhcpClient = _Cie1000IpConfigInterfacesIpv4EnableDhcpClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1, 3),
    _Cie1000IpConfigInterfacesIpv4EnableDhcpClient_Type()
)
cie1000IpConfigInterfacesIpv4EnableDhcpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4EnableDhcpClient.setStatus("current")
_Cie1000IpConfigInterfacesIpv4Ipv4Address_Type = IpAddress
_Cie1000IpConfigInterfacesIpv4Ipv4Address_Object = MibTableColumn
cie1000IpConfigInterfacesIpv4Ipv4Address = _Cie1000IpConfigInterfacesIpv4Ipv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1, 4),
    _Cie1000IpConfigInterfacesIpv4Ipv4Address_Type()
)
cie1000IpConfigInterfacesIpv4Ipv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4Ipv4Address.setStatus("current")
_Cie1000IpConfigInterfacesIpv4PrefixSize_Type = Unsigned32
_Cie1000IpConfigInterfacesIpv4PrefixSize_Object = MibTableColumn
cie1000IpConfigInterfacesIpv4PrefixSize = _Cie1000IpConfigInterfacesIpv4PrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1, 5),
    _Cie1000IpConfigInterfacesIpv4PrefixSize_Type()
)
cie1000IpConfigInterfacesIpv4PrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4PrefixSize.setStatus("current")
_Cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Type = Unsigned32
_Cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Object = MibTableColumn
cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout = _Cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 3, 1, 6),
    _Cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout_Type()
)
cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout.setStatus("current")
_Cie1000IpConfigInterfacesIpv6Table_Object = MibTable
cie1000IpConfigInterfacesIpv6Table = _Cie1000IpConfigInterfacesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6Table.setStatus("current")
_Cie1000IpConfigInterfacesIpv6Entry_Object = MibTableRow
cie1000IpConfigInterfacesIpv6Entry = _Cie1000IpConfigInterfacesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 4, 1)
)
cie1000IpConfigInterfacesIpv6Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6Entry.setStatus("current")
_Cie1000IpConfigInterfacesIpv6IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpConfigInterfacesIpv6IfIndex_Object = MibTableColumn
cie1000IpConfigInterfacesIpv6IfIndex = _Cie1000IpConfigInterfacesIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 4, 1, 1),
    _Cie1000IpConfigInterfacesIpv6IfIndex_Type()
)
cie1000IpConfigInterfacesIpv6IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6IfIndex.setStatus("current")
_Cie1000IpConfigInterfacesIpv6Active_Type = TruthValue
_Cie1000IpConfigInterfacesIpv6Active_Object = MibTableColumn
cie1000IpConfigInterfacesIpv6Active = _Cie1000IpConfigInterfacesIpv6Active_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 4, 1, 2),
    _Cie1000IpConfigInterfacesIpv6Active_Type()
)
cie1000IpConfigInterfacesIpv6Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6Active.setStatus("current")
_Cie1000IpConfigInterfacesIpv6Ipv6Address_Type = InetAddressIPv6
_Cie1000IpConfigInterfacesIpv6Ipv6Address_Object = MibTableColumn
cie1000IpConfigInterfacesIpv6Ipv6Address = _Cie1000IpConfigInterfacesIpv6Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 4, 1, 3),
    _Cie1000IpConfigInterfacesIpv6Ipv6Address_Type()
)
cie1000IpConfigInterfacesIpv6Ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6Ipv6Address.setStatus("current")
_Cie1000IpConfigInterfacesIpv6PrefixSize_Type = Unsigned32
_Cie1000IpConfigInterfacesIpv6PrefixSize_Object = MibTableColumn
cie1000IpConfigInterfacesIpv6PrefixSize = _Cie1000IpConfigInterfacesIpv6PrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 2, 4, 1, 4),
    _Cie1000IpConfigInterfacesIpv6PrefixSize_Type()
)
cie1000IpConfigInterfacesIpv6PrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6PrefixSize.setStatus("current")
_Cie1000IpConfigRoutes_ObjectIdentity = ObjectIdentity
cie1000IpConfigRoutes = _Cie1000IpConfigRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3)
)
_Cie1000IpConfigRoutesIpv4Table_Object = MibTable
cie1000IpConfigRoutesIpv4Table = _Cie1000IpConfigRoutesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4Table.setStatus("current")
_Cie1000IpConfigRoutesIpv4Entry_Object = MibTableRow
cie1000IpConfigRoutesIpv4Entry = _Cie1000IpConfigRoutesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 1, 1)
)
cie1000IpConfigRoutesIpv4Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4NetworkAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4NetworkPrefixSize"),
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4NextHop"),
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4Entry.setStatus("current")
_Cie1000IpConfigRoutesIpv4NetworkAddress_Type = IpAddress
_Cie1000IpConfigRoutesIpv4NetworkAddress_Object = MibTableColumn
cie1000IpConfigRoutesIpv4NetworkAddress = _Cie1000IpConfigRoutesIpv4NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 1, 1, 1),
    _Cie1000IpConfigRoutesIpv4NetworkAddress_Type()
)
cie1000IpConfigRoutesIpv4NetworkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4NetworkAddress.setStatus("current")


class _Cie1000IpConfigRoutesIpv4NetworkPrefixSize_Type(Integer32):
    """Custom type cie1000IpConfigRoutesIpv4NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Cie1000IpConfigRoutesIpv4NetworkPrefixSize_Type.__name__ = "Integer32"
_Cie1000IpConfigRoutesIpv4NetworkPrefixSize_Object = MibTableColumn
cie1000IpConfigRoutesIpv4NetworkPrefixSize = _Cie1000IpConfigRoutesIpv4NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 1, 1, 2),
    _Cie1000IpConfigRoutesIpv4NetworkPrefixSize_Type()
)
cie1000IpConfigRoutesIpv4NetworkPrefixSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4NetworkPrefixSize.setStatus("current")
_Cie1000IpConfigRoutesIpv4NextHop_Type = IpAddress
_Cie1000IpConfigRoutesIpv4NextHop_Object = MibTableColumn
cie1000IpConfigRoutesIpv4NextHop = _Cie1000IpConfigRoutesIpv4NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 1, 1, 3),
    _Cie1000IpConfigRoutesIpv4NextHop_Type()
)
cie1000IpConfigRoutesIpv4NextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4NextHop.setStatus("current")
_Cie1000IpConfigRoutesIpv4Action_Type = CIE1000RowEditorState
_Cie1000IpConfigRoutesIpv4Action_Object = MibTableColumn
cie1000IpConfigRoutesIpv4Action = _Cie1000IpConfigRoutesIpv4Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 1, 1, 100),
    _Cie1000IpConfigRoutesIpv4Action_Type()
)
cie1000IpConfigRoutesIpv4Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4Action.setStatus("current")
_Cie1000IpConfigRoutesIpv4RowEditor_ObjectIdentity = ObjectIdentity
cie1000IpConfigRoutesIpv4RowEditor = _Cie1000IpConfigRoutesIpv4RowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 2)
)
_Cie1000IpConfigRoutesIpv4RowEditorNetworkAddress_Type = IpAddress
_Cie1000IpConfigRoutesIpv4RowEditorNetworkAddress_Object = MibScalar
cie1000IpConfigRoutesIpv4RowEditorNetworkAddress = _Cie1000IpConfigRoutesIpv4RowEditorNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 2, 1),
    _Cie1000IpConfigRoutesIpv4RowEditorNetworkAddress_Type()
)
cie1000IpConfigRoutesIpv4RowEditorNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4RowEditorNetworkAddress.setStatus("current")


class _Cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize_Type(Integer32):
    """Custom type cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize_Type.__name__ = "Integer32"
_Cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize_Object = MibScalar
cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize = _Cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 2, 2),
    _Cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize_Type()
)
cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize.setStatus("current")
_Cie1000IpConfigRoutesIpv4RowEditorNextHop_Type = IpAddress
_Cie1000IpConfigRoutesIpv4RowEditorNextHop_Object = MibScalar
cie1000IpConfigRoutesIpv4RowEditorNextHop = _Cie1000IpConfigRoutesIpv4RowEditorNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 2, 3),
    _Cie1000IpConfigRoutesIpv4RowEditorNextHop_Type()
)
cie1000IpConfigRoutesIpv4RowEditorNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4RowEditorNextHop.setStatus("current")
_Cie1000IpConfigRoutesIpv4RowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpConfigRoutesIpv4RowEditorAction_Object = MibScalar
cie1000IpConfigRoutesIpv4RowEditorAction = _Cie1000IpConfigRoutesIpv4RowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 2, 100),
    _Cie1000IpConfigRoutesIpv4RowEditorAction_Type()
)
cie1000IpConfigRoutesIpv4RowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4RowEditorAction.setStatus("current")
_Cie1000IpConfigRoutesIpv6Table_Object = MibTable
cie1000IpConfigRoutesIpv6Table = _Cie1000IpConfigRoutesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6Table.setStatus("current")
_Cie1000IpConfigRoutesIpv6Entry_Object = MibTableRow
cie1000IpConfigRoutesIpv6Entry = _Cie1000IpConfigRoutesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3, 1)
)
cie1000IpConfigRoutesIpv6Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NetworkAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NetworkPrefixSize"),
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NextHop"),
    (0, "CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NextHopInterface"),
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6Entry.setStatus("current")
_Cie1000IpConfigRoutesIpv6NetworkAddress_Type = InetAddressIPv6
_Cie1000IpConfigRoutesIpv6NetworkAddress_Object = MibTableColumn
cie1000IpConfigRoutesIpv6NetworkAddress = _Cie1000IpConfigRoutesIpv6NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3, 1, 1),
    _Cie1000IpConfigRoutesIpv6NetworkAddress_Type()
)
cie1000IpConfigRoutesIpv6NetworkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6NetworkAddress.setStatus("current")


class _Cie1000IpConfigRoutesIpv6NetworkPrefixSize_Type(Integer32):
    """Custom type cie1000IpConfigRoutesIpv6NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cie1000IpConfigRoutesIpv6NetworkPrefixSize_Type.__name__ = "Integer32"
_Cie1000IpConfigRoutesIpv6NetworkPrefixSize_Object = MibTableColumn
cie1000IpConfigRoutesIpv6NetworkPrefixSize = _Cie1000IpConfigRoutesIpv6NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3, 1, 2),
    _Cie1000IpConfigRoutesIpv6NetworkPrefixSize_Type()
)
cie1000IpConfigRoutesIpv6NetworkPrefixSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6NetworkPrefixSize.setStatus("current")
_Cie1000IpConfigRoutesIpv6NextHop_Type = InetAddressIPv6
_Cie1000IpConfigRoutesIpv6NextHop_Object = MibTableColumn
cie1000IpConfigRoutesIpv6NextHop = _Cie1000IpConfigRoutesIpv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3, 1, 3),
    _Cie1000IpConfigRoutesIpv6NextHop_Type()
)
cie1000IpConfigRoutesIpv6NextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6NextHop.setStatus("current")
_Cie1000IpConfigRoutesIpv6NextHopInterface_Type = CIE1000InterfaceIndex
_Cie1000IpConfigRoutesIpv6NextHopInterface_Object = MibTableColumn
cie1000IpConfigRoutesIpv6NextHopInterface = _Cie1000IpConfigRoutesIpv6NextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3, 1, 4),
    _Cie1000IpConfigRoutesIpv6NextHopInterface_Type()
)
cie1000IpConfigRoutesIpv6NextHopInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6NextHopInterface.setStatus("current")
_Cie1000IpConfigRoutesIpv6Action_Type = CIE1000RowEditorState
_Cie1000IpConfigRoutesIpv6Action_Object = MibTableColumn
cie1000IpConfigRoutesIpv6Action = _Cie1000IpConfigRoutesIpv6Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 3, 1, 100),
    _Cie1000IpConfigRoutesIpv6Action_Type()
)
cie1000IpConfigRoutesIpv6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6Action.setStatus("current")
_Cie1000IpConfigRoutesIpv6RowEditor_ObjectIdentity = ObjectIdentity
cie1000IpConfigRoutesIpv6RowEditor = _Cie1000IpConfigRoutesIpv6RowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 4)
)
_Cie1000IpConfigRoutesIpv6RowEditorNetworkAddress_Type = InetAddressIPv6
_Cie1000IpConfigRoutesIpv6RowEditorNetworkAddress_Object = MibScalar
cie1000IpConfigRoutesIpv6RowEditorNetworkAddress = _Cie1000IpConfigRoutesIpv6RowEditorNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 4, 1),
    _Cie1000IpConfigRoutesIpv6RowEditorNetworkAddress_Type()
)
cie1000IpConfigRoutesIpv6RowEditorNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6RowEditorNetworkAddress.setStatus("current")


class _Cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize_Type(Integer32):
    """Custom type cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize_Type.__name__ = "Integer32"
_Cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize_Object = MibScalar
cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize = _Cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 4, 2),
    _Cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize_Type()
)
cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize.setStatus("current")
_Cie1000IpConfigRoutesIpv6RowEditorNextHop_Type = InetAddressIPv6
_Cie1000IpConfigRoutesIpv6RowEditorNextHop_Object = MibScalar
cie1000IpConfigRoutesIpv6RowEditorNextHop = _Cie1000IpConfigRoutesIpv6RowEditorNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 4, 3),
    _Cie1000IpConfigRoutesIpv6RowEditorNextHop_Type()
)
cie1000IpConfigRoutesIpv6RowEditorNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6RowEditorNextHop.setStatus("current")
_Cie1000IpConfigRoutesIpv6RowEditorNextHopInterface_Type = CIE1000InterfaceIndex
_Cie1000IpConfigRoutesIpv6RowEditorNextHopInterface_Object = MibScalar
cie1000IpConfigRoutesIpv6RowEditorNextHopInterface = _Cie1000IpConfigRoutesIpv6RowEditorNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 4, 4),
    _Cie1000IpConfigRoutesIpv6RowEditorNextHopInterface_Type()
)
cie1000IpConfigRoutesIpv6RowEditorNextHopInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6RowEditorNextHopInterface.setStatus("current")
_Cie1000IpConfigRoutesIpv6RowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpConfigRoutesIpv6RowEditorAction_Object = MibScalar
cie1000IpConfigRoutesIpv6RowEditorAction = _Cie1000IpConfigRoutesIpv6RowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 2, 3, 4, 100),
    _Cie1000IpConfigRoutesIpv6RowEditorAction_Type()
)
cie1000IpConfigRoutesIpv6RowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6RowEditorAction.setStatus("current")
_Cie1000IpStatus_ObjectIdentity = ObjectIdentity
cie1000IpStatus = _Cie1000IpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3)
)
_Cie1000IpStatusGlobals_ObjectIdentity = ObjectIdentity
cie1000IpStatusGlobals = _Cie1000IpStatusGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1)
)
_Cie1000IpStatusGlobalsIpv4NeighbourTable_Object = MibTable
cie1000IpStatusGlobalsIpv4NeighbourTable = _Cie1000IpStatusGlobalsIpv4NeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv4NeighbourTable.setStatus("current")
_Cie1000IpStatusGlobalsIpv4NeighbourEntry_Object = MibTableRow
cie1000IpStatusGlobalsIpv4NeighbourEntry = _Cie1000IpStatusGlobalsIpv4NeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 1, 1)
)
cie1000IpStatusGlobalsIpv4NeighbourEntry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv4NeighbourIpv4"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv4NeighbourEntry.setStatus("current")
_Cie1000IpStatusGlobalsIpv4NeighbourIpv4_Type = IpAddress
_Cie1000IpStatusGlobalsIpv4NeighbourIpv4_Object = MibTableColumn
cie1000IpStatusGlobalsIpv4NeighbourIpv4 = _Cie1000IpStatusGlobalsIpv4NeighbourIpv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 1, 1, 1),
    _Cie1000IpStatusGlobalsIpv4NeighbourIpv4_Type()
)
cie1000IpStatusGlobalsIpv4NeighbourIpv4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv4NeighbourIpv4.setStatus("current")
_Cie1000IpStatusGlobalsIpv4NeighbourMacAddress_Type = MacAddress
_Cie1000IpStatusGlobalsIpv4NeighbourMacAddress_Object = MibTableColumn
cie1000IpStatusGlobalsIpv4NeighbourMacAddress = _Cie1000IpStatusGlobalsIpv4NeighbourMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 1, 1, 2),
    _Cie1000IpStatusGlobalsIpv4NeighbourMacAddress_Type()
)
cie1000IpStatusGlobalsIpv4NeighbourMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv4NeighbourMacAddress.setStatus("current")
_Cie1000IpStatusGlobalsIpv4NeighbourInterface_Type = CIE1000InterfaceIndex
_Cie1000IpStatusGlobalsIpv4NeighbourInterface_Object = MibTableColumn
cie1000IpStatusGlobalsIpv4NeighbourInterface = _Cie1000IpStatusGlobalsIpv4NeighbourInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 1, 1, 3),
    _Cie1000IpStatusGlobalsIpv4NeighbourInterface_Type()
)
cie1000IpStatusGlobalsIpv4NeighbourInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv4NeighbourInterface.setStatus("current")
_Cie1000IpStatusGlobalsIpv6NeighbourTable_Object = MibTable
cie1000IpStatusGlobalsIpv6NeighbourTable = _Cie1000IpStatusGlobalsIpv6NeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourTable.setStatus("current")
_Cie1000IpStatusGlobalsIpv6NeighbourEntry_Object = MibTableRow
cie1000IpStatusGlobalsIpv6NeighbourEntry = _Cie1000IpStatusGlobalsIpv6NeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 2, 1)
)
cie1000IpStatusGlobalsIpv6NeighbourEntry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourIpAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourEntry.setStatus("current")
_Cie1000IpStatusGlobalsIpv6NeighbourIpAddress_Type = InetAddressIPv6
_Cie1000IpStatusGlobalsIpv6NeighbourIpAddress_Object = MibTableColumn
cie1000IpStatusGlobalsIpv6NeighbourIpAddress = _Cie1000IpStatusGlobalsIpv6NeighbourIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 2, 1, 1),
    _Cie1000IpStatusGlobalsIpv6NeighbourIpAddress_Type()
)
cie1000IpStatusGlobalsIpv6NeighbourIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourIpAddress.setStatus("current")


class _Cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery_Type(Integer32):
    """Custom type cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery_Type.__name__ = "Integer32"
_Cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery_Object = MibTableColumn
cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery = _Cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 2, 1, 2),
    _Cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery_Type()
)
cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery.setStatus("current")
_Cie1000IpStatusGlobalsIpv6NeighbourMacAddress_Type = MacAddress
_Cie1000IpStatusGlobalsIpv6NeighbourMacAddress_Object = MibTableColumn
cie1000IpStatusGlobalsIpv6NeighbourMacAddress = _Cie1000IpStatusGlobalsIpv6NeighbourMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 2, 1, 3),
    _Cie1000IpStatusGlobalsIpv6NeighbourMacAddress_Type()
)
cie1000IpStatusGlobalsIpv6NeighbourMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourMacAddress.setStatus("current")
_Cie1000IpStatusGlobalsIpv6NeighbourInterface_Type = CIE1000InterfaceIndex
_Cie1000IpStatusGlobalsIpv6NeighbourInterface_Object = MibTableColumn
cie1000IpStatusGlobalsIpv6NeighbourInterface = _Cie1000IpStatusGlobalsIpv6NeighbourInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 1, 2, 1, 4),
    _Cie1000IpStatusGlobalsIpv6NeighbourInterface_Type()
)
cie1000IpStatusGlobalsIpv6NeighbourInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourInterface.setStatus("current")
_Cie1000IpStatusInterfaces_ObjectIdentity = ObjectIdentity
cie1000IpStatusInterfaces = _Cie1000IpStatusInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2)
)
_Cie1000IpStatusInterfacesLinkTable_Object = MibTable
cie1000IpStatusInterfacesLinkTable = _Cie1000IpStatusInterfacesLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkTable.setStatus("current")
_Cie1000IpStatusInterfacesLinkEntry_Object = MibTableRow
cie1000IpStatusInterfacesLinkEntry = _Cie1000IpStatusInterfacesLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1)
)
cie1000IpStatusInterfacesLinkEntry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkEntry.setStatus("current")
_Cie1000IpStatusInterfacesLinkIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatusInterfacesLinkIfIndex_Object = MibTableColumn
cie1000IpStatusInterfacesLinkIfIndex = _Cie1000IpStatusInterfacesLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 1),
    _Cie1000IpStatusInterfacesLinkIfIndex_Type()
)
cie1000IpStatusInterfacesLinkIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkIfIndex.setStatus("current")
_Cie1000IpStatusInterfacesLinkOsInterfaceIndex_Type = Unsigned32
_Cie1000IpStatusInterfacesLinkOsInterfaceIndex_Object = MibTableColumn
cie1000IpStatusInterfacesLinkOsInterfaceIndex = _Cie1000IpStatusInterfacesLinkOsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 2),
    _Cie1000IpStatusInterfacesLinkOsInterfaceIndex_Type()
)
cie1000IpStatusInterfacesLinkOsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkOsInterfaceIndex.setStatus("current")
_Cie1000IpStatusInterfacesLinkMtu_Type = Unsigned32
_Cie1000IpStatusInterfacesLinkMtu_Object = MibTableColumn
cie1000IpStatusInterfacesLinkMtu = _Cie1000IpStatusInterfacesLinkMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 3),
    _Cie1000IpStatusInterfacesLinkMtu_Type()
)
cie1000IpStatusInterfacesLinkMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkMtu.setStatus("current")
_Cie1000IpStatusInterfacesLinkMacAddress_Type = MacAddress
_Cie1000IpStatusInterfacesLinkMacAddress_Object = MibTableColumn
cie1000IpStatusInterfacesLinkMacAddress = _Cie1000IpStatusInterfacesLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 4),
    _Cie1000IpStatusInterfacesLinkMacAddress_Type()
)
cie1000IpStatusInterfacesLinkMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkMacAddress.setStatus("current")
_Cie1000IpStatusInterfacesLinkUp_Type = TruthValue
_Cie1000IpStatusInterfacesLinkUp_Object = MibTableColumn
cie1000IpStatusInterfacesLinkUp = _Cie1000IpStatusInterfacesLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 5),
    _Cie1000IpStatusInterfacesLinkUp_Type()
)
cie1000IpStatusInterfacesLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkUp.setStatus("current")
_Cie1000IpStatusInterfacesLinkBroadcast_Type = TruthValue
_Cie1000IpStatusInterfacesLinkBroadcast_Object = MibTableColumn
cie1000IpStatusInterfacesLinkBroadcast = _Cie1000IpStatusInterfacesLinkBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 6),
    _Cie1000IpStatusInterfacesLinkBroadcast_Type()
)
cie1000IpStatusInterfacesLinkBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkBroadcast.setStatus("current")
_Cie1000IpStatusInterfacesLinkLoopback_Type = TruthValue
_Cie1000IpStatusInterfacesLinkLoopback_Object = MibTableColumn
cie1000IpStatusInterfacesLinkLoopback = _Cie1000IpStatusInterfacesLinkLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 7),
    _Cie1000IpStatusInterfacesLinkLoopback_Type()
)
cie1000IpStatusInterfacesLinkLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkLoopback.setStatus("current")
_Cie1000IpStatusInterfacesLinkRunning_Type = TruthValue
_Cie1000IpStatusInterfacesLinkRunning_Object = MibTableColumn
cie1000IpStatusInterfacesLinkRunning = _Cie1000IpStatusInterfacesLinkRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 8),
    _Cie1000IpStatusInterfacesLinkRunning_Type()
)
cie1000IpStatusInterfacesLinkRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkRunning.setStatus("current")
_Cie1000IpStatusInterfacesLinkNoarp_Type = TruthValue
_Cie1000IpStatusInterfacesLinkNoarp_Object = MibTableColumn
cie1000IpStatusInterfacesLinkNoarp = _Cie1000IpStatusInterfacesLinkNoarp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 9),
    _Cie1000IpStatusInterfacesLinkNoarp_Type()
)
cie1000IpStatusInterfacesLinkNoarp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkNoarp.setStatus("current")
_Cie1000IpStatusInterfacesLinkPromisc_Type = TruthValue
_Cie1000IpStatusInterfacesLinkPromisc_Object = MibTableColumn
cie1000IpStatusInterfacesLinkPromisc = _Cie1000IpStatusInterfacesLinkPromisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 10),
    _Cie1000IpStatusInterfacesLinkPromisc_Type()
)
cie1000IpStatusInterfacesLinkPromisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkPromisc.setStatus("current")
_Cie1000IpStatusInterfacesLinkMulticast_Type = TruthValue
_Cie1000IpStatusInterfacesLinkMulticast_Object = MibTableColumn
cie1000IpStatusInterfacesLinkMulticast = _Cie1000IpStatusInterfacesLinkMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 1, 1, 11),
    _Cie1000IpStatusInterfacesLinkMulticast_Type()
)
cie1000IpStatusInterfacesLinkMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkMulticast.setStatus("current")
_Cie1000IpStatusInterfacesIpv4Table_Object = MibTable
cie1000IpStatusInterfacesIpv4Table = _Cie1000IpStatusInterfacesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4Table.setStatus("current")
_Cie1000IpStatusInterfacesIpv4Entry_Object = MibTableRow
cie1000IpStatusInterfacesIpv4Entry = _Cie1000IpStatusInterfacesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 2, 1)
)
cie1000IpStatusInterfacesIpv4Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4IfIndex"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4NetworkAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4NetworkMaskLength"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4Entry.setStatus("current")
_Cie1000IpStatusInterfacesIpv4IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatusInterfacesIpv4IfIndex_Object = MibTableColumn
cie1000IpStatusInterfacesIpv4IfIndex = _Cie1000IpStatusInterfacesIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 2, 1, 1),
    _Cie1000IpStatusInterfacesIpv4IfIndex_Type()
)
cie1000IpStatusInterfacesIpv4IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4IfIndex.setStatus("current")
_Cie1000IpStatusInterfacesIpv4NetworkAddress_Type = IpAddress
_Cie1000IpStatusInterfacesIpv4NetworkAddress_Object = MibTableColumn
cie1000IpStatusInterfacesIpv4NetworkAddress = _Cie1000IpStatusInterfacesIpv4NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 2, 1, 2),
    _Cie1000IpStatusInterfacesIpv4NetworkAddress_Type()
)
cie1000IpStatusInterfacesIpv4NetworkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4NetworkAddress.setStatus("current")


class _Cie1000IpStatusInterfacesIpv4NetworkMaskLength_Type(Integer32):
    """Custom type cie1000IpStatusInterfacesIpv4NetworkMaskLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Cie1000IpStatusInterfacesIpv4NetworkMaskLength_Type.__name__ = "Integer32"
_Cie1000IpStatusInterfacesIpv4NetworkMaskLength_Object = MibTableColumn
cie1000IpStatusInterfacesIpv4NetworkMaskLength = _Cie1000IpStatusInterfacesIpv4NetworkMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 2, 1, 3),
    _Cie1000IpStatusInterfacesIpv4NetworkMaskLength_Type()
)
cie1000IpStatusInterfacesIpv4NetworkMaskLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4NetworkMaskLength.setStatus("current")
_Cie1000IpStatusInterfacesIpv4Broadcast_Type = IpAddress
_Cie1000IpStatusInterfacesIpv4Broadcast_Object = MibTableColumn
cie1000IpStatusInterfacesIpv4Broadcast = _Cie1000IpStatusInterfacesIpv4Broadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 2, 1, 4),
    _Cie1000IpStatusInterfacesIpv4Broadcast_Type()
)
cie1000IpStatusInterfacesIpv4Broadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4Broadcast.setStatus("current")
_Cie1000IpStatusInterfacesDhcpClientV4Table_Object = MibTable
cie1000IpStatusInterfacesDhcpClientV4Table = _Cie1000IpStatusInterfacesDhcpClientV4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesDhcpClientV4Table.setStatus("current")
_Cie1000IpStatusInterfacesDhcpClientV4Entry_Object = MibTableRow
cie1000IpStatusInterfacesDhcpClientV4Entry = _Cie1000IpStatusInterfacesDhcpClientV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 3, 1)
)
cie1000IpStatusInterfacesDhcpClientV4Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesDhcpClientV4IfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesDhcpClientV4Entry.setStatus("current")
_Cie1000IpStatusInterfacesDhcpClientV4IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatusInterfacesDhcpClientV4IfIndex_Object = MibTableColumn
cie1000IpStatusInterfacesDhcpClientV4IfIndex = _Cie1000IpStatusInterfacesDhcpClientV4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 3, 1, 1),
    _Cie1000IpStatusInterfacesDhcpClientV4IfIndex_Type()
)
cie1000IpStatusInterfacesDhcpClientV4IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesDhcpClientV4IfIndex.setStatus("current")
_Cie1000IpStatusInterfacesDhcpClientV4State_Type = CIE1000IpDhcpClientState
_Cie1000IpStatusInterfacesDhcpClientV4State_Object = MibTableColumn
cie1000IpStatusInterfacesDhcpClientV4State = _Cie1000IpStatusInterfacesDhcpClientV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 3, 1, 2),
    _Cie1000IpStatusInterfacesDhcpClientV4State_Type()
)
cie1000IpStatusInterfacesDhcpClientV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesDhcpClientV4State.setStatus("current")
_Cie1000IpStatusInterfacesDhcpClientV4ServerIp_Type = IpAddress
_Cie1000IpStatusInterfacesDhcpClientV4ServerIp_Object = MibTableColumn
cie1000IpStatusInterfacesDhcpClientV4ServerIp = _Cie1000IpStatusInterfacesDhcpClientV4ServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 3, 1, 3),
    _Cie1000IpStatusInterfacesDhcpClientV4ServerIp_Type()
)
cie1000IpStatusInterfacesDhcpClientV4ServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesDhcpClientV4ServerIp.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Table_Object = MibTable
cie1000IpStatusInterfacesIpv6Table = _Cie1000IpStatusInterfacesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Table.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Entry_Object = MibTableRow
cie1000IpStatusInterfacesIpv6Entry = _Cie1000IpStatusInterfacesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1)
)
cie1000IpStatusInterfacesIpv6Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6IfIndex"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6NetworkAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6NetworkMaskLength"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Entry.setStatus("current")
_Cie1000IpStatusInterfacesIpv6IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatusInterfacesIpv6IfIndex_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6IfIndex = _Cie1000IpStatusInterfacesIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 1),
    _Cie1000IpStatusInterfacesIpv6IfIndex_Type()
)
cie1000IpStatusInterfacesIpv6IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6IfIndex.setStatus("current")
_Cie1000IpStatusInterfacesIpv6NetworkAddress_Type = InetAddressIPv6
_Cie1000IpStatusInterfacesIpv6NetworkAddress_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6NetworkAddress = _Cie1000IpStatusInterfacesIpv6NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 2),
    _Cie1000IpStatusInterfacesIpv6NetworkAddress_Type()
)
cie1000IpStatusInterfacesIpv6NetworkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6NetworkAddress.setStatus("current")


class _Cie1000IpStatusInterfacesIpv6NetworkMaskLength_Type(Integer32):
    """Custom type cie1000IpStatusInterfacesIpv6NetworkMaskLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cie1000IpStatusInterfacesIpv6NetworkMaskLength_Type.__name__ = "Integer32"
_Cie1000IpStatusInterfacesIpv6NetworkMaskLength_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6NetworkMaskLength = _Cie1000IpStatusInterfacesIpv6NetworkMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 3),
    _Cie1000IpStatusInterfacesIpv6NetworkMaskLength_Type()
)
cie1000IpStatusInterfacesIpv6NetworkMaskLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6NetworkMaskLength.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Tentative_Type = TruthValue
_Cie1000IpStatusInterfacesIpv6Tentative_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6Tentative = _Cie1000IpStatusInterfacesIpv6Tentative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 4),
    _Cie1000IpStatusInterfacesIpv6Tentative_Type()
)
cie1000IpStatusInterfacesIpv6Tentative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Tentative.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Duplicated_Type = TruthValue
_Cie1000IpStatusInterfacesIpv6Duplicated_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6Duplicated = _Cie1000IpStatusInterfacesIpv6Duplicated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 5),
    _Cie1000IpStatusInterfacesIpv6Duplicated_Type()
)
cie1000IpStatusInterfacesIpv6Duplicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Duplicated.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Detached_Type = TruthValue
_Cie1000IpStatusInterfacesIpv6Detached_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6Detached = _Cie1000IpStatusInterfacesIpv6Detached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 6),
    _Cie1000IpStatusInterfacesIpv6Detached_Type()
)
cie1000IpStatusInterfacesIpv6Detached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Detached.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Nodad_Type = TruthValue
_Cie1000IpStatusInterfacesIpv6Nodad_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6Nodad = _Cie1000IpStatusInterfacesIpv6Nodad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 7),
    _Cie1000IpStatusInterfacesIpv6Nodad_Type()
)
cie1000IpStatusInterfacesIpv6Nodad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Nodad.setStatus("current")
_Cie1000IpStatusInterfacesIpv6Autoconf_Type = TruthValue
_Cie1000IpStatusInterfacesIpv6Autoconf_Object = MibTableColumn
cie1000IpStatusInterfacesIpv6Autoconf = _Cie1000IpStatusInterfacesIpv6Autoconf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 2, 4, 1, 8),
    _Cie1000IpStatusInterfacesIpv6Autoconf_Type()
)
cie1000IpStatusInterfacesIpv6Autoconf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6Autoconf.setStatus("current")
_Cie1000IpStatusRoutes_ObjectIdentity = ObjectIdentity
cie1000IpStatusRoutes = _Cie1000IpStatusRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3)
)
_Cie1000IpStatusRoutesIpv4Table_Object = MibTable
cie1000IpStatusRoutesIpv4Table = _Cie1000IpStatusRoutesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4Table.setStatus("current")
_Cie1000IpStatusRoutesIpv4Entry_Object = MibTableRow
cie1000IpStatusRoutesIpv4Entry = _Cie1000IpStatusRoutesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1)
)
cie1000IpStatusRoutesIpv4Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4NetworkAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4NetworkPrefixSize"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4NextHop"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4Entry.setStatus("current")
_Cie1000IpStatusRoutesIpv4NetworkAddress_Type = IpAddress
_Cie1000IpStatusRoutesIpv4NetworkAddress_Object = MibTableColumn
cie1000IpStatusRoutesIpv4NetworkAddress = _Cie1000IpStatusRoutesIpv4NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 1),
    _Cie1000IpStatusRoutesIpv4NetworkAddress_Type()
)
cie1000IpStatusRoutesIpv4NetworkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4NetworkAddress.setStatus("current")


class _Cie1000IpStatusRoutesIpv4NetworkPrefixSize_Type(Integer32):
    """Custom type cie1000IpStatusRoutesIpv4NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Cie1000IpStatusRoutesIpv4NetworkPrefixSize_Type.__name__ = "Integer32"
_Cie1000IpStatusRoutesIpv4NetworkPrefixSize_Object = MibTableColumn
cie1000IpStatusRoutesIpv4NetworkPrefixSize = _Cie1000IpStatusRoutesIpv4NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 2),
    _Cie1000IpStatusRoutesIpv4NetworkPrefixSize_Type()
)
cie1000IpStatusRoutesIpv4NetworkPrefixSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4NetworkPrefixSize.setStatus("current")
_Cie1000IpStatusRoutesIpv4NextHop_Type = IpAddress
_Cie1000IpStatusRoutesIpv4NextHop_Object = MibTableColumn
cie1000IpStatusRoutesIpv4NextHop = _Cie1000IpStatusRoutesIpv4NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 3),
    _Cie1000IpStatusRoutesIpv4NextHop_Type()
)
cie1000IpStatusRoutesIpv4NextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4NextHop.setStatus("current")
_Cie1000IpStatusRoutesIpv4DerivedNextHopInterface_Type = CIE1000InterfaceIndex
_Cie1000IpStatusRoutesIpv4DerivedNextHopInterface_Object = MibTableColumn
cie1000IpStatusRoutesIpv4DerivedNextHopInterface = _Cie1000IpStatusRoutesIpv4DerivedNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 4),
    _Cie1000IpStatusRoutesIpv4DerivedNextHopInterface_Type()
)
cie1000IpStatusRoutesIpv4DerivedNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4DerivedNextHopInterface.setStatus("current")
_Cie1000IpStatusRoutesIpv4FlagUp_Type = TruthValue
_Cie1000IpStatusRoutesIpv4FlagUp_Object = MibTableColumn
cie1000IpStatusRoutesIpv4FlagUp = _Cie1000IpStatusRoutesIpv4FlagUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 35),
    _Cie1000IpStatusRoutesIpv4FlagUp_Type()
)
cie1000IpStatusRoutesIpv4FlagUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4FlagUp.setStatus("current")
_Cie1000IpStatusRoutesIpv4FlagHost_Type = TruthValue
_Cie1000IpStatusRoutesIpv4FlagHost_Object = MibTableColumn
cie1000IpStatusRoutesIpv4FlagHost = _Cie1000IpStatusRoutesIpv4FlagHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 36),
    _Cie1000IpStatusRoutesIpv4FlagHost_Type()
)
cie1000IpStatusRoutesIpv4FlagHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4FlagHost.setStatus("current")
_Cie1000IpStatusRoutesIpv4FlagGateway_Type = TruthValue
_Cie1000IpStatusRoutesIpv4FlagGateway_Object = MibTableColumn
cie1000IpStatusRoutesIpv4FlagGateway = _Cie1000IpStatusRoutesIpv4FlagGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 37),
    _Cie1000IpStatusRoutesIpv4FlagGateway_Type()
)
cie1000IpStatusRoutesIpv4FlagGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4FlagGateway.setStatus("current")
_Cie1000IpStatusRoutesIpv4OwnerConf_Type = TruthValue
_Cie1000IpStatusRoutesIpv4OwnerConf_Object = MibTableColumn
cie1000IpStatusRoutesIpv4OwnerConf = _Cie1000IpStatusRoutesIpv4OwnerConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 67),
    _Cie1000IpStatusRoutesIpv4OwnerConf_Type()
)
cie1000IpStatusRoutesIpv4OwnerConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4OwnerConf.setStatus("current")
_Cie1000IpStatusRoutesIpv4OwnerDhcp_Type = TruthValue
_Cie1000IpStatusRoutesIpv4OwnerDhcp_Object = MibTableColumn
cie1000IpStatusRoutesIpv4OwnerDhcp = _Cie1000IpStatusRoutesIpv4OwnerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 68),
    _Cie1000IpStatusRoutesIpv4OwnerDhcp_Type()
)
cie1000IpStatusRoutesIpv4OwnerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4OwnerDhcp.setStatus("current")
_Cie1000IpStatusRoutesIpv4OwnerDynamic_Type = TruthValue
_Cie1000IpStatusRoutesIpv4OwnerDynamic_Object = MibTableColumn
cie1000IpStatusRoutesIpv4OwnerDynamic = _Cie1000IpStatusRoutesIpv4OwnerDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 1, 1, 69),
    _Cie1000IpStatusRoutesIpv4OwnerDynamic_Type()
)
cie1000IpStatusRoutesIpv4OwnerDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4OwnerDynamic.setStatus("current")
_Cie1000IpStatusRoutesIpv6Table_Object = MibTable
cie1000IpStatusRoutesIpv6Table = _Cie1000IpStatusRoutesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6Table.setStatus("current")
_Cie1000IpStatusRoutesIpv6Entry_Object = MibTableRow
cie1000IpStatusRoutesIpv6Entry = _Cie1000IpStatusRoutesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1)
)
cie1000IpStatusRoutesIpv6Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NetworkAddress"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NetworkPrefixSize"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NextHop"),
    (0, "CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NextHopInterface"),
)
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6Entry.setStatus("current")
_Cie1000IpStatusRoutesIpv6NetworkAddress_Type = InetAddressIPv6
_Cie1000IpStatusRoutesIpv6NetworkAddress_Object = MibTableColumn
cie1000IpStatusRoutesIpv6NetworkAddress = _Cie1000IpStatusRoutesIpv6NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 1),
    _Cie1000IpStatusRoutesIpv6NetworkAddress_Type()
)
cie1000IpStatusRoutesIpv6NetworkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6NetworkAddress.setStatus("current")


class _Cie1000IpStatusRoutesIpv6NetworkPrefixSize_Type(Integer32):
    """Custom type cie1000IpStatusRoutesIpv6NetworkPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cie1000IpStatusRoutesIpv6NetworkPrefixSize_Type.__name__ = "Integer32"
_Cie1000IpStatusRoutesIpv6NetworkPrefixSize_Object = MibTableColumn
cie1000IpStatusRoutesIpv6NetworkPrefixSize = _Cie1000IpStatusRoutesIpv6NetworkPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 2),
    _Cie1000IpStatusRoutesIpv6NetworkPrefixSize_Type()
)
cie1000IpStatusRoutesIpv6NetworkPrefixSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6NetworkPrefixSize.setStatus("current")
_Cie1000IpStatusRoutesIpv6NextHop_Type = InetAddressIPv6
_Cie1000IpStatusRoutesIpv6NextHop_Object = MibTableColumn
cie1000IpStatusRoutesIpv6NextHop = _Cie1000IpStatusRoutesIpv6NextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 3),
    _Cie1000IpStatusRoutesIpv6NextHop_Type()
)
cie1000IpStatusRoutesIpv6NextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6NextHop.setStatus("current")
_Cie1000IpStatusRoutesIpv6NextHopInterface_Type = CIE1000InterfaceIndex
_Cie1000IpStatusRoutesIpv6NextHopInterface_Object = MibTableColumn
cie1000IpStatusRoutesIpv6NextHopInterface = _Cie1000IpStatusRoutesIpv6NextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 4),
    _Cie1000IpStatusRoutesIpv6NextHopInterface_Type()
)
cie1000IpStatusRoutesIpv6NextHopInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6NextHopInterface.setStatus("current")
_Cie1000IpStatusRoutesIpv6DerivedNextHopInterface_Type = CIE1000InterfaceIndex
_Cie1000IpStatusRoutesIpv6DerivedNextHopInterface_Object = MibTableColumn
cie1000IpStatusRoutesIpv6DerivedNextHopInterface = _Cie1000IpStatusRoutesIpv6DerivedNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 5),
    _Cie1000IpStatusRoutesIpv6DerivedNextHopInterface_Type()
)
cie1000IpStatusRoutesIpv6DerivedNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6DerivedNextHopInterface.setStatus("current")
_Cie1000IpStatusRoutesIpv6FlagUp_Type = TruthValue
_Cie1000IpStatusRoutesIpv6FlagUp_Object = MibTableColumn
cie1000IpStatusRoutesIpv6FlagUp = _Cie1000IpStatusRoutesIpv6FlagUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 36),
    _Cie1000IpStatusRoutesIpv6FlagUp_Type()
)
cie1000IpStatusRoutesIpv6FlagUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6FlagUp.setStatus("current")
_Cie1000IpStatusRoutesIpv6FlagHost_Type = TruthValue
_Cie1000IpStatusRoutesIpv6FlagHost_Object = MibTableColumn
cie1000IpStatusRoutesIpv6FlagHost = _Cie1000IpStatusRoutesIpv6FlagHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 37),
    _Cie1000IpStatusRoutesIpv6FlagHost_Type()
)
cie1000IpStatusRoutesIpv6FlagHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6FlagHost.setStatus("current")
_Cie1000IpStatusRoutesIpv6FlagGateway_Type = TruthValue
_Cie1000IpStatusRoutesIpv6FlagGateway_Object = MibTableColumn
cie1000IpStatusRoutesIpv6FlagGateway = _Cie1000IpStatusRoutesIpv6FlagGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 38),
    _Cie1000IpStatusRoutesIpv6FlagGateway_Type()
)
cie1000IpStatusRoutesIpv6FlagGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6FlagGateway.setStatus("current")
_Cie1000IpStatusRoutesIpv6OwnerConf_Type = TruthValue
_Cie1000IpStatusRoutesIpv6OwnerConf_Object = MibTableColumn
cie1000IpStatusRoutesIpv6OwnerConf = _Cie1000IpStatusRoutesIpv6OwnerConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 68),
    _Cie1000IpStatusRoutesIpv6OwnerConf_Type()
)
cie1000IpStatusRoutesIpv6OwnerConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6OwnerConf.setStatus("current")
_Cie1000IpStatusRoutesIpv6OwnerDhcp_Type = TruthValue
_Cie1000IpStatusRoutesIpv6OwnerDhcp_Object = MibTableColumn
cie1000IpStatusRoutesIpv6OwnerDhcp = _Cie1000IpStatusRoutesIpv6OwnerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 69),
    _Cie1000IpStatusRoutesIpv6OwnerDhcp_Type()
)
cie1000IpStatusRoutesIpv6OwnerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6OwnerDhcp.setStatus("current")
_Cie1000IpStatusRoutesIpv6OwnerDynamic_Type = TruthValue
_Cie1000IpStatusRoutesIpv6OwnerDynamic_Object = MibTableColumn
cie1000IpStatusRoutesIpv6OwnerDynamic = _Cie1000IpStatusRoutesIpv6OwnerDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 3, 3, 2, 1, 70),
    _Cie1000IpStatusRoutesIpv6OwnerDynamic_Type()
)
cie1000IpStatusRoutesIpv6OwnerDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6OwnerDynamic.setStatus("current")
_Cie1000IpControl_ObjectIdentity = ObjectIdentity
cie1000IpControl = _Cie1000IpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4)
)
_Cie1000IpControlGlobals_ObjectIdentity = ObjectIdentity
cie1000IpControlGlobals = _Cie1000IpControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 1)
)
_Cie1000IpControlGlobalsIpv4NeighbourTableClear_Type = TruthValue
_Cie1000IpControlGlobalsIpv4NeighbourTableClear_Object = MibScalar
cie1000IpControlGlobalsIpv4NeighbourTableClear = _Cie1000IpControlGlobalsIpv4NeighbourTableClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 1, 1),
    _Cie1000IpControlGlobalsIpv4NeighbourTableClear_Type()
)
cie1000IpControlGlobalsIpv4NeighbourTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpControlGlobalsIpv4NeighbourTableClear.setStatus("current")
_Cie1000IpControlGlobalsIpv6NeighbourTableClear_Type = TruthValue
_Cie1000IpControlGlobalsIpv6NeighbourTableClear_Object = MibScalar
cie1000IpControlGlobalsIpv6NeighbourTableClear = _Cie1000IpControlGlobalsIpv6NeighbourTableClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 1, 2),
    _Cie1000IpControlGlobalsIpv6NeighbourTableClear_Type()
)
cie1000IpControlGlobalsIpv6NeighbourTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpControlGlobalsIpv6NeighbourTableClear.setStatus("current")
_Cie1000IpControlGlobalsIpv4SystemStatisticsClear_Type = CIE1000Unsigned8
_Cie1000IpControlGlobalsIpv4SystemStatisticsClear_Object = MibScalar
cie1000IpControlGlobalsIpv4SystemStatisticsClear = _Cie1000IpControlGlobalsIpv4SystemStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 1, 3),
    _Cie1000IpControlGlobalsIpv4SystemStatisticsClear_Type()
)
cie1000IpControlGlobalsIpv4SystemStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpControlGlobalsIpv4SystemStatisticsClear.setStatus("current")
_Cie1000IpControlGlobalsIpv6SystemStatisticsClear_Type = CIE1000Unsigned8
_Cie1000IpControlGlobalsIpv6SystemStatisticsClear_Object = MibScalar
cie1000IpControlGlobalsIpv6SystemStatisticsClear = _Cie1000IpControlGlobalsIpv6SystemStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 1, 4),
    _Cie1000IpControlGlobalsIpv6SystemStatisticsClear_Type()
)
cie1000IpControlGlobalsIpv6SystemStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpControlGlobalsIpv6SystemStatisticsClear.setStatus("current")
_Cie1000IpControlInterface_ObjectIdentity = ObjectIdentity
cie1000IpControlInterface = _Cie1000IpControlInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 2)
)
_Cie1000IpControlInterfaceDhcpClientTable_Object = MibTable
cie1000IpControlInterfaceDhcpClientTable = _Cie1000IpControlInterfaceDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000IpControlInterfaceDhcpClientTable.setStatus("current")
_Cie1000IpControlInterfaceDhcpClientEntry_Object = MibTableRow
cie1000IpControlInterfaceDhcpClientEntry = _Cie1000IpControlInterfaceDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 2, 1, 1)
)
cie1000IpControlInterfaceDhcpClientEntry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpControlInterfaceDhcpClientIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpControlInterfaceDhcpClientEntry.setStatus("current")
_Cie1000IpControlInterfaceDhcpClientIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpControlInterfaceDhcpClientIfIndex_Object = MibTableColumn
cie1000IpControlInterfaceDhcpClientIfIndex = _Cie1000IpControlInterfaceDhcpClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 2, 1, 1, 1),
    _Cie1000IpControlInterfaceDhcpClientIfIndex_Type()
)
cie1000IpControlInterfaceDhcpClientIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpControlInterfaceDhcpClientIfIndex.setStatus("current")
_Cie1000IpControlInterfaceDhcpClientRestart_Type = TruthValue
_Cie1000IpControlInterfaceDhcpClientRestart_Object = MibTableColumn
cie1000IpControlInterfaceDhcpClientRestart = _Cie1000IpControlInterfaceDhcpClientRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 4, 2, 1, 1, 2),
    _Cie1000IpControlInterfaceDhcpClientRestart_Type()
)
cie1000IpControlInterfaceDhcpClientRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpControlInterfaceDhcpClientRestart.setStatus("current")
_Cie1000IpStatistics_ObjectIdentity = ObjectIdentity
cie1000IpStatistics = _Cie1000IpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5)
)
_Cie1000IpStatisticsGlobals_ObjectIdentity = ObjectIdentity
cie1000IpStatisticsGlobals = _Cie1000IpStatisticsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1)
)
_Cie1000IpStatisticsGlobalsIpv4_ObjectIdentity = ObjectIdentity
cie1000IpStatisticsGlobalsIpv4 = _Cie1000IpStatisticsGlobalsIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1)
)
_Cie1000IpStatisticsGlobalsIpv4InReceives_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InReceives_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InReceives = _Cie1000IpStatisticsGlobalsIpv4InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 1),
    _Cie1000IpStatisticsGlobalsIpv4InReceives_Type()
)
cie1000IpStatisticsGlobalsIpv4InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InReceives.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInReceives_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInReceives_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInReceives = _Cie1000IpStatisticsGlobalsIpv4HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 2),
    _Cie1000IpStatisticsGlobalsIpv4HCInReceives_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInReceives.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InOctets = _Cie1000IpStatisticsGlobalsIpv4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 3),
    _Cie1000IpStatisticsGlobalsIpv4InOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInOctets = _Cie1000IpStatisticsGlobalsIpv4HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 4),
    _Cie1000IpStatisticsGlobalsIpv4HCInOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InHdrErrors_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InHdrErrors_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InHdrErrors = _Cie1000IpStatisticsGlobalsIpv4InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 5),
    _Cie1000IpStatisticsGlobalsIpv4InHdrErrors_Type()
)
cie1000IpStatisticsGlobalsIpv4InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InHdrErrors.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InNoRoutes_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InNoRoutes = _Cie1000IpStatisticsGlobalsIpv4InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 6),
    _Cie1000IpStatisticsGlobalsIpv4InNoRoutes_Type()
)
cie1000IpStatisticsGlobalsIpv4InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InNoRoutes.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InAddrErrors_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InAddrErrors_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InAddrErrors = _Cie1000IpStatisticsGlobalsIpv4InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 7),
    _Cie1000IpStatisticsGlobalsIpv4InAddrErrors_Type()
)
cie1000IpStatisticsGlobalsIpv4InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InAddrErrors.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InUnknownProtos_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InUnknownProtos_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InUnknownProtos = _Cie1000IpStatisticsGlobalsIpv4InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 8),
    _Cie1000IpStatisticsGlobalsIpv4InUnknownProtos_Type()
)
cie1000IpStatisticsGlobalsIpv4InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InUnknownProtos.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InTruncatedPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InTruncatedPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InTruncatedPkts = _Cie1000IpStatisticsGlobalsIpv4InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 9),
    _Cie1000IpStatisticsGlobalsIpv4InTruncatedPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InTruncatedPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InForwDatagrams = _Cie1000IpStatisticsGlobalsIpv4InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 10),
    _Cie1000IpStatisticsGlobalsIpv4InForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv4InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams = _Cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 11),
    _Cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4ReasmReqds_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4ReasmReqds_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4ReasmReqds = _Cie1000IpStatisticsGlobalsIpv4ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 12),
    _Cie1000IpStatisticsGlobalsIpv4ReasmReqds_Type()
)
cie1000IpStatisticsGlobalsIpv4ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4ReasmReqds.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4ReasmOKs_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4ReasmOKs_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4ReasmOKs = _Cie1000IpStatisticsGlobalsIpv4ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 13),
    _Cie1000IpStatisticsGlobalsIpv4ReasmOKs_Type()
)
cie1000IpStatisticsGlobalsIpv4ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4ReasmOKs.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4ReasmFails_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4ReasmFails_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4ReasmFails = _Cie1000IpStatisticsGlobalsIpv4ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 14),
    _Cie1000IpStatisticsGlobalsIpv4ReasmFails_Type()
)
cie1000IpStatisticsGlobalsIpv4ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4ReasmFails.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InDiscards_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InDiscards_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InDiscards = _Cie1000IpStatisticsGlobalsIpv4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 15),
    _Cie1000IpStatisticsGlobalsIpv4InDiscards_Type()
)
cie1000IpStatisticsGlobalsIpv4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InDiscards.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InDelivers_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InDelivers_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InDelivers = _Cie1000IpStatisticsGlobalsIpv4InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 16),
    _Cie1000IpStatisticsGlobalsIpv4InDelivers_Type()
)
cie1000IpStatisticsGlobalsIpv4InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InDelivers.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInDelivers_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInDelivers_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInDelivers = _Cie1000IpStatisticsGlobalsIpv4HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 17),
    _Cie1000IpStatisticsGlobalsIpv4HCInDelivers_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInDelivers.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutRequests_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutRequests_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutRequests = _Cie1000IpStatisticsGlobalsIpv4OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 18),
    _Cie1000IpStatisticsGlobalsIpv4OutRequests_Type()
)
cie1000IpStatisticsGlobalsIpv4OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutRequests.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutRequests_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutRequests_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutRequests = _Cie1000IpStatisticsGlobalsIpv4HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 19),
    _Cie1000IpStatisticsGlobalsIpv4HCOutRequests_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutRequests.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutNoRoutes_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutNoRoutes = _Cie1000IpStatisticsGlobalsIpv4OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 20),
    _Cie1000IpStatisticsGlobalsIpv4OutNoRoutes_Type()
)
cie1000IpStatisticsGlobalsIpv4OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutNoRoutes.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutForwDatagrams = _Cie1000IpStatisticsGlobalsIpv4OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 21),
    _Cie1000IpStatisticsGlobalsIpv4OutForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv4OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams = _Cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 22),
    _Cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutDiscards_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutDiscards_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutDiscards = _Cie1000IpStatisticsGlobalsIpv4OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 23),
    _Cie1000IpStatisticsGlobalsIpv4OutDiscards_Type()
)
cie1000IpStatisticsGlobalsIpv4OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutDiscards.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutFragReqds_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutFragReqds_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutFragReqds = _Cie1000IpStatisticsGlobalsIpv4OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 24),
    _Cie1000IpStatisticsGlobalsIpv4OutFragReqds_Type()
)
cie1000IpStatisticsGlobalsIpv4OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutFragReqds.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutFragOKs_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutFragOKs_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutFragOKs = _Cie1000IpStatisticsGlobalsIpv4OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 25),
    _Cie1000IpStatisticsGlobalsIpv4OutFragOKs_Type()
)
cie1000IpStatisticsGlobalsIpv4OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutFragOKs.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutFragFails_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutFragFails_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutFragFails = _Cie1000IpStatisticsGlobalsIpv4OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 26),
    _Cie1000IpStatisticsGlobalsIpv4OutFragFails_Type()
)
cie1000IpStatisticsGlobalsIpv4OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutFragFails.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutFragCreates_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutFragCreates_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutFragCreates = _Cie1000IpStatisticsGlobalsIpv4OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 27),
    _Cie1000IpStatisticsGlobalsIpv4OutFragCreates_Type()
)
cie1000IpStatisticsGlobalsIpv4OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutFragCreates.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutTransmits_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutTransmits_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutTransmits = _Cie1000IpStatisticsGlobalsIpv4OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 28),
    _Cie1000IpStatisticsGlobalsIpv4OutTransmits_Type()
)
cie1000IpStatisticsGlobalsIpv4OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutTransmits.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutTransmits_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutTransmits_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutTransmits = _Cie1000IpStatisticsGlobalsIpv4HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 29),
    _Cie1000IpStatisticsGlobalsIpv4HCOutTransmits_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutTransmits.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutOctets = _Cie1000IpStatisticsGlobalsIpv4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 30),
    _Cie1000IpStatisticsGlobalsIpv4OutOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutOctets = _Cie1000IpStatisticsGlobalsIpv4HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 31),
    _Cie1000IpStatisticsGlobalsIpv4HCOutOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InMcastPkts = _Cie1000IpStatisticsGlobalsIpv4InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 32),
    _Cie1000IpStatisticsGlobalsIpv4InMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInMcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInMcastPkts = _Cie1000IpStatisticsGlobalsIpv4HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 33),
    _Cie1000IpStatisticsGlobalsIpv4HCInMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InMcastOctets = _Cie1000IpStatisticsGlobalsIpv4InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 34),
    _Cie1000IpStatisticsGlobalsIpv4InMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInMcastOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInMcastOctets = _Cie1000IpStatisticsGlobalsIpv4HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 35),
    _Cie1000IpStatisticsGlobalsIpv4HCInMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutMcastPkts = _Cie1000IpStatisticsGlobalsIpv4OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 36),
    _Cie1000IpStatisticsGlobalsIpv4OutMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts = _Cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 37),
    _Cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutMcastOctets = _Cie1000IpStatisticsGlobalsIpv4OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 38),
    _Cie1000IpStatisticsGlobalsIpv4OutMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets = _Cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 39),
    _Cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4InBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4InBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4InBcastPkts = _Cie1000IpStatisticsGlobalsIpv4InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 40),
    _Cie1000IpStatisticsGlobalsIpv4InBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCInBcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCInBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCInBcastPkts = _Cie1000IpStatisticsGlobalsIpv4HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 41),
    _Cie1000IpStatisticsGlobalsIpv4HCInBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCInBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4OutBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4OutBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4OutBcastPkts = _Cie1000IpStatisticsGlobalsIpv4OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 42),
    _Cie1000IpStatisticsGlobalsIpv4OutBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4OutBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts = _Cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 43),
    _Cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4DiscontinuityTime_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv4DiscontinuityTime_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4DiscontinuityTime = _Cie1000IpStatisticsGlobalsIpv4DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 44),
    _Cie1000IpStatisticsGlobalsIpv4DiscontinuityTime_Type()
)
cie1000IpStatisticsGlobalsIpv4DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4DiscontinuityTime.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv4RefreshRate_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv4RefreshRate_Object = MibScalar
cie1000IpStatisticsGlobalsIpv4RefreshRate = _Cie1000IpStatisticsGlobalsIpv4RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 1, 45),
    _Cie1000IpStatisticsGlobalsIpv4RefreshRate_Type()
)
cie1000IpStatisticsGlobalsIpv4RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4RefreshRate.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6_ObjectIdentity = ObjectIdentity
cie1000IpStatisticsGlobalsIpv6 = _Cie1000IpStatisticsGlobalsIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2)
)
_Cie1000IpStatisticsGlobalsIpv6InReceives_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InReceives_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InReceives = _Cie1000IpStatisticsGlobalsIpv6InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 1),
    _Cie1000IpStatisticsGlobalsIpv6InReceives_Type()
)
cie1000IpStatisticsGlobalsIpv6InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InReceives.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInReceives_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInReceives_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInReceives = _Cie1000IpStatisticsGlobalsIpv6HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 2),
    _Cie1000IpStatisticsGlobalsIpv6HCInReceives_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInReceives.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InOctets = _Cie1000IpStatisticsGlobalsIpv6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 3),
    _Cie1000IpStatisticsGlobalsIpv6InOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInOctets = _Cie1000IpStatisticsGlobalsIpv6HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 4),
    _Cie1000IpStatisticsGlobalsIpv6HCInOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InHdrErrors_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InHdrErrors_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InHdrErrors = _Cie1000IpStatisticsGlobalsIpv6InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 5),
    _Cie1000IpStatisticsGlobalsIpv6InHdrErrors_Type()
)
cie1000IpStatisticsGlobalsIpv6InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InHdrErrors.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InNoRoutes_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InNoRoutes = _Cie1000IpStatisticsGlobalsIpv6InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 6),
    _Cie1000IpStatisticsGlobalsIpv6InNoRoutes_Type()
)
cie1000IpStatisticsGlobalsIpv6InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InNoRoutes.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InAddrErrors_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InAddrErrors_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InAddrErrors = _Cie1000IpStatisticsGlobalsIpv6InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 7),
    _Cie1000IpStatisticsGlobalsIpv6InAddrErrors_Type()
)
cie1000IpStatisticsGlobalsIpv6InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InAddrErrors.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InUnknownProtos_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InUnknownProtos_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InUnknownProtos = _Cie1000IpStatisticsGlobalsIpv6InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 8),
    _Cie1000IpStatisticsGlobalsIpv6InUnknownProtos_Type()
)
cie1000IpStatisticsGlobalsIpv6InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InUnknownProtos.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InTruncatedPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InTruncatedPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InTruncatedPkts = _Cie1000IpStatisticsGlobalsIpv6InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 9),
    _Cie1000IpStatisticsGlobalsIpv6InTruncatedPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InTruncatedPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InForwDatagrams = _Cie1000IpStatisticsGlobalsIpv6InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 10),
    _Cie1000IpStatisticsGlobalsIpv6InForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv6InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams = _Cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 11),
    _Cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6ReasmReqds_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6ReasmReqds_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6ReasmReqds = _Cie1000IpStatisticsGlobalsIpv6ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 12),
    _Cie1000IpStatisticsGlobalsIpv6ReasmReqds_Type()
)
cie1000IpStatisticsGlobalsIpv6ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6ReasmReqds.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6ReasmOKs_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6ReasmOKs_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6ReasmOKs = _Cie1000IpStatisticsGlobalsIpv6ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 13),
    _Cie1000IpStatisticsGlobalsIpv6ReasmOKs_Type()
)
cie1000IpStatisticsGlobalsIpv6ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6ReasmOKs.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6ReasmFails_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6ReasmFails_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6ReasmFails = _Cie1000IpStatisticsGlobalsIpv6ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 14),
    _Cie1000IpStatisticsGlobalsIpv6ReasmFails_Type()
)
cie1000IpStatisticsGlobalsIpv6ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6ReasmFails.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InDiscards_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InDiscards_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InDiscards = _Cie1000IpStatisticsGlobalsIpv6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 15),
    _Cie1000IpStatisticsGlobalsIpv6InDiscards_Type()
)
cie1000IpStatisticsGlobalsIpv6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InDiscards.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InDelivers_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InDelivers_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InDelivers = _Cie1000IpStatisticsGlobalsIpv6InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 16),
    _Cie1000IpStatisticsGlobalsIpv6InDelivers_Type()
)
cie1000IpStatisticsGlobalsIpv6InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InDelivers.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInDelivers_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInDelivers_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInDelivers = _Cie1000IpStatisticsGlobalsIpv6HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 17),
    _Cie1000IpStatisticsGlobalsIpv6HCInDelivers_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInDelivers.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutRequests_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutRequests_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutRequests = _Cie1000IpStatisticsGlobalsIpv6OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 18),
    _Cie1000IpStatisticsGlobalsIpv6OutRequests_Type()
)
cie1000IpStatisticsGlobalsIpv6OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutRequests.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutRequests_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutRequests_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutRequests = _Cie1000IpStatisticsGlobalsIpv6HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 19),
    _Cie1000IpStatisticsGlobalsIpv6HCOutRequests_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutRequests.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutNoRoutes_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutNoRoutes = _Cie1000IpStatisticsGlobalsIpv6OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 20),
    _Cie1000IpStatisticsGlobalsIpv6OutNoRoutes_Type()
)
cie1000IpStatisticsGlobalsIpv6OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutNoRoutes.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutForwDatagrams = _Cie1000IpStatisticsGlobalsIpv6OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 21),
    _Cie1000IpStatisticsGlobalsIpv6OutForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv6OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams = _Cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 22),
    _Cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutDiscards_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutDiscards_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutDiscards = _Cie1000IpStatisticsGlobalsIpv6OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 23),
    _Cie1000IpStatisticsGlobalsIpv6OutDiscards_Type()
)
cie1000IpStatisticsGlobalsIpv6OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutDiscards.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutFragReqds_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutFragReqds_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutFragReqds = _Cie1000IpStatisticsGlobalsIpv6OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 24),
    _Cie1000IpStatisticsGlobalsIpv6OutFragReqds_Type()
)
cie1000IpStatisticsGlobalsIpv6OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutFragReqds.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutFragOKs_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutFragOKs_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutFragOKs = _Cie1000IpStatisticsGlobalsIpv6OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 25),
    _Cie1000IpStatisticsGlobalsIpv6OutFragOKs_Type()
)
cie1000IpStatisticsGlobalsIpv6OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutFragOKs.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutFragFails_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutFragFails_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutFragFails = _Cie1000IpStatisticsGlobalsIpv6OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 26),
    _Cie1000IpStatisticsGlobalsIpv6OutFragFails_Type()
)
cie1000IpStatisticsGlobalsIpv6OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutFragFails.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutFragCreates_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutFragCreates_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutFragCreates = _Cie1000IpStatisticsGlobalsIpv6OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 27),
    _Cie1000IpStatisticsGlobalsIpv6OutFragCreates_Type()
)
cie1000IpStatisticsGlobalsIpv6OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutFragCreates.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutTransmits_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutTransmits_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutTransmits = _Cie1000IpStatisticsGlobalsIpv6OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 28),
    _Cie1000IpStatisticsGlobalsIpv6OutTransmits_Type()
)
cie1000IpStatisticsGlobalsIpv6OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutTransmits.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutTransmits_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutTransmits_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutTransmits = _Cie1000IpStatisticsGlobalsIpv6HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 29),
    _Cie1000IpStatisticsGlobalsIpv6HCOutTransmits_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutTransmits.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutOctets = _Cie1000IpStatisticsGlobalsIpv6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 30),
    _Cie1000IpStatisticsGlobalsIpv6OutOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutOctets = _Cie1000IpStatisticsGlobalsIpv6HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 31),
    _Cie1000IpStatisticsGlobalsIpv6HCOutOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InMcastPkts = _Cie1000IpStatisticsGlobalsIpv6InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 32),
    _Cie1000IpStatisticsGlobalsIpv6InMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInMcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInMcastPkts = _Cie1000IpStatisticsGlobalsIpv6HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 33),
    _Cie1000IpStatisticsGlobalsIpv6HCInMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InMcastOctets = _Cie1000IpStatisticsGlobalsIpv6InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 34),
    _Cie1000IpStatisticsGlobalsIpv6InMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInMcastOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInMcastOctets = _Cie1000IpStatisticsGlobalsIpv6HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 35),
    _Cie1000IpStatisticsGlobalsIpv6HCInMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutMcastPkts = _Cie1000IpStatisticsGlobalsIpv6OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 36),
    _Cie1000IpStatisticsGlobalsIpv6OutMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts = _Cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 37),
    _Cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutMcastOctets = _Cie1000IpStatisticsGlobalsIpv6OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 38),
    _Cie1000IpStatisticsGlobalsIpv6OutMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets = _Cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 39),
    _Cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6InBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6InBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6InBcastPkts = _Cie1000IpStatisticsGlobalsIpv6InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 40),
    _Cie1000IpStatisticsGlobalsIpv6InBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCInBcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCInBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCInBcastPkts = _Cie1000IpStatisticsGlobalsIpv6HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 41),
    _Cie1000IpStatisticsGlobalsIpv6HCInBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCInBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6OutBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6OutBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6OutBcastPkts = _Cie1000IpStatisticsGlobalsIpv6OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 42),
    _Cie1000IpStatisticsGlobalsIpv6OutBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6OutBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts = _Cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 43),
    _Cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts_Type()
)
cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6DiscontinuityTime_Type = Counter64
_Cie1000IpStatisticsGlobalsIpv6DiscontinuityTime_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6DiscontinuityTime = _Cie1000IpStatisticsGlobalsIpv6DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 44),
    _Cie1000IpStatisticsGlobalsIpv6DiscontinuityTime_Type()
)
cie1000IpStatisticsGlobalsIpv6DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6DiscontinuityTime.setStatus("current")
_Cie1000IpStatisticsGlobalsIpv6RefreshRate_Type = Unsigned32
_Cie1000IpStatisticsGlobalsIpv6RefreshRate_Object = MibScalar
cie1000IpStatisticsGlobalsIpv6RefreshRate = _Cie1000IpStatisticsGlobalsIpv6RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 1, 2, 45),
    _Cie1000IpStatisticsGlobalsIpv6RefreshRate_Type()
)
cie1000IpStatisticsGlobalsIpv6RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6RefreshRate.setStatus("current")
_Cie1000IpStatisticsInterfaces_ObjectIdentity = ObjectIdentity
cie1000IpStatisticsInterfaces = _Cie1000IpStatisticsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2)
)
_Cie1000IpStatisticsInterfacesLinkTable_Object = MibTable
cie1000IpStatisticsInterfacesLinkTable = _Cie1000IpStatisticsInterfacesLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkTable.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkEntry_Object = MibTableRow
cie1000IpStatisticsInterfacesLinkEntry = _Cie1000IpStatisticsInterfacesLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1)
)
cie1000IpStatisticsInterfacesLinkEntry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkEntry.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkIfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatisticsInterfacesLinkIfIndex_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkIfIndex = _Cie1000IpStatisticsInterfacesLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 1),
    _Cie1000IpStatisticsInterfacesLinkIfIndex_Type()
)
cie1000IpStatisticsInterfacesLinkIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkIfIndex.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkInPackets_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkInPackets_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkInPackets = _Cie1000IpStatisticsInterfacesLinkInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 2),
    _Cie1000IpStatisticsInterfacesLinkInPackets_Type()
)
cie1000IpStatisticsInterfacesLinkInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkInPackets.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkOutPackets_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkOutPackets_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkOutPackets = _Cie1000IpStatisticsInterfacesLinkOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 3),
    _Cie1000IpStatisticsInterfacesLinkOutPackets_Type()
)
cie1000IpStatisticsInterfacesLinkOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkOutPackets.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkInBytes_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkInBytes_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkInBytes = _Cie1000IpStatisticsInterfacesLinkInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 4),
    _Cie1000IpStatisticsInterfacesLinkInBytes_Type()
)
cie1000IpStatisticsInterfacesLinkInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkInBytes.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkOutBytes_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkOutBytes_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkOutBytes = _Cie1000IpStatisticsInterfacesLinkOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 5),
    _Cie1000IpStatisticsInterfacesLinkOutBytes_Type()
)
cie1000IpStatisticsInterfacesLinkOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkOutBytes.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkInMulticasts_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkInMulticasts_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkInMulticasts = _Cie1000IpStatisticsInterfacesLinkInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 6),
    _Cie1000IpStatisticsInterfacesLinkInMulticasts_Type()
)
cie1000IpStatisticsInterfacesLinkInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkInMulticasts.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkOutMulticasts_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkOutMulticasts_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkOutMulticasts = _Cie1000IpStatisticsInterfacesLinkOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 7),
    _Cie1000IpStatisticsInterfacesLinkOutMulticasts_Type()
)
cie1000IpStatisticsInterfacesLinkOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkOutMulticasts.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkInBroadcasts_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkInBroadcasts_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkInBroadcasts = _Cie1000IpStatisticsInterfacesLinkInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 8),
    _Cie1000IpStatisticsInterfacesLinkInBroadcasts_Type()
)
cie1000IpStatisticsInterfacesLinkInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkInBroadcasts.setStatus("current")
_Cie1000IpStatisticsInterfacesLinkOutBroadcasts_Type = Counter64
_Cie1000IpStatisticsInterfacesLinkOutBroadcasts_Object = MibTableColumn
cie1000IpStatisticsInterfacesLinkOutBroadcasts = _Cie1000IpStatisticsInterfacesLinkOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 1, 1, 9),
    _Cie1000IpStatisticsInterfacesLinkOutBroadcasts_Type()
)
cie1000IpStatisticsInterfacesLinkOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkOutBroadcasts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4Table_Object = MibTable
cie1000IpStatisticsInterfacesIpv4Table = _Cie1000IpStatisticsInterfacesIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4Table.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4Entry_Object = MibTableRow
cie1000IpStatisticsInterfacesIpv4Entry = _Cie1000IpStatisticsInterfacesIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1)
)
cie1000IpStatisticsInterfacesIpv4Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4IfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4Entry.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatisticsInterfacesIpv4IfIndex_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4IfIndex = _Cie1000IpStatisticsInterfacesIpv4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 1),
    _Cie1000IpStatisticsInterfacesIpv4IfIndex_Type()
)
cie1000IpStatisticsInterfacesIpv4IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4IfIndex.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InReceives_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InReceives_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InReceives = _Cie1000IpStatisticsInterfacesIpv4InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 2),
    _Cie1000IpStatisticsInterfacesIpv4InReceives_Type()
)
cie1000IpStatisticsInterfacesIpv4InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InReceives.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInReceives_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInReceives_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInReceives = _Cie1000IpStatisticsInterfacesIpv4HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 3),
    _Cie1000IpStatisticsInterfacesIpv4HCInReceives_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInReceives.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InOctets = _Cie1000IpStatisticsInterfacesIpv4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 4),
    _Cie1000IpStatisticsInterfacesIpv4InOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInOctets = _Cie1000IpStatisticsInterfacesIpv4HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 5),
    _Cie1000IpStatisticsInterfacesIpv4HCInOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InHdrErrors_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InHdrErrors_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InHdrErrors = _Cie1000IpStatisticsInterfacesIpv4InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 6),
    _Cie1000IpStatisticsInterfacesIpv4InHdrErrors_Type()
)
cie1000IpStatisticsInterfacesIpv4InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InHdrErrors.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InNoRoutes_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InNoRoutes = _Cie1000IpStatisticsInterfacesIpv4InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 7),
    _Cie1000IpStatisticsInterfacesIpv4InNoRoutes_Type()
)
cie1000IpStatisticsInterfacesIpv4InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InNoRoutes.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InAddrErrors_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InAddrErrors_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InAddrErrors = _Cie1000IpStatisticsInterfacesIpv4InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 8),
    _Cie1000IpStatisticsInterfacesIpv4InAddrErrors_Type()
)
cie1000IpStatisticsInterfacesIpv4InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InAddrErrors.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InUnknownProtos_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InUnknownProtos_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InUnknownProtos = _Cie1000IpStatisticsInterfacesIpv4InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 9),
    _Cie1000IpStatisticsInterfacesIpv4InUnknownProtos_Type()
)
cie1000IpStatisticsInterfacesIpv4InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InUnknownProtos.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InTruncatedPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InTruncatedPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InTruncatedPkts = _Cie1000IpStatisticsInterfacesIpv4InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 10),
    _Cie1000IpStatisticsInterfacesIpv4InTruncatedPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InTruncatedPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InForwDatagrams = _Cie1000IpStatisticsInterfacesIpv4InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 11),
    _Cie1000IpStatisticsInterfacesIpv4InForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv4InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams = _Cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 12),
    _Cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4ReasmReqds_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4ReasmReqds_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4ReasmReqds = _Cie1000IpStatisticsInterfacesIpv4ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 13),
    _Cie1000IpStatisticsInterfacesIpv4ReasmReqds_Type()
)
cie1000IpStatisticsInterfacesIpv4ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4ReasmReqds.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4ReasmOKs_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4ReasmOKs_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4ReasmOKs = _Cie1000IpStatisticsInterfacesIpv4ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 14),
    _Cie1000IpStatisticsInterfacesIpv4ReasmOKs_Type()
)
cie1000IpStatisticsInterfacesIpv4ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4ReasmOKs.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4ReasmFails_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4ReasmFails_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4ReasmFails = _Cie1000IpStatisticsInterfacesIpv4ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 15),
    _Cie1000IpStatisticsInterfacesIpv4ReasmFails_Type()
)
cie1000IpStatisticsInterfacesIpv4ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4ReasmFails.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InDiscards_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InDiscards_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InDiscards = _Cie1000IpStatisticsInterfacesIpv4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 16),
    _Cie1000IpStatisticsInterfacesIpv4InDiscards_Type()
)
cie1000IpStatisticsInterfacesIpv4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InDiscards.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InDelivers_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InDelivers_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InDelivers = _Cie1000IpStatisticsInterfacesIpv4InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 17),
    _Cie1000IpStatisticsInterfacesIpv4InDelivers_Type()
)
cie1000IpStatisticsInterfacesIpv4InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InDelivers.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInDelivers_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInDelivers_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInDelivers = _Cie1000IpStatisticsInterfacesIpv4HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 18),
    _Cie1000IpStatisticsInterfacesIpv4HCInDelivers_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInDelivers.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutRequests_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutRequests_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutRequests = _Cie1000IpStatisticsInterfacesIpv4OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 19),
    _Cie1000IpStatisticsInterfacesIpv4OutRequests_Type()
)
cie1000IpStatisticsInterfacesIpv4OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutRequests.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutRequests_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutRequests_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutRequests = _Cie1000IpStatisticsInterfacesIpv4HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 20),
    _Cie1000IpStatisticsInterfacesIpv4HCOutRequests_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutRequests.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutNoRoutes_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutNoRoutes = _Cie1000IpStatisticsInterfacesIpv4OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 21),
    _Cie1000IpStatisticsInterfacesIpv4OutNoRoutes_Type()
)
cie1000IpStatisticsInterfacesIpv4OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutNoRoutes.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutForwDatagrams = _Cie1000IpStatisticsInterfacesIpv4OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 22),
    _Cie1000IpStatisticsInterfacesIpv4OutForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv4OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams = _Cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 23),
    _Cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutDiscards_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutDiscards_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutDiscards = _Cie1000IpStatisticsInterfacesIpv4OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 24),
    _Cie1000IpStatisticsInterfacesIpv4OutDiscards_Type()
)
cie1000IpStatisticsInterfacesIpv4OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutDiscards.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutFragReqds_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutFragReqds_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutFragReqds = _Cie1000IpStatisticsInterfacesIpv4OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 25),
    _Cie1000IpStatisticsInterfacesIpv4OutFragReqds_Type()
)
cie1000IpStatisticsInterfacesIpv4OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutFragReqds.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutFragOKs_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutFragOKs_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutFragOKs = _Cie1000IpStatisticsInterfacesIpv4OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 26),
    _Cie1000IpStatisticsInterfacesIpv4OutFragOKs_Type()
)
cie1000IpStatisticsInterfacesIpv4OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutFragOKs.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutFragFails_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutFragFails_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutFragFails = _Cie1000IpStatisticsInterfacesIpv4OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 27),
    _Cie1000IpStatisticsInterfacesIpv4OutFragFails_Type()
)
cie1000IpStatisticsInterfacesIpv4OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutFragFails.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutFragCreates_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutFragCreates_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutFragCreates = _Cie1000IpStatisticsInterfacesIpv4OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 28),
    _Cie1000IpStatisticsInterfacesIpv4OutFragCreates_Type()
)
cie1000IpStatisticsInterfacesIpv4OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutFragCreates.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutTransmits_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutTransmits_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutTransmits = _Cie1000IpStatisticsInterfacesIpv4OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 29),
    _Cie1000IpStatisticsInterfacesIpv4OutTransmits_Type()
)
cie1000IpStatisticsInterfacesIpv4OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutTransmits.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutTransmits_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutTransmits_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutTransmits = _Cie1000IpStatisticsInterfacesIpv4HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 30),
    _Cie1000IpStatisticsInterfacesIpv4HCOutTransmits_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutTransmits.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutOctets = _Cie1000IpStatisticsInterfacesIpv4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 31),
    _Cie1000IpStatisticsInterfacesIpv4OutOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutOctets = _Cie1000IpStatisticsInterfacesIpv4HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 32),
    _Cie1000IpStatisticsInterfacesIpv4HCOutOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InMcastPkts = _Cie1000IpStatisticsInterfacesIpv4InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 33),
    _Cie1000IpStatisticsInterfacesIpv4InMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInMcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInMcastPkts = _Cie1000IpStatisticsInterfacesIpv4HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 34),
    _Cie1000IpStatisticsInterfacesIpv4HCInMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InMcastOctets = _Cie1000IpStatisticsInterfacesIpv4InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 35),
    _Cie1000IpStatisticsInterfacesIpv4InMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInMcastOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInMcastOctets = _Cie1000IpStatisticsInterfacesIpv4HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 36),
    _Cie1000IpStatisticsInterfacesIpv4HCInMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutMcastPkts = _Cie1000IpStatisticsInterfacesIpv4OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 37),
    _Cie1000IpStatisticsInterfacesIpv4OutMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts = _Cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 38),
    _Cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutMcastOctets = _Cie1000IpStatisticsInterfacesIpv4OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 39),
    _Cie1000IpStatisticsInterfacesIpv4OutMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets = _Cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 40),
    _Cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4InBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4InBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4InBcastPkts = _Cie1000IpStatisticsInterfacesIpv4InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 41),
    _Cie1000IpStatisticsInterfacesIpv4InBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCInBcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCInBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCInBcastPkts = _Cie1000IpStatisticsInterfacesIpv4HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 42),
    _Cie1000IpStatisticsInterfacesIpv4HCInBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCInBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4OutBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4OutBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4OutBcastPkts = _Cie1000IpStatisticsInterfacesIpv4OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 43),
    _Cie1000IpStatisticsInterfacesIpv4OutBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4OutBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts = _Cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 44),
    _Cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4DiscontinuityTime_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv4DiscontinuityTime_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4DiscontinuityTime = _Cie1000IpStatisticsInterfacesIpv4DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 45),
    _Cie1000IpStatisticsInterfacesIpv4DiscontinuityTime_Type()
)
cie1000IpStatisticsInterfacesIpv4DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4DiscontinuityTime.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv4RefreshRate_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv4RefreshRate_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv4RefreshRate = _Cie1000IpStatisticsInterfacesIpv4RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 2, 1, 46),
    _Cie1000IpStatisticsInterfacesIpv4RefreshRate_Type()
)
cie1000IpStatisticsInterfacesIpv4RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4RefreshRate.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6Table_Object = MibTable
cie1000IpStatisticsInterfacesIpv6Table = _Cie1000IpStatisticsInterfacesIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6Table.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6Entry_Object = MibTableRow
cie1000IpStatisticsInterfacesIpv6Entry = _Cie1000IpStatisticsInterfacesIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1)
)
cie1000IpStatisticsInterfacesIpv6Entry.setIndexNames(
    (0, "CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6Entry.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6IfIndex_Type = CIE1000InterfaceIndex
_Cie1000IpStatisticsInterfacesIpv6IfIndex_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6IfIndex = _Cie1000IpStatisticsInterfacesIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 1),
    _Cie1000IpStatisticsInterfacesIpv6IfIndex_Type()
)
cie1000IpStatisticsInterfacesIpv6IfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6IfIndex.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InReceives_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InReceives_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InReceives = _Cie1000IpStatisticsInterfacesIpv6InReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 2),
    _Cie1000IpStatisticsInterfacesIpv6InReceives_Type()
)
cie1000IpStatisticsInterfacesIpv6InReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InReceives.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInReceives_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInReceives_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInReceives = _Cie1000IpStatisticsInterfacesIpv6HCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 3),
    _Cie1000IpStatisticsInterfacesIpv6HCInReceives_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInReceives.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InOctets = _Cie1000IpStatisticsInterfacesIpv6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 4),
    _Cie1000IpStatisticsInterfacesIpv6InOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInOctets = _Cie1000IpStatisticsInterfacesIpv6HCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 5),
    _Cie1000IpStatisticsInterfacesIpv6HCInOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InHdrErrors_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InHdrErrors_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InHdrErrors = _Cie1000IpStatisticsInterfacesIpv6InHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 6),
    _Cie1000IpStatisticsInterfacesIpv6InHdrErrors_Type()
)
cie1000IpStatisticsInterfacesIpv6InHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InHdrErrors.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InNoRoutes_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InNoRoutes = _Cie1000IpStatisticsInterfacesIpv6InNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 7),
    _Cie1000IpStatisticsInterfacesIpv6InNoRoutes_Type()
)
cie1000IpStatisticsInterfacesIpv6InNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InNoRoutes.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InAddrErrors_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InAddrErrors_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InAddrErrors = _Cie1000IpStatisticsInterfacesIpv6InAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 8),
    _Cie1000IpStatisticsInterfacesIpv6InAddrErrors_Type()
)
cie1000IpStatisticsInterfacesIpv6InAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InAddrErrors.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InUnknownProtos_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InUnknownProtos_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InUnknownProtos = _Cie1000IpStatisticsInterfacesIpv6InUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 9),
    _Cie1000IpStatisticsInterfacesIpv6InUnknownProtos_Type()
)
cie1000IpStatisticsInterfacesIpv6InUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InUnknownProtos.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InTruncatedPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InTruncatedPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InTruncatedPkts = _Cie1000IpStatisticsInterfacesIpv6InTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 10),
    _Cie1000IpStatisticsInterfacesIpv6InTruncatedPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6InTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InTruncatedPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InForwDatagrams = _Cie1000IpStatisticsInterfacesIpv6InForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 11),
    _Cie1000IpStatisticsInterfacesIpv6InForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv6InForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams = _Cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 12),
    _Cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6ReasmReqds_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6ReasmReqds_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6ReasmReqds = _Cie1000IpStatisticsInterfacesIpv6ReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 13),
    _Cie1000IpStatisticsInterfacesIpv6ReasmReqds_Type()
)
cie1000IpStatisticsInterfacesIpv6ReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6ReasmReqds.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6ReasmOKs_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6ReasmOKs_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6ReasmOKs = _Cie1000IpStatisticsInterfacesIpv6ReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 14),
    _Cie1000IpStatisticsInterfacesIpv6ReasmOKs_Type()
)
cie1000IpStatisticsInterfacesIpv6ReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6ReasmOKs.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6ReasmFails_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6ReasmFails_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6ReasmFails = _Cie1000IpStatisticsInterfacesIpv6ReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 15),
    _Cie1000IpStatisticsInterfacesIpv6ReasmFails_Type()
)
cie1000IpStatisticsInterfacesIpv6ReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6ReasmFails.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InDiscards_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InDiscards_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InDiscards = _Cie1000IpStatisticsInterfacesIpv6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 16),
    _Cie1000IpStatisticsInterfacesIpv6InDiscards_Type()
)
cie1000IpStatisticsInterfacesIpv6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InDiscards.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InDelivers_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InDelivers_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InDelivers = _Cie1000IpStatisticsInterfacesIpv6InDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 17),
    _Cie1000IpStatisticsInterfacesIpv6InDelivers_Type()
)
cie1000IpStatisticsInterfacesIpv6InDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InDelivers.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInDelivers_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInDelivers_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInDelivers = _Cie1000IpStatisticsInterfacesIpv6HCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 18),
    _Cie1000IpStatisticsInterfacesIpv6HCInDelivers_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInDelivers.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutRequests_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutRequests_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutRequests = _Cie1000IpStatisticsInterfacesIpv6OutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 19),
    _Cie1000IpStatisticsInterfacesIpv6OutRequests_Type()
)
cie1000IpStatisticsInterfacesIpv6OutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutRequests.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutRequests_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutRequests_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutRequests = _Cie1000IpStatisticsInterfacesIpv6HCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 20),
    _Cie1000IpStatisticsInterfacesIpv6HCOutRequests_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutRequests.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutNoRoutes_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutNoRoutes_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutNoRoutes = _Cie1000IpStatisticsInterfacesIpv6OutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 21),
    _Cie1000IpStatisticsInterfacesIpv6OutNoRoutes_Type()
)
cie1000IpStatisticsInterfacesIpv6OutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutNoRoutes.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutForwDatagrams_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutForwDatagrams = _Cie1000IpStatisticsInterfacesIpv6OutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 22),
    _Cie1000IpStatisticsInterfacesIpv6OutForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv6OutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams = _Cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 23),
    _Cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutDiscards_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutDiscards_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutDiscards = _Cie1000IpStatisticsInterfacesIpv6OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 24),
    _Cie1000IpStatisticsInterfacesIpv6OutDiscards_Type()
)
cie1000IpStatisticsInterfacesIpv6OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutDiscards.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutFragReqds_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutFragReqds_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutFragReqds = _Cie1000IpStatisticsInterfacesIpv6OutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 25),
    _Cie1000IpStatisticsInterfacesIpv6OutFragReqds_Type()
)
cie1000IpStatisticsInterfacesIpv6OutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutFragReqds.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutFragOKs_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutFragOKs_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutFragOKs = _Cie1000IpStatisticsInterfacesIpv6OutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 26),
    _Cie1000IpStatisticsInterfacesIpv6OutFragOKs_Type()
)
cie1000IpStatisticsInterfacesIpv6OutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutFragOKs.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutFragFails_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutFragFails_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutFragFails = _Cie1000IpStatisticsInterfacesIpv6OutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 27),
    _Cie1000IpStatisticsInterfacesIpv6OutFragFails_Type()
)
cie1000IpStatisticsInterfacesIpv6OutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutFragFails.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutFragCreates_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutFragCreates_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutFragCreates = _Cie1000IpStatisticsInterfacesIpv6OutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 28),
    _Cie1000IpStatisticsInterfacesIpv6OutFragCreates_Type()
)
cie1000IpStatisticsInterfacesIpv6OutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutFragCreates.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutTransmits_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutTransmits_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutTransmits = _Cie1000IpStatisticsInterfacesIpv6OutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 29),
    _Cie1000IpStatisticsInterfacesIpv6OutTransmits_Type()
)
cie1000IpStatisticsInterfacesIpv6OutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutTransmits.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutTransmits_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutTransmits_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutTransmits = _Cie1000IpStatisticsInterfacesIpv6HCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 30),
    _Cie1000IpStatisticsInterfacesIpv6HCOutTransmits_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutTransmits.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutOctets = _Cie1000IpStatisticsInterfacesIpv6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 31),
    _Cie1000IpStatisticsInterfacesIpv6OutOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutOctets = _Cie1000IpStatisticsInterfacesIpv6HCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 32),
    _Cie1000IpStatisticsInterfacesIpv6HCOutOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InMcastPkts = _Cie1000IpStatisticsInterfacesIpv6InMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 33),
    _Cie1000IpStatisticsInterfacesIpv6InMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6InMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInMcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInMcastPkts = _Cie1000IpStatisticsInterfacesIpv6HCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 34),
    _Cie1000IpStatisticsInterfacesIpv6HCInMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InMcastOctets = _Cie1000IpStatisticsInterfacesIpv6InMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 35),
    _Cie1000IpStatisticsInterfacesIpv6InMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6InMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInMcastOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInMcastOctets = _Cie1000IpStatisticsInterfacesIpv6HCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 36),
    _Cie1000IpStatisticsInterfacesIpv6HCInMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutMcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutMcastPkts = _Cie1000IpStatisticsInterfacesIpv6OutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 37),
    _Cie1000IpStatisticsInterfacesIpv6OutMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6OutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts = _Cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 38),
    _Cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutMcastOctets_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutMcastOctets = _Cie1000IpStatisticsInterfacesIpv6OutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 39),
    _Cie1000IpStatisticsInterfacesIpv6OutMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6OutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets = _Cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 40),
    _Cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6InBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6InBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6InBcastPkts = _Cie1000IpStatisticsInterfacesIpv6InBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 41),
    _Cie1000IpStatisticsInterfacesIpv6InBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6InBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCInBcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCInBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCInBcastPkts = _Cie1000IpStatisticsInterfacesIpv6HCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 42),
    _Cie1000IpStatisticsInterfacesIpv6HCInBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6HCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCInBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6OutBcastPkts_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6OutBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6OutBcastPkts = _Cie1000IpStatisticsInterfacesIpv6OutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 43),
    _Cie1000IpStatisticsInterfacesIpv6OutBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6OutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6OutBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts = _Cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 44),
    _Cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts_Type()
)
cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6DiscontinuityTime_Type = Counter64
_Cie1000IpStatisticsInterfacesIpv6DiscontinuityTime_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6DiscontinuityTime = _Cie1000IpStatisticsInterfacesIpv6DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 45),
    _Cie1000IpStatisticsInterfacesIpv6DiscontinuityTime_Type()
)
cie1000IpStatisticsInterfacesIpv6DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6DiscontinuityTime.setStatus("current")
_Cie1000IpStatisticsInterfacesIpv6RefreshRate_Type = Unsigned32
_Cie1000IpStatisticsInterfacesIpv6RefreshRate_Object = MibTableColumn
cie1000IpStatisticsInterfacesIpv6RefreshRate = _Cie1000IpStatisticsInterfacesIpv6RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 5, 2, 3, 1, 46),
    _Cie1000IpStatisticsInterfacesIpv6RefreshRate_Type()
)
cie1000IpStatisticsInterfacesIpv6RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6RefreshRate.setStatus("current")
_Cie1000IpTrap_ObjectIdentity = ObjectIdentity
cie1000IpTrap = _Cie1000IpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 6)
)
_Cie1000IpMibConformance_ObjectIdentity = ObjectIdentity
cie1000IpMibConformance = _Cie1000IpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2)
)
_Cie1000IpMibCompliances_ObjectIdentity = ObjectIdentity
cie1000IpMibCompliances = _Cie1000IpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 1)
)
_Cie1000IpMibGroups_ObjectIdentity = ObjectIdentity
cie1000IpMibGroups = _Cie1000IpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2)
)

# Managed Objects groups

cie1000IpCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 1)
)
cie1000IpCapabilitiesInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasIpv4HostCapabilities"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasIpv6HostCapabilities"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesMaxNumberOfIpInterfaces"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesMaxNumberOfStaticRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesNumberOfLpmHardwareEntries"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics"),
        ("CIE1000-IP-MIB", "cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics"))
)
if mibBuilder.loadTexts:
    cie1000IpCapabilitiesInfoGroup.setStatus("current")

cie1000IpConfigGlobalsMainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 2)
)
cie1000IpConfigGlobalsMainInfoGroup.setObjects(
    ("CIE1000-IP-MIB", "cie1000IpConfigGlobalsMainEnableRouting")
)
if mibBuilder.loadTexts:
    cie1000IpConfigGlobalsMainInfoGroup.setStatus("current")

cie1000IpConfigInterfacesTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 3)
)
cie1000IpConfigInterfacesTableInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesAction"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesTableInfoGroup.setStatus("current")

cie1000IpConfigInterfacesTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 4)
)
cie1000IpConfigInterfacesTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigInterfacesTableRowEditorIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesTableRowEditorInfoGroup.setStatus("current")

cie1000IpConfigInterfacesIpv4TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 5)
)
cie1000IpConfigInterfacesIpv4TableInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4Active"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4EnableDhcpClient"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4Ipv4Address"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4PrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv4TableInfoGroup.setStatus("current")

cie1000IpConfigInterfacesIpv6TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 6)
)
cie1000IpConfigInterfacesIpv6TableInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv6IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv6Active"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv6Ipv6Address"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv6PrefixSize"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigInterfacesIpv6TableInfoGroup.setStatus("current")

cie1000IpConfigRoutesIpv4TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 7)
)
cie1000IpConfigRoutesIpv4TableInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4NetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4NetworkPrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4NextHop"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4Action"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4TableInfoGroup.setStatus("current")

cie1000IpConfigRoutesIpv4RowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 8)
)
cie1000IpConfigRoutesIpv4RowEditorInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4RowEditorNetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4RowEditorNextHop"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4RowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv4RowEditorInfoGroup.setStatus("current")

cie1000IpConfigRoutesIpv6TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 9)
)
cie1000IpConfigRoutesIpv6TableInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NetworkPrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NextHop"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6NextHopInterface"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6Action"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6TableInfoGroup.setStatus("current")

cie1000IpConfigRoutesIpv6RowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 10)
)
cie1000IpConfigRoutesIpv6RowEditorInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6RowEditorNetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6RowEditorNextHop"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6RowEditorNextHopInterface"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6RowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpConfigRoutesIpv6RowEditorInfoGroup.setStatus("current")

cie1000IpStatusGlobalsIpv4NeighbourInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 11)
)
cie1000IpStatusGlobalsIpv4NeighbourInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv4NeighbourIpv4"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv4NeighbourMacAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv4NeighbourInterface"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv4NeighbourInfoGroup.setStatus("current")

cie1000IpStatusGlobalsIpv6NeighbourInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 12)
)
cie1000IpStatusGlobalsIpv6NeighbourInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourIpAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourMacAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourInterface"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusGlobalsIpv6NeighbourInfoGroup.setStatus("current")

cie1000IpStatusInterfacesLinkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 13)
)
cie1000IpStatusInterfacesLinkInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkOsInterfaceIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMtu"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMacAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkUp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkBroadcast"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkLoopback"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkRunning"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkNoarp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkPromisc"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMulticast"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesLinkInfoGroup.setStatus("current")

cie1000IpStatusInterfacesIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 14)
)
cie1000IpStatusInterfacesIpv4InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4NetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4NetworkMaskLength"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4Broadcast"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv4InfoGroup.setStatus("current")

cie1000IpStatusInterfacesDhcpClientV4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 15)
)
cie1000IpStatusInterfacesDhcpClientV4InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusInterfacesDhcpClientV4IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesDhcpClientV4State"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesDhcpClientV4ServerIp"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesDhcpClientV4InfoGroup.setStatus("current")

cie1000IpStatusInterfacesIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 16)
)
cie1000IpStatusInterfacesIpv6InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6NetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6NetworkMaskLength"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6Tentative"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6Duplicated"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6Detached"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6Nodad"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6Autoconf"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusInterfacesIpv6InfoGroup.setStatus("current")

cie1000IpStatusRoutesIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 17)
)
cie1000IpStatusRoutesIpv4InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4NetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4NetworkPrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4NextHop"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4DerivedNextHopInterface"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4FlagUp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4FlagHost"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4FlagGateway"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4OwnerConf"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4OwnerDhcp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4OwnerDynamic"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv4InfoGroup.setStatus("current")

cie1000IpStatusRoutesIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 18)
)
cie1000IpStatusRoutesIpv6InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NetworkAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NetworkPrefixSize"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NextHop"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6NextHopInterface"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6DerivedNextHopInterface"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6FlagUp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6FlagHost"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6FlagGateway"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6OwnerConf"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6OwnerDhcp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6OwnerDynamic"))
)
if mibBuilder.loadTexts:
    cie1000IpStatusRoutesIpv6InfoGroup.setStatus("current")

cie1000IpControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 19)
)
cie1000IpControlGlobalsInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpControlGlobalsIpv4NeighbourTableClear"),
        ("CIE1000-IP-MIB", "cie1000IpControlGlobalsIpv6NeighbourTableClear"),
        ("CIE1000-IP-MIB", "cie1000IpControlGlobalsIpv4SystemStatisticsClear"),
        ("CIE1000-IP-MIB", "cie1000IpControlGlobalsIpv6SystemStatisticsClear"))
)
if mibBuilder.loadTexts:
    cie1000IpControlGlobalsInfoGroup.setStatus("current")

cie1000IpControlInterfaceDhcpClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 20)
)
cie1000IpControlInterfaceDhcpClientInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpControlInterfaceDhcpClientIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpControlInterfaceDhcpClientRestart"))
)
if mibBuilder.loadTexts:
    cie1000IpControlInterfaceDhcpClientInfoGroup.setStatus("current")

cie1000IpStatisticsGlobalsIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 21)
)
cie1000IpStatisticsGlobalsIpv4InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InHdrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InAddrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InUnknownProtos"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InTruncatedPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4ReasmReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4ReasmOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4ReasmFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutFragReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutFragOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutFragFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutFragCreates"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCInBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4OutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4DiscontinuityTime"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4RefreshRate"))
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv4InfoGroup.setStatus("current")

cie1000IpStatisticsGlobalsIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 22)
)
cie1000IpStatisticsGlobalsIpv6InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InHdrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InAddrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InUnknownProtos"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InTruncatedPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6ReasmReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6ReasmOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6ReasmFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutFragReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutFragOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutFragFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutFragCreates"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCInBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6OutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6DiscontinuityTime"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6RefreshRate"))
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsGlobalsIpv6InfoGroup.setStatus("current")

cie1000IpStatisticsInterfacesLinkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 23)
)
cie1000IpStatisticsInterfacesLinkInfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkInPackets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkOutPackets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkInBytes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkOutBytes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkInMulticasts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkOutMulticasts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkInBroadcasts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkOutBroadcasts"))
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesLinkInfoGroup.setStatus("current")

cie1000IpStatisticsInterfacesIpv4InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 24)
)
cie1000IpStatisticsInterfacesIpv4InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InHdrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InAddrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InUnknownProtos"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InTruncatedPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4ReasmReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4ReasmOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4ReasmFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutFragReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutFragOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutFragFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutFragCreates"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCInBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4OutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4DiscontinuityTime"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4RefreshRate"))
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv4InfoGroup.setStatus("current")

cie1000IpStatisticsInterfacesIpv6InfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 25)
)
cie1000IpStatisticsInterfacesIpv6InfoGroup.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6IfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInReceives"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InHdrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InAddrErrors"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InUnknownProtos"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InTruncatedPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6ReasmReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6ReasmOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6ReasmFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInDelivers"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutRequests"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutNoRoutes"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutDiscards"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutFragReqds"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutFragOKs"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutFragFails"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutFragCreates"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutTransmits"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCInBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6OutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6DiscontinuityTime"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6RefreshRate"))
)
if mibBuilder.loadTexts:
    cie1000IpStatisticsInterfacesIpv6InfoGroup.setStatus("current")


# Notification objects

cie1000IpTrapInterfacesLinkAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 6, 1)
)
cie1000IpTrapInterfacesLinkAdd.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkOsInterfaceIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMtu"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMacAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkUp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkBroadcast"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkLoopback"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkRunning"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkNoarp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkPromisc"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMulticast"))
)
if mibBuilder.loadTexts:
    cie1000IpTrapInterfacesLinkAdd.setStatus(
        "current"
    )

cie1000IpTrapInterfacesLinkMod = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 6, 2)
)
cie1000IpTrapInterfacesLinkMod.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkIfIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkOsInterfaceIndex"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMtu"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMacAddress"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkUp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkBroadcast"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkLoopback"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkRunning"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkNoarp"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkPromisc"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkMulticast"))
)
if mibBuilder.loadTexts:
    cie1000IpTrapInterfacesLinkMod.setStatus(
        "current"
    )

cie1000IpTrapInterfacesLinkDel = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 1, 6, 3)
)
cie1000IpTrapInterfacesLinkDel.setObjects(
    ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkIfIndex")
)
if mibBuilder.loadTexts:
    cie1000IpTrapInterfacesLinkDel.setStatus(
        "current"
    )


# Notifications groups

cie1000IpTrapInterfacesLinkAddInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 26)
)
cie1000IpTrapInterfacesLinkAddInfoGroup.setObjects(
    ("CIE1000-IP-MIB", "cie1000IpTrapInterfacesLinkAdd")
)
if mibBuilder.loadTexts:
    cie1000IpTrapInterfacesLinkAddInfoGroup.setStatus(
        "current"
    )

cie1000IpTrapInterfacesLinkModInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 27)
)
cie1000IpTrapInterfacesLinkModInfoGroup.setObjects(
    ("CIE1000-IP-MIB", "cie1000IpTrapInterfacesLinkMod")
)
if mibBuilder.loadTexts:
    cie1000IpTrapInterfacesLinkModInfoGroup.setStatus(
        "current"
    )

cie1000IpTrapInterfacesLinkDelInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 2, 28)
)
cie1000IpTrapInterfacesLinkDelInfoGroup.setObjects(
    ("CIE1000-IP-MIB", "cie1000IpTrapInterfacesLinkDel")
)
if mibBuilder.loadTexts:
    cie1000IpTrapInterfacesLinkDelInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cie1000IpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 102, 2, 1, 1)
)
cie1000IpMibCompliance.setObjects(
      *(("CIE1000-IP-MIB", "cie1000IpCapabilitiesInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigGlobalsMainInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesTableInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesTableRowEditorInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv4TableInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigInterfacesIpv6TableInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4TableInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv4RowEditorInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6TableInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpConfigRoutesIpv6RowEditorInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv4NeighbourInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusGlobalsIpv6NeighbourInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesLinkInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv4InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesDhcpClientV4InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusInterfacesIpv6InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv4InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatusRoutesIpv6InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpControlGlobalsInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpControlInterfaceDhcpClientInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv4InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsGlobalsIpv6InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesLinkInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv4InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpStatisticsInterfacesIpv6InfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpTrapInterfacesLinkAddInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpTrapInterfacesLinkModInfoGroup"),
        ("CIE1000-IP-MIB", "cie1000IpTrapInterfacesLinkDelInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000IpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-IP-MIB",
    **{"CIE1000IpDhcpClientState": CIE1000IpDhcpClientState,
       "cie1000IpMib": cie1000IpMib,
       "cie1000IpMibObjects": cie1000IpMibObjects,
       "cie1000IpCapabilities": cie1000IpCapabilities,
       "cie1000IpCapabilitiesHasIpv4HostCapabilities": cie1000IpCapabilitiesHasIpv4HostCapabilities,
       "cie1000IpCapabilitiesHasIpv6HostCapabilities": cie1000IpCapabilitiesHasIpv6HostCapabilities,
       "cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities": cie1000IpCapabilitiesHasIpv4UnicastRoutingCapabilities,
       "cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities": cie1000IpCapabilitiesHasIpv4UnicastHwRoutingCapabilities,
       "cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities": cie1000IpCapabilitiesHasIpv6UnicastRoutingCapabilities,
       "cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities": cie1000IpCapabilitiesHasIpv6UnicastHwRoutingCapabilities,
       "cie1000IpCapabilitiesMaxNumberOfIpInterfaces": cie1000IpCapabilitiesMaxNumberOfIpInterfaces,
       "cie1000IpCapabilitiesMaxNumberOfStaticRoutes": cie1000IpCapabilitiesMaxNumberOfStaticRoutes,
       "cie1000IpCapabilitiesNumberOfLpmHardwareEntries": cie1000IpCapabilitiesNumberOfLpmHardwareEntries,
       "cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics": cie1000IpCapabilitiesHasPerInterfaceIpv4Statistics,
       "cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics": cie1000IpCapabilitiesHasPerInterfaceIpv6Statistics,
       "cie1000IpConfig": cie1000IpConfig,
       "cie1000IpConfigGlobals": cie1000IpConfigGlobals,
       "cie1000IpConfigGlobalsMain": cie1000IpConfigGlobalsMain,
       "cie1000IpConfigGlobalsMainEnableRouting": cie1000IpConfigGlobalsMainEnableRouting,
       "cie1000IpConfigInterfaces": cie1000IpConfigInterfaces,
       "cie1000IpConfigInterfacesTable": cie1000IpConfigInterfacesTable,
       "cie1000IpConfigInterfacesEntry": cie1000IpConfigInterfacesEntry,
       "cie1000IpConfigInterfacesIfIndex": cie1000IpConfigInterfacesIfIndex,
       "cie1000IpConfigInterfacesAction": cie1000IpConfigInterfacesAction,
       "cie1000IpConfigInterfacesTableRowEditor": cie1000IpConfigInterfacesTableRowEditor,
       "cie1000IpConfigInterfacesTableRowEditorIfIndex": cie1000IpConfigInterfacesTableRowEditorIfIndex,
       "cie1000IpConfigInterfacesTableRowEditorAction": cie1000IpConfigInterfacesTableRowEditorAction,
       "cie1000IpConfigInterfacesIpv4Table": cie1000IpConfigInterfacesIpv4Table,
       "cie1000IpConfigInterfacesIpv4Entry": cie1000IpConfigInterfacesIpv4Entry,
       "cie1000IpConfigInterfacesIpv4IfIndex": cie1000IpConfigInterfacesIpv4IfIndex,
       "cie1000IpConfigInterfacesIpv4Active": cie1000IpConfigInterfacesIpv4Active,
       "cie1000IpConfigInterfacesIpv4EnableDhcpClient": cie1000IpConfigInterfacesIpv4EnableDhcpClient,
       "cie1000IpConfigInterfacesIpv4Ipv4Address": cie1000IpConfigInterfacesIpv4Ipv4Address,
       "cie1000IpConfigInterfacesIpv4PrefixSize": cie1000IpConfigInterfacesIpv4PrefixSize,
       "cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout": cie1000IpConfigInterfacesIpv4DhcpClientFallbackTimeout,
       "cie1000IpConfigInterfacesIpv6Table": cie1000IpConfigInterfacesIpv6Table,
       "cie1000IpConfigInterfacesIpv6Entry": cie1000IpConfigInterfacesIpv6Entry,
       "cie1000IpConfigInterfacesIpv6IfIndex": cie1000IpConfigInterfacesIpv6IfIndex,
       "cie1000IpConfigInterfacesIpv6Active": cie1000IpConfigInterfacesIpv6Active,
       "cie1000IpConfigInterfacesIpv6Ipv6Address": cie1000IpConfigInterfacesIpv6Ipv6Address,
       "cie1000IpConfigInterfacesIpv6PrefixSize": cie1000IpConfigInterfacesIpv6PrefixSize,
       "cie1000IpConfigRoutes": cie1000IpConfigRoutes,
       "cie1000IpConfigRoutesIpv4Table": cie1000IpConfigRoutesIpv4Table,
       "cie1000IpConfigRoutesIpv4Entry": cie1000IpConfigRoutesIpv4Entry,
       "cie1000IpConfigRoutesIpv4NetworkAddress": cie1000IpConfigRoutesIpv4NetworkAddress,
       "cie1000IpConfigRoutesIpv4NetworkPrefixSize": cie1000IpConfigRoutesIpv4NetworkPrefixSize,
       "cie1000IpConfigRoutesIpv4NextHop": cie1000IpConfigRoutesIpv4NextHop,
       "cie1000IpConfigRoutesIpv4Action": cie1000IpConfigRoutesIpv4Action,
       "cie1000IpConfigRoutesIpv4RowEditor": cie1000IpConfigRoutesIpv4RowEditor,
       "cie1000IpConfigRoutesIpv4RowEditorNetworkAddress": cie1000IpConfigRoutesIpv4RowEditorNetworkAddress,
       "cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize": cie1000IpConfigRoutesIpv4RowEditorNetworkPrefixSize,
       "cie1000IpConfigRoutesIpv4RowEditorNextHop": cie1000IpConfigRoutesIpv4RowEditorNextHop,
       "cie1000IpConfigRoutesIpv4RowEditorAction": cie1000IpConfigRoutesIpv4RowEditorAction,
       "cie1000IpConfigRoutesIpv6Table": cie1000IpConfigRoutesIpv6Table,
       "cie1000IpConfigRoutesIpv6Entry": cie1000IpConfigRoutesIpv6Entry,
       "cie1000IpConfigRoutesIpv6NetworkAddress": cie1000IpConfigRoutesIpv6NetworkAddress,
       "cie1000IpConfigRoutesIpv6NetworkPrefixSize": cie1000IpConfigRoutesIpv6NetworkPrefixSize,
       "cie1000IpConfigRoutesIpv6NextHop": cie1000IpConfigRoutesIpv6NextHop,
       "cie1000IpConfigRoutesIpv6NextHopInterface": cie1000IpConfigRoutesIpv6NextHopInterface,
       "cie1000IpConfigRoutesIpv6Action": cie1000IpConfigRoutesIpv6Action,
       "cie1000IpConfigRoutesIpv6RowEditor": cie1000IpConfigRoutesIpv6RowEditor,
       "cie1000IpConfigRoutesIpv6RowEditorNetworkAddress": cie1000IpConfigRoutesIpv6RowEditorNetworkAddress,
       "cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize": cie1000IpConfigRoutesIpv6RowEditorNetworkPrefixSize,
       "cie1000IpConfigRoutesIpv6RowEditorNextHop": cie1000IpConfigRoutesIpv6RowEditorNextHop,
       "cie1000IpConfigRoutesIpv6RowEditorNextHopInterface": cie1000IpConfigRoutesIpv6RowEditorNextHopInterface,
       "cie1000IpConfigRoutesIpv6RowEditorAction": cie1000IpConfigRoutesIpv6RowEditorAction,
       "cie1000IpStatus": cie1000IpStatus,
       "cie1000IpStatusGlobals": cie1000IpStatusGlobals,
       "cie1000IpStatusGlobalsIpv4NeighbourTable": cie1000IpStatusGlobalsIpv4NeighbourTable,
       "cie1000IpStatusGlobalsIpv4NeighbourEntry": cie1000IpStatusGlobalsIpv4NeighbourEntry,
       "cie1000IpStatusGlobalsIpv4NeighbourIpv4": cie1000IpStatusGlobalsIpv4NeighbourIpv4,
       "cie1000IpStatusGlobalsIpv4NeighbourMacAddress": cie1000IpStatusGlobalsIpv4NeighbourMacAddress,
       "cie1000IpStatusGlobalsIpv4NeighbourInterface": cie1000IpStatusGlobalsIpv4NeighbourInterface,
       "cie1000IpStatusGlobalsIpv6NeighbourTable": cie1000IpStatusGlobalsIpv6NeighbourTable,
       "cie1000IpStatusGlobalsIpv6NeighbourEntry": cie1000IpStatusGlobalsIpv6NeighbourEntry,
       "cie1000IpStatusGlobalsIpv6NeighbourIpAddress": cie1000IpStatusGlobalsIpv6NeighbourIpAddress,
       "cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery": cie1000IpStatusGlobalsIpv6NeighbourInterfaceQuery,
       "cie1000IpStatusGlobalsIpv6NeighbourMacAddress": cie1000IpStatusGlobalsIpv6NeighbourMacAddress,
       "cie1000IpStatusGlobalsIpv6NeighbourInterface": cie1000IpStatusGlobalsIpv6NeighbourInterface,
       "cie1000IpStatusInterfaces": cie1000IpStatusInterfaces,
       "cie1000IpStatusInterfacesLinkTable": cie1000IpStatusInterfacesLinkTable,
       "cie1000IpStatusInterfacesLinkEntry": cie1000IpStatusInterfacesLinkEntry,
       "cie1000IpStatusInterfacesLinkIfIndex": cie1000IpStatusInterfacesLinkIfIndex,
       "cie1000IpStatusInterfacesLinkOsInterfaceIndex": cie1000IpStatusInterfacesLinkOsInterfaceIndex,
       "cie1000IpStatusInterfacesLinkMtu": cie1000IpStatusInterfacesLinkMtu,
       "cie1000IpStatusInterfacesLinkMacAddress": cie1000IpStatusInterfacesLinkMacAddress,
       "cie1000IpStatusInterfacesLinkUp": cie1000IpStatusInterfacesLinkUp,
       "cie1000IpStatusInterfacesLinkBroadcast": cie1000IpStatusInterfacesLinkBroadcast,
       "cie1000IpStatusInterfacesLinkLoopback": cie1000IpStatusInterfacesLinkLoopback,
       "cie1000IpStatusInterfacesLinkRunning": cie1000IpStatusInterfacesLinkRunning,
       "cie1000IpStatusInterfacesLinkNoarp": cie1000IpStatusInterfacesLinkNoarp,
       "cie1000IpStatusInterfacesLinkPromisc": cie1000IpStatusInterfacesLinkPromisc,
       "cie1000IpStatusInterfacesLinkMulticast": cie1000IpStatusInterfacesLinkMulticast,
       "cie1000IpStatusInterfacesIpv4Table": cie1000IpStatusInterfacesIpv4Table,
       "cie1000IpStatusInterfacesIpv4Entry": cie1000IpStatusInterfacesIpv4Entry,
       "cie1000IpStatusInterfacesIpv4IfIndex": cie1000IpStatusInterfacesIpv4IfIndex,
       "cie1000IpStatusInterfacesIpv4NetworkAddress": cie1000IpStatusInterfacesIpv4NetworkAddress,
       "cie1000IpStatusInterfacesIpv4NetworkMaskLength": cie1000IpStatusInterfacesIpv4NetworkMaskLength,
       "cie1000IpStatusInterfacesIpv4Broadcast": cie1000IpStatusInterfacesIpv4Broadcast,
       "cie1000IpStatusInterfacesDhcpClientV4Table": cie1000IpStatusInterfacesDhcpClientV4Table,
       "cie1000IpStatusInterfacesDhcpClientV4Entry": cie1000IpStatusInterfacesDhcpClientV4Entry,
       "cie1000IpStatusInterfacesDhcpClientV4IfIndex": cie1000IpStatusInterfacesDhcpClientV4IfIndex,
       "cie1000IpStatusInterfacesDhcpClientV4State": cie1000IpStatusInterfacesDhcpClientV4State,
       "cie1000IpStatusInterfacesDhcpClientV4ServerIp": cie1000IpStatusInterfacesDhcpClientV4ServerIp,
       "cie1000IpStatusInterfacesIpv6Table": cie1000IpStatusInterfacesIpv6Table,
       "cie1000IpStatusInterfacesIpv6Entry": cie1000IpStatusInterfacesIpv6Entry,
       "cie1000IpStatusInterfacesIpv6IfIndex": cie1000IpStatusInterfacesIpv6IfIndex,
       "cie1000IpStatusInterfacesIpv6NetworkAddress": cie1000IpStatusInterfacesIpv6NetworkAddress,
       "cie1000IpStatusInterfacesIpv6NetworkMaskLength": cie1000IpStatusInterfacesIpv6NetworkMaskLength,
       "cie1000IpStatusInterfacesIpv6Tentative": cie1000IpStatusInterfacesIpv6Tentative,
       "cie1000IpStatusInterfacesIpv6Duplicated": cie1000IpStatusInterfacesIpv6Duplicated,
       "cie1000IpStatusInterfacesIpv6Detached": cie1000IpStatusInterfacesIpv6Detached,
       "cie1000IpStatusInterfacesIpv6Nodad": cie1000IpStatusInterfacesIpv6Nodad,
       "cie1000IpStatusInterfacesIpv6Autoconf": cie1000IpStatusInterfacesIpv6Autoconf,
       "cie1000IpStatusRoutes": cie1000IpStatusRoutes,
       "cie1000IpStatusRoutesIpv4Table": cie1000IpStatusRoutesIpv4Table,
       "cie1000IpStatusRoutesIpv4Entry": cie1000IpStatusRoutesIpv4Entry,
       "cie1000IpStatusRoutesIpv4NetworkAddress": cie1000IpStatusRoutesIpv4NetworkAddress,
       "cie1000IpStatusRoutesIpv4NetworkPrefixSize": cie1000IpStatusRoutesIpv4NetworkPrefixSize,
       "cie1000IpStatusRoutesIpv4NextHop": cie1000IpStatusRoutesIpv4NextHop,
       "cie1000IpStatusRoutesIpv4DerivedNextHopInterface": cie1000IpStatusRoutesIpv4DerivedNextHopInterface,
       "cie1000IpStatusRoutesIpv4FlagUp": cie1000IpStatusRoutesIpv4FlagUp,
       "cie1000IpStatusRoutesIpv4FlagHost": cie1000IpStatusRoutesIpv4FlagHost,
       "cie1000IpStatusRoutesIpv4FlagGateway": cie1000IpStatusRoutesIpv4FlagGateway,
       "cie1000IpStatusRoutesIpv4OwnerConf": cie1000IpStatusRoutesIpv4OwnerConf,
       "cie1000IpStatusRoutesIpv4OwnerDhcp": cie1000IpStatusRoutesIpv4OwnerDhcp,
       "cie1000IpStatusRoutesIpv4OwnerDynamic": cie1000IpStatusRoutesIpv4OwnerDynamic,
       "cie1000IpStatusRoutesIpv6Table": cie1000IpStatusRoutesIpv6Table,
       "cie1000IpStatusRoutesIpv6Entry": cie1000IpStatusRoutesIpv6Entry,
       "cie1000IpStatusRoutesIpv6NetworkAddress": cie1000IpStatusRoutesIpv6NetworkAddress,
       "cie1000IpStatusRoutesIpv6NetworkPrefixSize": cie1000IpStatusRoutesIpv6NetworkPrefixSize,
       "cie1000IpStatusRoutesIpv6NextHop": cie1000IpStatusRoutesIpv6NextHop,
       "cie1000IpStatusRoutesIpv6NextHopInterface": cie1000IpStatusRoutesIpv6NextHopInterface,
       "cie1000IpStatusRoutesIpv6DerivedNextHopInterface": cie1000IpStatusRoutesIpv6DerivedNextHopInterface,
       "cie1000IpStatusRoutesIpv6FlagUp": cie1000IpStatusRoutesIpv6FlagUp,
       "cie1000IpStatusRoutesIpv6FlagHost": cie1000IpStatusRoutesIpv6FlagHost,
       "cie1000IpStatusRoutesIpv6FlagGateway": cie1000IpStatusRoutesIpv6FlagGateway,
       "cie1000IpStatusRoutesIpv6OwnerConf": cie1000IpStatusRoutesIpv6OwnerConf,
       "cie1000IpStatusRoutesIpv6OwnerDhcp": cie1000IpStatusRoutesIpv6OwnerDhcp,
       "cie1000IpStatusRoutesIpv6OwnerDynamic": cie1000IpStatusRoutesIpv6OwnerDynamic,
       "cie1000IpControl": cie1000IpControl,
       "cie1000IpControlGlobals": cie1000IpControlGlobals,
       "cie1000IpControlGlobalsIpv4NeighbourTableClear": cie1000IpControlGlobalsIpv4NeighbourTableClear,
       "cie1000IpControlGlobalsIpv6NeighbourTableClear": cie1000IpControlGlobalsIpv6NeighbourTableClear,
       "cie1000IpControlGlobalsIpv4SystemStatisticsClear": cie1000IpControlGlobalsIpv4SystemStatisticsClear,
       "cie1000IpControlGlobalsIpv6SystemStatisticsClear": cie1000IpControlGlobalsIpv6SystemStatisticsClear,
       "cie1000IpControlInterface": cie1000IpControlInterface,
       "cie1000IpControlInterfaceDhcpClientTable": cie1000IpControlInterfaceDhcpClientTable,
       "cie1000IpControlInterfaceDhcpClientEntry": cie1000IpControlInterfaceDhcpClientEntry,
       "cie1000IpControlInterfaceDhcpClientIfIndex": cie1000IpControlInterfaceDhcpClientIfIndex,
       "cie1000IpControlInterfaceDhcpClientRestart": cie1000IpControlInterfaceDhcpClientRestart,
       "cie1000IpStatistics": cie1000IpStatistics,
       "cie1000IpStatisticsGlobals": cie1000IpStatisticsGlobals,
       "cie1000IpStatisticsGlobalsIpv4": cie1000IpStatisticsGlobalsIpv4,
       "cie1000IpStatisticsGlobalsIpv4InReceives": cie1000IpStatisticsGlobalsIpv4InReceives,
       "cie1000IpStatisticsGlobalsIpv4HCInReceives": cie1000IpStatisticsGlobalsIpv4HCInReceives,
       "cie1000IpStatisticsGlobalsIpv4InOctets": cie1000IpStatisticsGlobalsIpv4InOctets,
       "cie1000IpStatisticsGlobalsIpv4HCInOctets": cie1000IpStatisticsGlobalsIpv4HCInOctets,
       "cie1000IpStatisticsGlobalsIpv4InHdrErrors": cie1000IpStatisticsGlobalsIpv4InHdrErrors,
       "cie1000IpStatisticsGlobalsIpv4InNoRoutes": cie1000IpStatisticsGlobalsIpv4InNoRoutes,
       "cie1000IpStatisticsGlobalsIpv4InAddrErrors": cie1000IpStatisticsGlobalsIpv4InAddrErrors,
       "cie1000IpStatisticsGlobalsIpv4InUnknownProtos": cie1000IpStatisticsGlobalsIpv4InUnknownProtos,
       "cie1000IpStatisticsGlobalsIpv4InTruncatedPkts": cie1000IpStatisticsGlobalsIpv4InTruncatedPkts,
       "cie1000IpStatisticsGlobalsIpv4InForwDatagrams": cie1000IpStatisticsGlobalsIpv4InForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams": cie1000IpStatisticsGlobalsIpv4HCInForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv4ReasmReqds": cie1000IpStatisticsGlobalsIpv4ReasmReqds,
       "cie1000IpStatisticsGlobalsIpv4ReasmOKs": cie1000IpStatisticsGlobalsIpv4ReasmOKs,
       "cie1000IpStatisticsGlobalsIpv4ReasmFails": cie1000IpStatisticsGlobalsIpv4ReasmFails,
       "cie1000IpStatisticsGlobalsIpv4InDiscards": cie1000IpStatisticsGlobalsIpv4InDiscards,
       "cie1000IpStatisticsGlobalsIpv4InDelivers": cie1000IpStatisticsGlobalsIpv4InDelivers,
       "cie1000IpStatisticsGlobalsIpv4HCInDelivers": cie1000IpStatisticsGlobalsIpv4HCInDelivers,
       "cie1000IpStatisticsGlobalsIpv4OutRequests": cie1000IpStatisticsGlobalsIpv4OutRequests,
       "cie1000IpStatisticsGlobalsIpv4HCOutRequests": cie1000IpStatisticsGlobalsIpv4HCOutRequests,
       "cie1000IpStatisticsGlobalsIpv4OutNoRoutes": cie1000IpStatisticsGlobalsIpv4OutNoRoutes,
       "cie1000IpStatisticsGlobalsIpv4OutForwDatagrams": cie1000IpStatisticsGlobalsIpv4OutForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams": cie1000IpStatisticsGlobalsIpv4HCOutForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv4OutDiscards": cie1000IpStatisticsGlobalsIpv4OutDiscards,
       "cie1000IpStatisticsGlobalsIpv4OutFragReqds": cie1000IpStatisticsGlobalsIpv4OutFragReqds,
       "cie1000IpStatisticsGlobalsIpv4OutFragOKs": cie1000IpStatisticsGlobalsIpv4OutFragOKs,
       "cie1000IpStatisticsGlobalsIpv4OutFragFails": cie1000IpStatisticsGlobalsIpv4OutFragFails,
       "cie1000IpStatisticsGlobalsIpv4OutFragCreates": cie1000IpStatisticsGlobalsIpv4OutFragCreates,
       "cie1000IpStatisticsGlobalsIpv4OutTransmits": cie1000IpStatisticsGlobalsIpv4OutTransmits,
       "cie1000IpStatisticsGlobalsIpv4HCOutTransmits": cie1000IpStatisticsGlobalsIpv4HCOutTransmits,
       "cie1000IpStatisticsGlobalsIpv4OutOctets": cie1000IpStatisticsGlobalsIpv4OutOctets,
       "cie1000IpStatisticsGlobalsIpv4HCOutOctets": cie1000IpStatisticsGlobalsIpv4HCOutOctets,
       "cie1000IpStatisticsGlobalsIpv4InMcastPkts": cie1000IpStatisticsGlobalsIpv4InMcastPkts,
       "cie1000IpStatisticsGlobalsIpv4HCInMcastPkts": cie1000IpStatisticsGlobalsIpv4HCInMcastPkts,
       "cie1000IpStatisticsGlobalsIpv4InMcastOctets": cie1000IpStatisticsGlobalsIpv4InMcastOctets,
       "cie1000IpStatisticsGlobalsIpv4HCInMcastOctets": cie1000IpStatisticsGlobalsIpv4HCInMcastOctets,
       "cie1000IpStatisticsGlobalsIpv4OutMcastPkts": cie1000IpStatisticsGlobalsIpv4OutMcastPkts,
       "cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts": cie1000IpStatisticsGlobalsIpv4HCOutMcastPkts,
       "cie1000IpStatisticsGlobalsIpv4OutMcastOctets": cie1000IpStatisticsGlobalsIpv4OutMcastOctets,
       "cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets": cie1000IpStatisticsGlobalsIpv4HCOutMcastOctets,
       "cie1000IpStatisticsGlobalsIpv4InBcastPkts": cie1000IpStatisticsGlobalsIpv4InBcastPkts,
       "cie1000IpStatisticsGlobalsIpv4HCInBcastPkts": cie1000IpStatisticsGlobalsIpv4HCInBcastPkts,
       "cie1000IpStatisticsGlobalsIpv4OutBcastPkts": cie1000IpStatisticsGlobalsIpv4OutBcastPkts,
       "cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts": cie1000IpStatisticsGlobalsIpv4HCOutBcastPkts,
       "cie1000IpStatisticsGlobalsIpv4DiscontinuityTime": cie1000IpStatisticsGlobalsIpv4DiscontinuityTime,
       "cie1000IpStatisticsGlobalsIpv4RefreshRate": cie1000IpStatisticsGlobalsIpv4RefreshRate,
       "cie1000IpStatisticsGlobalsIpv6": cie1000IpStatisticsGlobalsIpv6,
       "cie1000IpStatisticsGlobalsIpv6InReceives": cie1000IpStatisticsGlobalsIpv6InReceives,
       "cie1000IpStatisticsGlobalsIpv6HCInReceives": cie1000IpStatisticsGlobalsIpv6HCInReceives,
       "cie1000IpStatisticsGlobalsIpv6InOctets": cie1000IpStatisticsGlobalsIpv6InOctets,
       "cie1000IpStatisticsGlobalsIpv6HCInOctets": cie1000IpStatisticsGlobalsIpv6HCInOctets,
       "cie1000IpStatisticsGlobalsIpv6InHdrErrors": cie1000IpStatisticsGlobalsIpv6InHdrErrors,
       "cie1000IpStatisticsGlobalsIpv6InNoRoutes": cie1000IpStatisticsGlobalsIpv6InNoRoutes,
       "cie1000IpStatisticsGlobalsIpv6InAddrErrors": cie1000IpStatisticsGlobalsIpv6InAddrErrors,
       "cie1000IpStatisticsGlobalsIpv6InUnknownProtos": cie1000IpStatisticsGlobalsIpv6InUnknownProtos,
       "cie1000IpStatisticsGlobalsIpv6InTruncatedPkts": cie1000IpStatisticsGlobalsIpv6InTruncatedPkts,
       "cie1000IpStatisticsGlobalsIpv6InForwDatagrams": cie1000IpStatisticsGlobalsIpv6InForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams": cie1000IpStatisticsGlobalsIpv6HCInForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv6ReasmReqds": cie1000IpStatisticsGlobalsIpv6ReasmReqds,
       "cie1000IpStatisticsGlobalsIpv6ReasmOKs": cie1000IpStatisticsGlobalsIpv6ReasmOKs,
       "cie1000IpStatisticsGlobalsIpv6ReasmFails": cie1000IpStatisticsGlobalsIpv6ReasmFails,
       "cie1000IpStatisticsGlobalsIpv6InDiscards": cie1000IpStatisticsGlobalsIpv6InDiscards,
       "cie1000IpStatisticsGlobalsIpv6InDelivers": cie1000IpStatisticsGlobalsIpv6InDelivers,
       "cie1000IpStatisticsGlobalsIpv6HCInDelivers": cie1000IpStatisticsGlobalsIpv6HCInDelivers,
       "cie1000IpStatisticsGlobalsIpv6OutRequests": cie1000IpStatisticsGlobalsIpv6OutRequests,
       "cie1000IpStatisticsGlobalsIpv6HCOutRequests": cie1000IpStatisticsGlobalsIpv6HCOutRequests,
       "cie1000IpStatisticsGlobalsIpv6OutNoRoutes": cie1000IpStatisticsGlobalsIpv6OutNoRoutes,
       "cie1000IpStatisticsGlobalsIpv6OutForwDatagrams": cie1000IpStatisticsGlobalsIpv6OutForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams": cie1000IpStatisticsGlobalsIpv6HCOutForwDatagrams,
       "cie1000IpStatisticsGlobalsIpv6OutDiscards": cie1000IpStatisticsGlobalsIpv6OutDiscards,
       "cie1000IpStatisticsGlobalsIpv6OutFragReqds": cie1000IpStatisticsGlobalsIpv6OutFragReqds,
       "cie1000IpStatisticsGlobalsIpv6OutFragOKs": cie1000IpStatisticsGlobalsIpv6OutFragOKs,
       "cie1000IpStatisticsGlobalsIpv6OutFragFails": cie1000IpStatisticsGlobalsIpv6OutFragFails,
       "cie1000IpStatisticsGlobalsIpv6OutFragCreates": cie1000IpStatisticsGlobalsIpv6OutFragCreates,
       "cie1000IpStatisticsGlobalsIpv6OutTransmits": cie1000IpStatisticsGlobalsIpv6OutTransmits,
       "cie1000IpStatisticsGlobalsIpv6HCOutTransmits": cie1000IpStatisticsGlobalsIpv6HCOutTransmits,
       "cie1000IpStatisticsGlobalsIpv6OutOctets": cie1000IpStatisticsGlobalsIpv6OutOctets,
       "cie1000IpStatisticsGlobalsIpv6HCOutOctets": cie1000IpStatisticsGlobalsIpv6HCOutOctets,
       "cie1000IpStatisticsGlobalsIpv6InMcastPkts": cie1000IpStatisticsGlobalsIpv6InMcastPkts,
       "cie1000IpStatisticsGlobalsIpv6HCInMcastPkts": cie1000IpStatisticsGlobalsIpv6HCInMcastPkts,
       "cie1000IpStatisticsGlobalsIpv6InMcastOctets": cie1000IpStatisticsGlobalsIpv6InMcastOctets,
       "cie1000IpStatisticsGlobalsIpv6HCInMcastOctets": cie1000IpStatisticsGlobalsIpv6HCInMcastOctets,
       "cie1000IpStatisticsGlobalsIpv6OutMcastPkts": cie1000IpStatisticsGlobalsIpv6OutMcastPkts,
       "cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts": cie1000IpStatisticsGlobalsIpv6HCOutMcastPkts,
       "cie1000IpStatisticsGlobalsIpv6OutMcastOctets": cie1000IpStatisticsGlobalsIpv6OutMcastOctets,
       "cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets": cie1000IpStatisticsGlobalsIpv6HCOutMcastOctets,
       "cie1000IpStatisticsGlobalsIpv6InBcastPkts": cie1000IpStatisticsGlobalsIpv6InBcastPkts,
       "cie1000IpStatisticsGlobalsIpv6HCInBcastPkts": cie1000IpStatisticsGlobalsIpv6HCInBcastPkts,
       "cie1000IpStatisticsGlobalsIpv6OutBcastPkts": cie1000IpStatisticsGlobalsIpv6OutBcastPkts,
       "cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts": cie1000IpStatisticsGlobalsIpv6HCOutBcastPkts,
       "cie1000IpStatisticsGlobalsIpv6DiscontinuityTime": cie1000IpStatisticsGlobalsIpv6DiscontinuityTime,
       "cie1000IpStatisticsGlobalsIpv6RefreshRate": cie1000IpStatisticsGlobalsIpv6RefreshRate,
       "cie1000IpStatisticsInterfaces": cie1000IpStatisticsInterfaces,
       "cie1000IpStatisticsInterfacesLinkTable": cie1000IpStatisticsInterfacesLinkTable,
       "cie1000IpStatisticsInterfacesLinkEntry": cie1000IpStatisticsInterfacesLinkEntry,
       "cie1000IpStatisticsInterfacesLinkIfIndex": cie1000IpStatisticsInterfacesLinkIfIndex,
       "cie1000IpStatisticsInterfacesLinkInPackets": cie1000IpStatisticsInterfacesLinkInPackets,
       "cie1000IpStatisticsInterfacesLinkOutPackets": cie1000IpStatisticsInterfacesLinkOutPackets,
       "cie1000IpStatisticsInterfacesLinkInBytes": cie1000IpStatisticsInterfacesLinkInBytes,
       "cie1000IpStatisticsInterfacesLinkOutBytes": cie1000IpStatisticsInterfacesLinkOutBytes,
       "cie1000IpStatisticsInterfacesLinkInMulticasts": cie1000IpStatisticsInterfacesLinkInMulticasts,
       "cie1000IpStatisticsInterfacesLinkOutMulticasts": cie1000IpStatisticsInterfacesLinkOutMulticasts,
       "cie1000IpStatisticsInterfacesLinkInBroadcasts": cie1000IpStatisticsInterfacesLinkInBroadcasts,
       "cie1000IpStatisticsInterfacesLinkOutBroadcasts": cie1000IpStatisticsInterfacesLinkOutBroadcasts,
       "cie1000IpStatisticsInterfacesIpv4Table": cie1000IpStatisticsInterfacesIpv4Table,
       "cie1000IpStatisticsInterfacesIpv4Entry": cie1000IpStatisticsInterfacesIpv4Entry,
       "cie1000IpStatisticsInterfacesIpv4IfIndex": cie1000IpStatisticsInterfacesIpv4IfIndex,
       "cie1000IpStatisticsInterfacesIpv4InReceives": cie1000IpStatisticsInterfacesIpv4InReceives,
       "cie1000IpStatisticsInterfacesIpv4HCInReceives": cie1000IpStatisticsInterfacesIpv4HCInReceives,
       "cie1000IpStatisticsInterfacesIpv4InOctets": cie1000IpStatisticsInterfacesIpv4InOctets,
       "cie1000IpStatisticsInterfacesIpv4HCInOctets": cie1000IpStatisticsInterfacesIpv4HCInOctets,
       "cie1000IpStatisticsInterfacesIpv4InHdrErrors": cie1000IpStatisticsInterfacesIpv4InHdrErrors,
       "cie1000IpStatisticsInterfacesIpv4InNoRoutes": cie1000IpStatisticsInterfacesIpv4InNoRoutes,
       "cie1000IpStatisticsInterfacesIpv4InAddrErrors": cie1000IpStatisticsInterfacesIpv4InAddrErrors,
       "cie1000IpStatisticsInterfacesIpv4InUnknownProtos": cie1000IpStatisticsInterfacesIpv4InUnknownProtos,
       "cie1000IpStatisticsInterfacesIpv4InTruncatedPkts": cie1000IpStatisticsInterfacesIpv4InTruncatedPkts,
       "cie1000IpStatisticsInterfacesIpv4InForwDatagrams": cie1000IpStatisticsInterfacesIpv4InForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams": cie1000IpStatisticsInterfacesIpv4HCInForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv4ReasmReqds": cie1000IpStatisticsInterfacesIpv4ReasmReqds,
       "cie1000IpStatisticsInterfacesIpv4ReasmOKs": cie1000IpStatisticsInterfacesIpv4ReasmOKs,
       "cie1000IpStatisticsInterfacesIpv4ReasmFails": cie1000IpStatisticsInterfacesIpv4ReasmFails,
       "cie1000IpStatisticsInterfacesIpv4InDiscards": cie1000IpStatisticsInterfacesIpv4InDiscards,
       "cie1000IpStatisticsInterfacesIpv4InDelivers": cie1000IpStatisticsInterfacesIpv4InDelivers,
       "cie1000IpStatisticsInterfacesIpv4HCInDelivers": cie1000IpStatisticsInterfacesIpv4HCInDelivers,
       "cie1000IpStatisticsInterfacesIpv4OutRequests": cie1000IpStatisticsInterfacesIpv4OutRequests,
       "cie1000IpStatisticsInterfacesIpv4HCOutRequests": cie1000IpStatisticsInterfacesIpv4HCOutRequests,
       "cie1000IpStatisticsInterfacesIpv4OutNoRoutes": cie1000IpStatisticsInterfacesIpv4OutNoRoutes,
       "cie1000IpStatisticsInterfacesIpv4OutForwDatagrams": cie1000IpStatisticsInterfacesIpv4OutForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams": cie1000IpStatisticsInterfacesIpv4HCOutForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv4OutDiscards": cie1000IpStatisticsInterfacesIpv4OutDiscards,
       "cie1000IpStatisticsInterfacesIpv4OutFragReqds": cie1000IpStatisticsInterfacesIpv4OutFragReqds,
       "cie1000IpStatisticsInterfacesIpv4OutFragOKs": cie1000IpStatisticsInterfacesIpv4OutFragOKs,
       "cie1000IpStatisticsInterfacesIpv4OutFragFails": cie1000IpStatisticsInterfacesIpv4OutFragFails,
       "cie1000IpStatisticsInterfacesIpv4OutFragCreates": cie1000IpStatisticsInterfacesIpv4OutFragCreates,
       "cie1000IpStatisticsInterfacesIpv4OutTransmits": cie1000IpStatisticsInterfacesIpv4OutTransmits,
       "cie1000IpStatisticsInterfacesIpv4HCOutTransmits": cie1000IpStatisticsInterfacesIpv4HCOutTransmits,
       "cie1000IpStatisticsInterfacesIpv4OutOctets": cie1000IpStatisticsInterfacesIpv4OutOctets,
       "cie1000IpStatisticsInterfacesIpv4HCOutOctets": cie1000IpStatisticsInterfacesIpv4HCOutOctets,
       "cie1000IpStatisticsInterfacesIpv4InMcastPkts": cie1000IpStatisticsInterfacesIpv4InMcastPkts,
       "cie1000IpStatisticsInterfacesIpv4HCInMcastPkts": cie1000IpStatisticsInterfacesIpv4HCInMcastPkts,
       "cie1000IpStatisticsInterfacesIpv4InMcastOctets": cie1000IpStatisticsInterfacesIpv4InMcastOctets,
       "cie1000IpStatisticsInterfacesIpv4HCInMcastOctets": cie1000IpStatisticsInterfacesIpv4HCInMcastOctets,
       "cie1000IpStatisticsInterfacesIpv4OutMcastPkts": cie1000IpStatisticsInterfacesIpv4OutMcastPkts,
       "cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts": cie1000IpStatisticsInterfacesIpv4HCOutMcastPkts,
       "cie1000IpStatisticsInterfacesIpv4OutMcastOctets": cie1000IpStatisticsInterfacesIpv4OutMcastOctets,
       "cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets": cie1000IpStatisticsInterfacesIpv4HCOutMcastOctets,
       "cie1000IpStatisticsInterfacesIpv4InBcastPkts": cie1000IpStatisticsInterfacesIpv4InBcastPkts,
       "cie1000IpStatisticsInterfacesIpv4HCInBcastPkts": cie1000IpStatisticsInterfacesIpv4HCInBcastPkts,
       "cie1000IpStatisticsInterfacesIpv4OutBcastPkts": cie1000IpStatisticsInterfacesIpv4OutBcastPkts,
       "cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts": cie1000IpStatisticsInterfacesIpv4HCOutBcastPkts,
       "cie1000IpStatisticsInterfacesIpv4DiscontinuityTime": cie1000IpStatisticsInterfacesIpv4DiscontinuityTime,
       "cie1000IpStatisticsInterfacesIpv4RefreshRate": cie1000IpStatisticsInterfacesIpv4RefreshRate,
       "cie1000IpStatisticsInterfacesIpv6Table": cie1000IpStatisticsInterfacesIpv6Table,
       "cie1000IpStatisticsInterfacesIpv6Entry": cie1000IpStatisticsInterfacesIpv6Entry,
       "cie1000IpStatisticsInterfacesIpv6IfIndex": cie1000IpStatisticsInterfacesIpv6IfIndex,
       "cie1000IpStatisticsInterfacesIpv6InReceives": cie1000IpStatisticsInterfacesIpv6InReceives,
       "cie1000IpStatisticsInterfacesIpv6HCInReceives": cie1000IpStatisticsInterfacesIpv6HCInReceives,
       "cie1000IpStatisticsInterfacesIpv6InOctets": cie1000IpStatisticsInterfacesIpv6InOctets,
       "cie1000IpStatisticsInterfacesIpv6HCInOctets": cie1000IpStatisticsInterfacesIpv6HCInOctets,
       "cie1000IpStatisticsInterfacesIpv6InHdrErrors": cie1000IpStatisticsInterfacesIpv6InHdrErrors,
       "cie1000IpStatisticsInterfacesIpv6InNoRoutes": cie1000IpStatisticsInterfacesIpv6InNoRoutes,
       "cie1000IpStatisticsInterfacesIpv6InAddrErrors": cie1000IpStatisticsInterfacesIpv6InAddrErrors,
       "cie1000IpStatisticsInterfacesIpv6InUnknownProtos": cie1000IpStatisticsInterfacesIpv6InUnknownProtos,
       "cie1000IpStatisticsInterfacesIpv6InTruncatedPkts": cie1000IpStatisticsInterfacesIpv6InTruncatedPkts,
       "cie1000IpStatisticsInterfacesIpv6InForwDatagrams": cie1000IpStatisticsInterfacesIpv6InForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams": cie1000IpStatisticsInterfacesIpv6HCInForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv6ReasmReqds": cie1000IpStatisticsInterfacesIpv6ReasmReqds,
       "cie1000IpStatisticsInterfacesIpv6ReasmOKs": cie1000IpStatisticsInterfacesIpv6ReasmOKs,
       "cie1000IpStatisticsInterfacesIpv6ReasmFails": cie1000IpStatisticsInterfacesIpv6ReasmFails,
       "cie1000IpStatisticsInterfacesIpv6InDiscards": cie1000IpStatisticsInterfacesIpv6InDiscards,
       "cie1000IpStatisticsInterfacesIpv6InDelivers": cie1000IpStatisticsInterfacesIpv6InDelivers,
       "cie1000IpStatisticsInterfacesIpv6HCInDelivers": cie1000IpStatisticsInterfacesIpv6HCInDelivers,
       "cie1000IpStatisticsInterfacesIpv6OutRequests": cie1000IpStatisticsInterfacesIpv6OutRequests,
       "cie1000IpStatisticsInterfacesIpv6HCOutRequests": cie1000IpStatisticsInterfacesIpv6HCOutRequests,
       "cie1000IpStatisticsInterfacesIpv6OutNoRoutes": cie1000IpStatisticsInterfacesIpv6OutNoRoutes,
       "cie1000IpStatisticsInterfacesIpv6OutForwDatagrams": cie1000IpStatisticsInterfacesIpv6OutForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams": cie1000IpStatisticsInterfacesIpv6HCOutForwDatagrams,
       "cie1000IpStatisticsInterfacesIpv6OutDiscards": cie1000IpStatisticsInterfacesIpv6OutDiscards,
       "cie1000IpStatisticsInterfacesIpv6OutFragReqds": cie1000IpStatisticsInterfacesIpv6OutFragReqds,
       "cie1000IpStatisticsInterfacesIpv6OutFragOKs": cie1000IpStatisticsInterfacesIpv6OutFragOKs,
       "cie1000IpStatisticsInterfacesIpv6OutFragFails": cie1000IpStatisticsInterfacesIpv6OutFragFails,
       "cie1000IpStatisticsInterfacesIpv6OutFragCreates": cie1000IpStatisticsInterfacesIpv6OutFragCreates,
       "cie1000IpStatisticsInterfacesIpv6OutTransmits": cie1000IpStatisticsInterfacesIpv6OutTransmits,
       "cie1000IpStatisticsInterfacesIpv6HCOutTransmits": cie1000IpStatisticsInterfacesIpv6HCOutTransmits,
       "cie1000IpStatisticsInterfacesIpv6OutOctets": cie1000IpStatisticsInterfacesIpv6OutOctets,
       "cie1000IpStatisticsInterfacesIpv6HCOutOctets": cie1000IpStatisticsInterfacesIpv6HCOutOctets,
       "cie1000IpStatisticsInterfacesIpv6InMcastPkts": cie1000IpStatisticsInterfacesIpv6InMcastPkts,
       "cie1000IpStatisticsInterfacesIpv6HCInMcastPkts": cie1000IpStatisticsInterfacesIpv6HCInMcastPkts,
       "cie1000IpStatisticsInterfacesIpv6InMcastOctets": cie1000IpStatisticsInterfacesIpv6InMcastOctets,
       "cie1000IpStatisticsInterfacesIpv6HCInMcastOctets": cie1000IpStatisticsInterfacesIpv6HCInMcastOctets,
       "cie1000IpStatisticsInterfacesIpv6OutMcastPkts": cie1000IpStatisticsInterfacesIpv6OutMcastPkts,
       "cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts": cie1000IpStatisticsInterfacesIpv6HCOutMcastPkts,
       "cie1000IpStatisticsInterfacesIpv6OutMcastOctets": cie1000IpStatisticsInterfacesIpv6OutMcastOctets,
       "cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets": cie1000IpStatisticsInterfacesIpv6HCOutMcastOctets,
       "cie1000IpStatisticsInterfacesIpv6InBcastPkts": cie1000IpStatisticsInterfacesIpv6InBcastPkts,
       "cie1000IpStatisticsInterfacesIpv6HCInBcastPkts": cie1000IpStatisticsInterfacesIpv6HCInBcastPkts,
       "cie1000IpStatisticsInterfacesIpv6OutBcastPkts": cie1000IpStatisticsInterfacesIpv6OutBcastPkts,
       "cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts": cie1000IpStatisticsInterfacesIpv6HCOutBcastPkts,
       "cie1000IpStatisticsInterfacesIpv6DiscontinuityTime": cie1000IpStatisticsInterfacesIpv6DiscontinuityTime,
       "cie1000IpStatisticsInterfacesIpv6RefreshRate": cie1000IpStatisticsInterfacesIpv6RefreshRate,
       "cie1000IpTrap": cie1000IpTrap,
       "cie1000IpTrapInterfacesLinkAdd": cie1000IpTrapInterfacesLinkAdd,
       "cie1000IpTrapInterfacesLinkMod": cie1000IpTrapInterfacesLinkMod,
       "cie1000IpTrapInterfacesLinkDel": cie1000IpTrapInterfacesLinkDel,
       "cie1000IpMibConformance": cie1000IpMibConformance,
       "cie1000IpMibCompliances": cie1000IpMibCompliances,
       "cie1000IpMibCompliance": cie1000IpMibCompliance,
       "cie1000IpMibGroups": cie1000IpMibGroups,
       "cie1000IpCapabilitiesInfoGroup": cie1000IpCapabilitiesInfoGroup,
       "cie1000IpConfigGlobalsMainInfoGroup": cie1000IpConfigGlobalsMainInfoGroup,
       "cie1000IpConfigInterfacesTableInfoGroup": cie1000IpConfigInterfacesTableInfoGroup,
       "cie1000IpConfigInterfacesTableRowEditorInfoGroup": cie1000IpConfigInterfacesTableRowEditorInfoGroup,
       "cie1000IpConfigInterfacesIpv4TableInfoGroup": cie1000IpConfigInterfacesIpv4TableInfoGroup,
       "cie1000IpConfigInterfacesIpv6TableInfoGroup": cie1000IpConfigInterfacesIpv6TableInfoGroup,
       "cie1000IpConfigRoutesIpv4TableInfoGroup": cie1000IpConfigRoutesIpv4TableInfoGroup,
       "cie1000IpConfigRoutesIpv4RowEditorInfoGroup": cie1000IpConfigRoutesIpv4RowEditorInfoGroup,
       "cie1000IpConfigRoutesIpv6TableInfoGroup": cie1000IpConfigRoutesIpv6TableInfoGroup,
       "cie1000IpConfigRoutesIpv6RowEditorInfoGroup": cie1000IpConfigRoutesIpv6RowEditorInfoGroup,
       "cie1000IpStatusGlobalsIpv4NeighbourInfoGroup": cie1000IpStatusGlobalsIpv4NeighbourInfoGroup,
       "cie1000IpStatusGlobalsIpv6NeighbourInfoGroup": cie1000IpStatusGlobalsIpv6NeighbourInfoGroup,
       "cie1000IpStatusInterfacesLinkInfoGroup": cie1000IpStatusInterfacesLinkInfoGroup,
       "cie1000IpStatusInterfacesIpv4InfoGroup": cie1000IpStatusInterfacesIpv4InfoGroup,
       "cie1000IpStatusInterfacesDhcpClientV4InfoGroup": cie1000IpStatusInterfacesDhcpClientV4InfoGroup,
       "cie1000IpStatusInterfacesIpv6InfoGroup": cie1000IpStatusInterfacesIpv6InfoGroup,
       "cie1000IpStatusRoutesIpv4InfoGroup": cie1000IpStatusRoutesIpv4InfoGroup,
       "cie1000IpStatusRoutesIpv6InfoGroup": cie1000IpStatusRoutesIpv6InfoGroup,
       "cie1000IpControlGlobalsInfoGroup": cie1000IpControlGlobalsInfoGroup,
       "cie1000IpControlInterfaceDhcpClientInfoGroup": cie1000IpControlInterfaceDhcpClientInfoGroup,
       "cie1000IpStatisticsGlobalsIpv4InfoGroup": cie1000IpStatisticsGlobalsIpv4InfoGroup,
       "cie1000IpStatisticsGlobalsIpv6InfoGroup": cie1000IpStatisticsGlobalsIpv6InfoGroup,
       "cie1000IpStatisticsInterfacesLinkInfoGroup": cie1000IpStatisticsInterfacesLinkInfoGroup,
       "cie1000IpStatisticsInterfacesIpv4InfoGroup": cie1000IpStatisticsInterfacesIpv4InfoGroup,
       "cie1000IpStatisticsInterfacesIpv6InfoGroup": cie1000IpStatisticsInterfacesIpv6InfoGroup,
       "cie1000IpTrapInterfacesLinkAddInfoGroup": cie1000IpTrapInterfacesLinkAddInfoGroup,
       "cie1000IpTrapInterfacesLinkModInfoGroup": cie1000IpTrapInterfacesLinkModInfoGroup,
       "cie1000IpTrapInterfacesLinkDelInfoGroup": cie1000IpTrapInterfacesLinkDelInfoGroup}
)
