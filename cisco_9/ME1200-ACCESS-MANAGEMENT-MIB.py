# SNMP MIB module (ME1200-ACCESS-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-ACCESS-MANAGEMENT-MIB.mib
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

(ME1200RowEditorState,
 ME1200Unsigned16) = mibBuilder.importSymbols(
    "ME1200-TC",
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200AccessManagementMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51)
)
if mibBuilder.loadTexts:
    me1200AccessManagementMib.setRevisions(
        ("2014-02-18 00:00",
         "2014-01-29 00:00",
         "2013-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200AccessManagementMIBObjects_ObjectIdentity = ObjectIdentity
me1200AccessManagementMIBObjects = _Me1200AccessManagementMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1)
)
_Me1200AccessManagementConfig_ObjectIdentity = ObjectIdentity
me1200AccessManagementConfig = _Me1200AccessManagementConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2)
)
_Me1200AccessManagementGlobals_ObjectIdentity = ObjectIdentity
me1200AccessManagementGlobals = _Me1200AccessManagementGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 1)
)
_Me1200AccessManagementGlobalsAdminState_Type = TruthValue
_Me1200AccessManagementGlobalsAdminState_Object = MibScalar
me1200AccessManagementGlobalsAdminState = _Me1200AccessManagementGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 1, 1),
    _Me1200AccessManagementGlobalsAdminState_Type()
)
me1200AccessManagementGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementGlobalsAdminState.setStatus("current")
_Me1200AccessManagementIpv4Table_Object = MibTable
me1200AccessManagementIpv4Table = _Me1200AccessManagementIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4Table.setStatus("current")
_Me1200AccessManagementIpv4Entry_Object = MibTableRow
me1200AccessManagementIpv4Entry = _Me1200AccessManagementIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1)
)
me1200AccessManagementIpv4Entry.setIndexNames(
    (0, "ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4AccessIndex"),
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4Entry.setStatus("current")


class _Me1200AccessManagementIpv4AccessIndex_Type(Integer32):
    """Custom type me1200AccessManagementIpv4AccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200AccessManagementIpv4AccessIndex_Type.__name__ = "Integer32"
_Me1200AccessManagementIpv4AccessIndex_Object = MibTableColumn
me1200AccessManagementIpv4AccessIndex = _Me1200AccessManagementIpv4AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 1),
    _Me1200AccessManagementIpv4AccessIndex_Type()
)
me1200AccessManagementIpv4AccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4AccessIndex.setStatus("current")
_Me1200AccessManagementIpv4VlanId_Type = ME1200Unsigned16
_Me1200AccessManagementIpv4VlanId_Object = MibTableColumn
me1200AccessManagementIpv4VlanId = _Me1200AccessManagementIpv4VlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 2),
    _Me1200AccessManagementIpv4VlanId_Type()
)
me1200AccessManagementIpv4VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4VlanId.setStatus("current")
_Me1200AccessManagementIpv4StartAddress_Type = IpAddress
_Me1200AccessManagementIpv4StartAddress_Object = MibTableColumn
me1200AccessManagementIpv4StartAddress = _Me1200AccessManagementIpv4StartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 3),
    _Me1200AccessManagementIpv4StartAddress_Type()
)
me1200AccessManagementIpv4StartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4StartAddress.setStatus("current")
_Me1200AccessManagementIpv4EndAddress_Type = IpAddress
_Me1200AccessManagementIpv4EndAddress_Object = MibTableColumn
me1200AccessManagementIpv4EndAddress = _Me1200AccessManagementIpv4EndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 4),
    _Me1200AccessManagementIpv4EndAddress_Type()
)
me1200AccessManagementIpv4EndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4EndAddress.setStatus("current")
_Me1200AccessManagementIpv4WebServices_Type = TruthValue
_Me1200AccessManagementIpv4WebServices_Object = MibTableColumn
me1200AccessManagementIpv4WebServices = _Me1200AccessManagementIpv4WebServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 5),
    _Me1200AccessManagementIpv4WebServices_Type()
)
me1200AccessManagementIpv4WebServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4WebServices.setStatus("current")
_Me1200AccessManagementIpv4SnmpServices_Type = TruthValue
_Me1200AccessManagementIpv4SnmpServices_Object = MibTableColumn
me1200AccessManagementIpv4SnmpServices = _Me1200AccessManagementIpv4SnmpServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 6),
    _Me1200AccessManagementIpv4SnmpServices_Type()
)
me1200AccessManagementIpv4SnmpServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4SnmpServices.setStatus("current")
_Me1200AccessManagementIpv4TelnetServices_Type = TruthValue
_Me1200AccessManagementIpv4TelnetServices_Object = MibTableColumn
me1200AccessManagementIpv4TelnetServices = _Me1200AccessManagementIpv4TelnetServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 7),
    _Me1200AccessManagementIpv4TelnetServices_Type()
)
me1200AccessManagementIpv4TelnetServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TelnetServices.setStatus("current")
_Me1200AccessManagementIpv4Action_Type = ME1200RowEditorState
_Me1200AccessManagementIpv4Action_Object = MibTableColumn
me1200AccessManagementIpv4Action = _Me1200AccessManagementIpv4Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 2, 1, 100),
    _Me1200AccessManagementIpv4Action_Type()
)
me1200AccessManagementIpv4Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4Action.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditor_ObjectIdentity = ObjectIdentity
me1200AccessManagementIpv4TableRowEditor = _Me1200AccessManagementIpv4TableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3)
)


class _Me1200AccessManagementIpv4TableRowEditorAccessIndex_Type(Integer32):
    """Custom type me1200AccessManagementIpv4TableRowEditorAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200AccessManagementIpv4TableRowEditorAccessIndex_Type.__name__ = "Integer32"
_Me1200AccessManagementIpv4TableRowEditorAccessIndex_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorAccessIndex = _Me1200AccessManagementIpv4TableRowEditorAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 1),
    _Me1200AccessManagementIpv4TableRowEditorAccessIndex_Type()
)
me1200AccessManagementIpv4TableRowEditorAccessIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorAccessIndex.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorVlanId_Type = ME1200Unsigned16
_Me1200AccessManagementIpv4TableRowEditorVlanId_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorVlanId = _Me1200AccessManagementIpv4TableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 2),
    _Me1200AccessManagementIpv4TableRowEditorVlanId_Type()
)
me1200AccessManagementIpv4TableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorVlanId.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorStartAddress_Type = IpAddress
_Me1200AccessManagementIpv4TableRowEditorStartAddress_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorStartAddress = _Me1200AccessManagementIpv4TableRowEditorStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 3),
    _Me1200AccessManagementIpv4TableRowEditorStartAddress_Type()
)
me1200AccessManagementIpv4TableRowEditorStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorStartAddress.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorEndAddress_Type = IpAddress
_Me1200AccessManagementIpv4TableRowEditorEndAddress_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorEndAddress = _Me1200AccessManagementIpv4TableRowEditorEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 4),
    _Me1200AccessManagementIpv4TableRowEditorEndAddress_Type()
)
me1200AccessManagementIpv4TableRowEditorEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorEndAddress.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorWebServices_Type = TruthValue
_Me1200AccessManagementIpv4TableRowEditorWebServices_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorWebServices = _Me1200AccessManagementIpv4TableRowEditorWebServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 5),
    _Me1200AccessManagementIpv4TableRowEditorWebServices_Type()
)
me1200AccessManagementIpv4TableRowEditorWebServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorWebServices.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorSnmpServices_Type = TruthValue
_Me1200AccessManagementIpv4TableRowEditorSnmpServices_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorSnmpServices = _Me1200AccessManagementIpv4TableRowEditorSnmpServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 6),
    _Me1200AccessManagementIpv4TableRowEditorSnmpServices_Type()
)
me1200AccessManagementIpv4TableRowEditorSnmpServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorSnmpServices.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorTelnetServices_Type = TruthValue
_Me1200AccessManagementIpv4TableRowEditorTelnetServices_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorTelnetServices = _Me1200AccessManagementIpv4TableRowEditorTelnetServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 7),
    _Me1200AccessManagementIpv4TableRowEditorTelnetServices_Type()
)
me1200AccessManagementIpv4TableRowEditorTelnetServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorTelnetServices.setStatus("current")
_Me1200AccessManagementIpv4TableRowEditorAction_Type = ME1200RowEditorState
_Me1200AccessManagementIpv4TableRowEditorAction_Object = MibScalar
me1200AccessManagementIpv4TableRowEditorAction = _Me1200AccessManagementIpv4TableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 3, 100),
    _Me1200AccessManagementIpv4TableRowEditorAction_Type()
)
me1200AccessManagementIpv4TableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorAction.setStatus("current")
_Me1200AccessManagementIpv6Table_Object = MibTable
me1200AccessManagementIpv6Table = _Me1200AccessManagementIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6Table.setStatus("current")
_Me1200AccessManagementIpv6Entry_Object = MibTableRow
me1200AccessManagementIpv6Entry = _Me1200AccessManagementIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1)
)
me1200AccessManagementIpv6Entry.setIndexNames(
    (0, "ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6AccessIndex"),
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6Entry.setStatus("current")


class _Me1200AccessManagementIpv6AccessIndex_Type(Integer32):
    """Custom type me1200AccessManagementIpv6AccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200AccessManagementIpv6AccessIndex_Type.__name__ = "Integer32"
_Me1200AccessManagementIpv6AccessIndex_Object = MibTableColumn
me1200AccessManagementIpv6AccessIndex = _Me1200AccessManagementIpv6AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 1),
    _Me1200AccessManagementIpv6AccessIndex_Type()
)
me1200AccessManagementIpv6AccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6AccessIndex.setStatus("current")
_Me1200AccessManagementIpv6VlanId_Type = ME1200Unsigned16
_Me1200AccessManagementIpv6VlanId_Object = MibTableColumn
me1200AccessManagementIpv6VlanId = _Me1200AccessManagementIpv6VlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 2),
    _Me1200AccessManagementIpv6VlanId_Type()
)
me1200AccessManagementIpv6VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6VlanId.setStatus("current")
_Me1200AccessManagementIpv6StartAddress_Type = InetAddressIPv6
_Me1200AccessManagementIpv6StartAddress_Object = MibTableColumn
me1200AccessManagementIpv6StartAddress = _Me1200AccessManagementIpv6StartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 3),
    _Me1200AccessManagementIpv6StartAddress_Type()
)
me1200AccessManagementIpv6StartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6StartAddress.setStatus("current")
_Me1200AccessManagementIpv6EndAddress_Type = InetAddressIPv6
_Me1200AccessManagementIpv6EndAddress_Object = MibTableColumn
me1200AccessManagementIpv6EndAddress = _Me1200AccessManagementIpv6EndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 4),
    _Me1200AccessManagementIpv6EndAddress_Type()
)
me1200AccessManagementIpv6EndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6EndAddress.setStatus("current")
_Me1200AccessManagementIpv6WebServices_Type = TruthValue
_Me1200AccessManagementIpv6WebServices_Object = MibTableColumn
me1200AccessManagementIpv6WebServices = _Me1200AccessManagementIpv6WebServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 5),
    _Me1200AccessManagementIpv6WebServices_Type()
)
me1200AccessManagementIpv6WebServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6WebServices.setStatus("current")
_Me1200AccessManagementIpv6SnmpServices_Type = TruthValue
_Me1200AccessManagementIpv6SnmpServices_Object = MibTableColumn
me1200AccessManagementIpv6SnmpServices = _Me1200AccessManagementIpv6SnmpServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 6),
    _Me1200AccessManagementIpv6SnmpServices_Type()
)
me1200AccessManagementIpv6SnmpServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6SnmpServices.setStatus("current")
_Me1200AccessManagementIpv6TelnetServices_Type = TruthValue
_Me1200AccessManagementIpv6TelnetServices_Object = MibTableColumn
me1200AccessManagementIpv6TelnetServices = _Me1200AccessManagementIpv6TelnetServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 7),
    _Me1200AccessManagementIpv6TelnetServices_Type()
)
me1200AccessManagementIpv6TelnetServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TelnetServices.setStatus("current")
_Me1200AccessManagementIpv6Action_Type = ME1200RowEditorState
_Me1200AccessManagementIpv6Action_Object = MibTableColumn
me1200AccessManagementIpv6Action = _Me1200AccessManagementIpv6Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 4, 1, 100),
    _Me1200AccessManagementIpv6Action_Type()
)
me1200AccessManagementIpv6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6Action.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditor_ObjectIdentity = ObjectIdentity
me1200AccessManagementIpv6TableRowEditor = _Me1200AccessManagementIpv6TableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5)
)


class _Me1200AccessManagementIpv6TableRowEditorAccessIndex_Type(Integer32):
    """Custom type me1200AccessManagementIpv6TableRowEditorAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200AccessManagementIpv6TableRowEditorAccessIndex_Type.__name__ = "Integer32"
_Me1200AccessManagementIpv6TableRowEditorAccessIndex_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorAccessIndex = _Me1200AccessManagementIpv6TableRowEditorAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 1),
    _Me1200AccessManagementIpv6TableRowEditorAccessIndex_Type()
)
me1200AccessManagementIpv6TableRowEditorAccessIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorAccessIndex.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorVlanId_Type = ME1200Unsigned16
_Me1200AccessManagementIpv6TableRowEditorVlanId_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorVlanId = _Me1200AccessManagementIpv6TableRowEditorVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 2),
    _Me1200AccessManagementIpv6TableRowEditorVlanId_Type()
)
me1200AccessManagementIpv6TableRowEditorVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorVlanId.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorStartAddress_Type = InetAddressIPv6
_Me1200AccessManagementIpv6TableRowEditorStartAddress_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorStartAddress = _Me1200AccessManagementIpv6TableRowEditorStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 3),
    _Me1200AccessManagementIpv6TableRowEditorStartAddress_Type()
)
me1200AccessManagementIpv6TableRowEditorStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorStartAddress.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorEndAddress_Type = InetAddressIPv6
_Me1200AccessManagementIpv6TableRowEditorEndAddress_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorEndAddress = _Me1200AccessManagementIpv6TableRowEditorEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 4),
    _Me1200AccessManagementIpv6TableRowEditorEndAddress_Type()
)
me1200AccessManagementIpv6TableRowEditorEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorEndAddress.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorWebServices_Type = TruthValue
_Me1200AccessManagementIpv6TableRowEditorWebServices_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorWebServices = _Me1200AccessManagementIpv6TableRowEditorWebServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 5),
    _Me1200AccessManagementIpv6TableRowEditorWebServices_Type()
)
me1200AccessManagementIpv6TableRowEditorWebServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorWebServices.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorSnmpServices_Type = TruthValue
_Me1200AccessManagementIpv6TableRowEditorSnmpServices_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorSnmpServices = _Me1200AccessManagementIpv6TableRowEditorSnmpServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 6),
    _Me1200AccessManagementIpv6TableRowEditorSnmpServices_Type()
)
me1200AccessManagementIpv6TableRowEditorSnmpServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorSnmpServices.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorTelnetServices_Type = TruthValue
_Me1200AccessManagementIpv6TableRowEditorTelnetServices_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorTelnetServices = _Me1200AccessManagementIpv6TableRowEditorTelnetServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 7),
    _Me1200AccessManagementIpv6TableRowEditorTelnetServices_Type()
)
me1200AccessManagementIpv6TableRowEditorTelnetServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorTelnetServices.setStatus("current")
_Me1200AccessManagementIpv6TableRowEditorAction_Type = ME1200RowEditorState
_Me1200AccessManagementIpv6TableRowEditorAction_Object = MibScalar
me1200AccessManagementIpv6TableRowEditorAction = _Me1200AccessManagementIpv6TableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 2, 5, 100),
    _Me1200AccessManagementIpv6TableRowEditorAction_Type()
)
me1200AccessManagementIpv6TableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorAction.setStatus("current")
_Me1200AccessManagementStatus_ObjectIdentity = ObjectIdentity
me1200AccessManagementStatus = _Me1200AccessManagementStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3)
)
_Me1200AccessManagementStatistics_ObjectIdentity = ObjectIdentity
me1200AccessManagementStatistics = _Me1200AccessManagementStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1)
)
_Me1200AccessManagementStatisticsHttpReceivedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsHttpReceivedPkts_Object = MibScalar
me1200AccessManagementStatisticsHttpReceivedPkts = _Me1200AccessManagementStatisticsHttpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 1),
    _Me1200AccessManagementStatisticsHttpReceivedPkts_Type()
)
me1200AccessManagementStatisticsHttpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsHttpReceivedPkts.setStatus("current")
_Me1200AccessManagementStatisticsHttpAllowedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsHttpAllowedPkts_Object = MibScalar
me1200AccessManagementStatisticsHttpAllowedPkts = _Me1200AccessManagementStatisticsHttpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 2),
    _Me1200AccessManagementStatisticsHttpAllowedPkts_Type()
)
me1200AccessManagementStatisticsHttpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsHttpAllowedPkts.setStatus("current")
_Me1200AccessManagementStatisticsHttpDiscardedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsHttpDiscardedPkts_Object = MibScalar
me1200AccessManagementStatisticsHttpDiscardedPkts = _Me1200AccessManagementStatisticsHttpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 3),
    _Me1200AccessManagementStatisticsHttpDiscardedPkts_Type()
)
me1200AccessManagementStatisticsHttpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsHttpDiscardedPkts.setStatus("current")
_Me1200AccessManagementStatisticsHttpsReceivedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsHttpsReceivedPkts_Object = MibScalar
me1200AccessManagementStatisticsHttpsReceivedPkts = _Me1200AccessManagementStatisticsHttpsReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 4),
    _Me1200AccessManagementStatisticsHttpsReceivedPkts_Type()
)
me1200AccessManagementStatisticsHttpsReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsHttpsReceivedPkts.setStatus("current")
_Me1200AccessManagementStatisticsHttpsAllowedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsHttpsAllowedPkts_Object = MibScalar
me1200AccessManagementStatisticsHttpsAllowedPkts = _Me1200AccessManagementStatisticsHttpsAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 5),
    _Me1200AccessManagementStatisticsHttpsAllowedPkts_Type()
)
me1200AccessManagementStatisticsHttpsAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsHttpsAllowedPkts.setStatus("current")
_Me1200AccessManagementStatisticsHttpsDiscardedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsHttpsDiscardedPkts_Object = MibScalar
me1200AccessManagementStatisticsHttpsDiscardedPkts = _Me1200AccessManagementStatisticsHttpsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 6),
    _Me1200AccessManagementStatisticsHttpsDiscardedPkts_Type()
)
me1200AccessManagementStatisticsHttpsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsHttpsDiscardedPkts.setStatus("current")
_Me1200AccessManagementStatisticsSnmpReceivedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsSnmpReceivedPkts_Object = MibScalar
me1200AccessManagementStatisticsSnmpReceivedPkts = _Me1200AccessManagementStatisticsSnmpReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 7),
    _Me1200AccessManagementStatisticsSnmpReceivedPkts_Type()
)
me1200AccessManagementStatisticsSnmpReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsSnmpReceivedPkts.setStatus("current")
_Me1200AccessManagementStatisticsSnmpAllowedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsSnmpAllowedPkts_Object = MibScalar
me1200AccessManagementStatisticsSnmpAllowedPkts = _Me1200AccessManagementStatisticsSnmpAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 8),
    _Me1200AccessManagementStatisticsSnmpAllowedPkts_Type()
)
me1200AccessManagementStatisticsSnmpAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsSnmpAllowedPkts.setStatus("current")
_Me1200AccessManagementStatisticsSnmpDiscardedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsSnmpDiscardedPkts_Object = MibScalar
me1200AccessManagementStatisticsSnmpDiscardedPkts = _Me1200AccessManagementStatisticsSnmpDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 9),
    _Me1200AccessManagementStatisticsSnmpDiscardedPkts_Type()
)
me1200AccessManagementStatisticsSnmpDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsSnmpDiscardedPkts.setStatus("current")
_Me1200AccessManagementStatisticsTelnetReceivedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsTelnetReceivedPkts_Object = MibScalar
me1200AccessManagementStatisticsTelnetReceivedPkts = _Me1200AccessManagementStatisticsTelnetReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 10),
    _Me1200AccessManagementStatisticsTelnetReceivedPkts_Type()
)
me1200AccessManagementStatisticsTelnetReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsTelnetReceivedPkts.setStatus("current")
_Me1200AccessManagementStatisticsTelnetAllowedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsTelnetAllowedPkts_Object = MibScalar
me1200AccessManagementStatisticsTelnetAllowedPkts = _Me1200AccessManagementStatisticsTelnetAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 11),
    _Me1200AccessManagementStatisticsTelnetAllowedPkts_Type()
)
me1200AccessManagementStatisticsTelnetAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsTelnetAllowedPkts.setStatus("current")
_Me1200AccessManagementStatisticsTelnetDiscardedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsTelnetDiscardedPkts_Object = MibScalar
me1200AccessManagementStatisticsTelnetDiscardedPkts = _Me1200AccessManagementStatisticsTelnetDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 12),
    _Me1200AccessManagementStatisticsTelnetDiscardedPkts_Type()
)
me1200AccessManagementStatisticsTelnetDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsTelnetDiscardedPkts.setStatus("current")
_Me1200AccessManagementStatisticsSshReceivedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsSshReceivedPkts_Object = MibScalar
me1200AccessManagementStatisticsSshReceivedPkts = _Me1200AccessManagementStatisticsSshReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 13),
    _Me1200AccessManagementStatisticsSshReceivedPkts_Type()
)
me1200AccessManagementStatisticsSshReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsSshReceivedPkts.setStatus("current")
_Me1200AccessManagementStatisticsSshAllowedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsSshAllowedPkts_Object = MibScalar
me1200AccessManagementStatisticsSshAllowedPkts = _Me1200AccessManagementStatisticsSshAllowedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 14),
    _Me1200AccessManagementStatisticsSshAllowedPkts_Type()
)
me1200AccessManagementStatisticsSshAllowedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsSshAllowedPkts.setStatus("current")
_Me1200AccessManagementStatisticsSshDiscardedPkts_Type = Unsigned32
_Me1200AccessManagementStatisticsSshDiscardedPkts_Object = MibScalar
me1200AccessManagementStatisticsSshDiscardedPkts = _Me1200AccessManagementStatisticsSshDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 3, 1, 15),
    _Me1200AccessManagementStatisticsSshDiscardedPkts_Type()
)
me1200AccessManagementStatisticsSshDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsSshDiscardedPkts.setStatus("current")
_Me1200AccessManagementControl_ObjectIdentity = ObjectIdentity
me1200AccessManagementControl = _Me1200AccessManagementControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 4)
)
_Me1200AccessManagementControlStatistics_ObjectIdentity = ObjectIdentity
me1200AccessManagementControlStatistics = _Me1200AccessManagementControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 4, 1)
)
_Me1200AccessManagementControlStatisticsClear_Type = TruthValue
_Me1200AccessManagementControlStatisticsClear_Object = MibScalar
me1200AccessManagementControlStatisticsClear = _Me1200AccessManagementControlStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 1, 4, 1, 1),
    _Me1200AccessManagementControlStatisticsClear_Type()
)
me1200AccessManagementControlStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AccessManagementControlStatisticsClear.setStatus("current")
_Me1200AccessManagementMIBConformance_ObjectIdentity = ObjectIdentity
me1200AccessManagementMIBConformance = _Me1200AccessManagementMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2)
)
_Me1200AccessManagementMIBCompliances_ObjectIdentity = ObjectIdentity
me1200AccessManagementMIBCompliances = _Me1200AccessManagementMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 1)
)
_Me1200AccessManagementMIBGroups_ObjectIdentity = ObjectIdentity
me1200AccessManagementMIBGroups = _Me1200AccessManagementMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2)
)

# Managed Objects groups

me1200AccessManagementGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 1)
)
me1200AccessManagementGlobalsInfoGroup.setObjects(
    ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementGlobalsAdminState")
)
if mibBuilder.loadTexts:
    me1200AccessManagementGlobalsInfoGroup.setStatus("current")

me1200AccessManagementIpv4TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 2)
)
me1200AccessManagementIpv4TableInfoGroup.setObjects(
      *(("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4VlanId"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4StartAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4EndAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4WebServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4SnmpServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TelnetServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4Action"))
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableInfoGroup.setStatus("current")

me1200AccessManagementIpv4TableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 3)
)
me1200AccessManagementIpv4TableRowEditorInfoGroup.setObjects(
      *(("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorAccessIndex"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorVlanId"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorStartAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorEndAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorWebServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorSnmpServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorTelnetServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv4TableRowEditorInfoGroup.setStatus("current")

me1200AccessManagementIpv6TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 4)
)
me1200AccessManagementIpv6TableInfoGroup.setObjects(
      *(("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6VlanId"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6StartAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6EndAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6WebServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6SnmpServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TelnetServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6Action"))
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableInfoGroup.setStatus("current")

me1200AccessManagementIpv6TableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 5)
)
me1200AccessManagementIpv6TableRowEditorInfoGroup.setObjects(
      *(("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorAccessIndex"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorVlanId"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorStartAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorEndAddress"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorWebServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorSnmpServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorTelnetServices"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200AccessManagementIpv6TableRowEditorInfoGroup.setStatus("current")

me1200AccessManagementStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 6)
)
me1200AccessManagementStatisticsInfoGroup.setObjects(
      *(("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsHttpReceivedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsHttpAllowedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsHttpDiscardedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsHttpsReceivedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsHttpsAllowedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsHttpsDiscardedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsSnmpReceivedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsSnmpAllowedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsSnmpDiscardedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsTelnetReceivedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsTelnetAllowedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsTelnetDiscardedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsSshReceivedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsSshAllowedPkts"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsSshDiscardedPkts"))
)
if mibBuilder.loadTexts:
    me1200AccessManagementStatisticsInfoGroup.setStatus("current")

me1200AccessManagementControlStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 2, 7)
)
me1200AccessManagementControlStatisticsInfoGroup.setObjects(
    ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementControlStatisticsClear")
)
if mibBuilder.loadTexts:
    me1200AccessManagementControlStatisticsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200AccessManagementMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 51, 2, 1, 1)
)
me1200AccessManagementMibCompliance.setObjects(
      *(("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementGlobalsInfoGroup"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableInfoGroup"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv4TableRowEditorInfoGroup"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableInfoGroup"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementIpv6TableRowEditorInfoGroup"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementStatisticsInfoGroup"),
        ("ME1200-ACCESS-MANAGEMENT-MIB", "me1200AccessManagementControlStatisticsInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200AccessManagementMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-ACCESS-MANAGEMENT-MIB",
    **{"me1200AccessManagementMib": me1200AccessManagementMib,
       "me1200AccessManagementMIBObjects": me1200AccessManagementMIBObjects,
       "me1200AccessManagementConfig": me1200AccessManagementConfig,
       "me1200AccessManagementGlobals": me1200AccessManagementGlobals,
       "me1200AccessManagementGlobalsAdminState": me1200AccessManagementGlobalsAdminState,
       "me1200AccessManagementIpv4Table": me1200AccessManagementIpv4Table,
       "me1200AccessManagementIpv4Entry": me1200AccessManagementIpv4Entry,
       "me1200AccessManagementIpv4AccessIndex": me1200AccessManagementIpv4AccessIndex,
       "me1200AccessManagementIpv4VlanId": me1200AccessManagementIpv4VlanId,
       "me1200AccessManagementIpv4StartAddress": me1200AccessManagementIpv4StartAddress,
       "me1200AccessManagementIpv4EndAddress": me1200AccessManagementIpv4EndAddress,
       "me1200AccessManagementIpv4WebServices": me1200AccessManagementIpv4WebServices,
       "me1200AccessManagementIpv4SnmpServices": me1200AccessManagementIpv4SnmpServices,
       "me1200AccessManagementIpv4TelnetServices": me1200AccessManagementIpv4TelnetServices,
       "me1200AccessManagementIpv4Action": me1200AccessManagementIpv4Action,
       "me1200AccessManagementIpv4TableRowEditor": me1200AccessManagementIpv4TableRowEditor,
       "me1200AccessManagementIpv4TableRowEditorAccessIndex": me1200AccessManagementIpv4TableRowEditorAccessIndex,
       "me1200AccessManagementIpv4TableRowEditorVlanId": me1200AccessManagementIpv4TableRowEditorVlanId,
       "me1200AccessManagementIpv4TableRowEditorStartAddress": me1200AccessManagementIpv4TableRowEditorStartAddress,
       "me1200AccessManagementIpv4TableRowEditorEndAddress": me1200AccessManagementIpv4TableRowEditorEndAddress,
       "me1200AccessManagementIpv4TableRowEditorWebServices": me1200AccessManagementIpv4TableRowEditorWebServices,
       "me1200AccessManagementIpv4TableRowEditorSnmpServices": me1200AccessManagementIpv4TableRowEditorSnmpServices,
       "me1200AccessManagementIpv4TableRowEditorTelnetServices": me1200AccessManagementIpv4TableRowEditorTelnetServices,
       "me1200AccessManagementIpv4TableRowEditorAction": me1200AccessManagementIpv4TableRowEditorAction,
       "me1200AccessManagementIpv6Table": me1200AccessManagementIpv6Table,
       "me1200AccessManagementIpv6Entry": me1200AccessManagementIpv6Entry,
       "me1200AccessManagementIpv6AccessIndex": me1200AccessManagementIpv6AccessIndex,
       "me1200AccessManagementIpv6VlanId": me1200AccessManagementIpv6VlanId,
       "me1200AccessManagementIpv6StartAddress": me1200AccessManagementIpv6StartAddress,
       "me1200AccessManagementIpv6EndAddress": me1200AccessManagementIpv6EndAddress,
       "me1200AccessManagementIpv6WebServices": me1200AccessManagementIpv6WebServices,
       "me1200AccessManagementIpv6SnmpServices": me1200AccessManagementIpv6SnmpServices,
       "me1200AccessManagementIpv6TelnetServices": me1200AccessManagementIpv6TelnetServices,
       "me1200AccessManagementIpv6Action": me1200AccessManagementIpv6Action,
       "me1200AccessManagementIpv6TableRowEditor": me1200AccessManagementIpv6TableRowEditor,
       "me1200AccessManagementIpv6TableRowEditorAccessIndex": me1200AccessManagementIpv6TableRowEditorAccessIndex,
       "me1200AccessManagementIpv6TableRowEditorVlanId": me1200AccessManagementIpv6TableRowEditorVlanId,
       "me1200AccessManagementIpv6TableRowEditorStartAddress": me1200AccessManagementIpv6TableRowEditorStartAddress,
       "me1200AccessManagementIpv6TableRowEditorEndAddress": me1200AccessManagementIpv6TableRowEditorEndAddress,
       "me1200AccessManagementIpv6TableRowEditorWebServices": me1200AccessManagementIpv6TableRowEditorWebServices,
       "me1200AccessManagementIpv6TableRowEditorSnmpServices": me1200AccessManagementIpv6TableRowEditorSnmpServices,
       "me1200AccessManagementIpv6TableRowEditorTelnetServices": me1200AccessManagementIpv6TableRowEditorTelnetServices,
       "me1200AccessManagementIpv6TableRowEditorAction": me1200AccessManagementIpv6TableRowEditorAction,
       "me1200AccessManagementStatus": me1200AccessManagementStatus,
       "me1200AccessManagementStatistics": me1200AccessManagementStatistics,
       "me1200AccessManagementStatisticsHttpReceivedPkts": me1200AccessManagementStatisticsHttpReceivedPkts,
       "me1200AccessManagementStatisticsHttpAllowedPkts": me1200AccessManagementStatisticsHttpAllowedPkts,
       "me1200AccessManagementStatisticsHttpDiscardedPkts": me1200AccessManagementStatisticsHttpDiscardedPkts,
       "me1200AccessManagementStatisticsHttpsReceivedPkts": me1200AccessManagementStatisticsHttpsReceivedPkts,
       "me1200AccessManagementStatisticsHttpsAllowedPkts": me1200AccessManagementStatisticsHttpsAllowedPkts,
       "me1200AccessManagementStatisticsHttpsDiscardedPkts": me1200AccessManagementStatisticsHttpsDiscardedPkts,
       "me1200AccessManagementStatisticsSnmpReceivedPkts": me1200AccessManagementStatisticsSnmpReceivedPkts,
       "me1200AccessManagementStatisticsSnmpAllowedPkts": me1200AccessManagementStatisticsSnmpAllowedPkts,
       "me1200AccessManagementStatisticsSnmpDiscardedPkts": me1200AccessManagementStatisticsSnmpDiscardedPkts,
       "me1200AccessManagementStatisticsTelnetReceivedPkts": me1200AccessManagementStatisticsTelnetReceivedPkts,
       "me1200AccessManagementStatisticsTelnetAllowedPkts": me1200AccessManagementStatisticsTelnetAllowedPkts,
       "me1200AccessManagementStatisticsTelnetDiscardedPkts": me1200AccessManagementStatisticsTelnetDiscardedPkts,
       "me1200AccessManagementStatisticsSshReceivedPkts": me1200AccessManagementStatisticsSshReceivedPkts,
       "me1200AccessManagementStatisticsSshAllowedPkts": me1200AccessManagementStatisticsSshAllowedPkts,
       "me1200AccessManagementStatisticsSshDiscardedPkts": me1200AccessManagementStatisticsSshDiscardedPkts,
       "me1200AccessManagementControl": me1200AccessManagementControl,
       "me1200AccessManagementControlStatistics": me1200AccessManagementControlStatistics,
       "me1200AccessManagementControlStatisticsClear": me1200AccessManagementControlStatisticsClear,
       "me1200AccessManagementMIBConformance": me1200AccessManagementMIBConformance,
       "me1200AccessManagementMIBCompliances": me1200AccessManagementMIBCompliances,
       "me1200AccessManagementMibCompliance": me1200AccessManagementMibCompliance,
       "me1200AccessManagementMIBGroups": me1200AccessManagementMIBGroups,
       "me1200AccessManagementGlobalsInfoGroup": me1200AccessManagementGlobalsInfoGroup,
       "me1200AccessManagementIpv4TableInfoGroup": me1200AccessManagementIpv4TableInfoGroup,
       "me1200AccessManagementIpv4TableRowEditorInfoGroup": me1200AccessManagementIpv4TableRowEditorInfoGroup,
       "me1200AccessManagementIpv6TableInfoGroup": me1200AccessManagementIpv6TableInfoGroup,
       "me1200AccessManagementIpv6TableRowEditorInfoGroup": me1200AccessManagementIpv6TableRowEditorInfoGroup,
       "me1200AccessManagementStatisticsInfoGroup": me1200AccessManagementStatisticsInfoGroup,
       "me1200AccessManagementControlStatisticsInfoGroup": me1200AccessManagementControlStatisticsInfoGroup}
)
