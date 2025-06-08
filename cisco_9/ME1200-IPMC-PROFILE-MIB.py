# SNMP MIB module (ME1200-IPMC-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-IPMC-PROFILE-MIB.mib
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
 ME1200RowEditorState) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200RowEditorState")

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

me1200IpmcProfileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38)
)
if mibBuilder.loadTexts:
    me1200IpmcProfileMib.setRevisions(
        ("2014-03-11 00:00",
         "2014-01-29 00:00",
         "2014-01-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200IpmcProfileRuleActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200IpmcProfileMIBObjects_ObjectIdentity = ObjectIdentity
me1200IpmcProfileMIBObjects = _Me1200IpmcProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1)
)
_Me1200IpmcProfileConfig_ObjectIdentity = ObjectIdentity
me1200IpmcProfileConfig = _Me1200IpmcProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2)
)
_Me1200IpmcProfileGlobals_ObjectIdentity = ObjectIdentity
me1200IpmcProfileGlobals = _Me1200IpmcProfileGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 1)
)
_Me1200IpmcProfileGlobalsAdminState_Type = TruthValue
_Me1200IpmcProfileGlobalsAdminState_Object = MibScalar
me1200IpmcProfileGlobalsAdminState = _Me1200IpmcProfileGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 1, 1),
    _Me1200IpmcProfileGlobalsAdminState_Type()
)
me1200IpmcProfileGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileGlobalsAdminState.setStatus("current")
_Me1200IpmcProfileManagementTable_Object = MibTable
me1200IpmcProfileManagementTable = _Me1200IpmcProfileManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementTable.setStatus("current")
_Me1200IpmcProfileManagementEntry_Object = MibTableRow
me1200IpmcProfileManagementEntry = _Me1200IpmcProfileManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 2, 1)
)
me1200IpmcProfileManagementEntry.setIndexNames(
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementProfileName"),
)
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementEntry.setStatus("current")


class _Me1200IpmcProfileManagementProfileName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileManagementProfileName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileManagementProfileName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileManagementProfileName_Object = MibTableColumn
me1200IpmcProfileManagementProfileName = _Me1200IpmcProfileManagementProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 2, 1, 1),
    _Me1200IpmcProfileManagementProfileName_Type()
)
me1200IpmcProfileManagementProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementProfileName.setStatus("current")


class _Me1200IpmcProfileManagementProfileDescription_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileManagementProfileDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200IpmcProfileManagementProfileDescription_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileManagementProfileDescription_Object = MibTableColumn
me1200IpmcProfileManagementProfileDescription = _Me1200IpmcProfileManagementProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 2, 1, 2),
    _Me1200IpmcProfileManagementProfileDescription_Type()
)
me1200IpmcProfileManagementProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementProfileDescription.setStatus("current")
_Me1200IpmcProfileManagementAction_Type = ME1200RowEditorState
_Me1200IpmcProfileManagementAction_Object = MibTableColumn
me1200IpmcProfileManagementAction = _Me1200IpmcProfileManagementAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 2, 1, 100),
    _Me1200IpmcProfileManagementAction_Type()
)
me1200IpmcProfileManagementAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementAction.setStatus("current")
_Me1200IpmcProfileManagementTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcProfileManagementTableRowEditor = _Me1200IpmcProfileManagementTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 3)
)


class _Me1200IpmcProfileManagementTableRowEditorProfileName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileManagementTableRowEditorProfileName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileManagementTableRowEditorProfileName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileManagementTableRowEditorProfileName_Object = MibScalar
me1200IpmcProfileManagementTableRowEditorProfileName = _Me1200IpmcProfileManagementTableRowEditorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 3, 1),
    _Me1200IpmcProfileManagementTableRowEditorProfileName_Type()
)
me1200IpmcProfileManagementTableRowEditorProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementTableRowEditorProfileName.setStatus("current")


class _Me1200IpmcProfileManagementTableRowEditorProfileDescription_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileManagementTableRowEditorProfileDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200IpmcProfileManagementTableRowEditorProfileDescription_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileManagementTableRowEditorProfileDescription_Object = MibScalar
me1200IpmcProfileManagementTableRowEditorProfileDescription = _Me1200IpmcProfileManagementTableRowEditorProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 3, 2),
    _Me1200IpmcProfileManagementTableRowEditorProfileDescription_Type()
)
me1200IpmcProfileManagementTableRowEditorProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementTableRowEditorProfileDescription.setStatus("current")
_Me1200IpmcProfileManagementTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcProfileManagementTableRowEditorAction_Object = MibScalar
me1200IpmcProfileManagementTableRowEditorAction = _Me1200IpmcProfileManagementTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 3, 100),
    _Me1200IpmcProfileManagementTableRowEditorAction_Type()
)
me1200IpmcProfileManagementTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementTableRowEditorAction.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeTable_Object = MibTable
me1200IpmcProfileIpv4AddressRangeTable = _Me1200IpmcProfileIpv4AddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTable.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeEntry_Object = MibTableRow
me1200IpmcProfileIpv4AddressRangeEntry = _Me1200IpmcProfileIpv4AddressRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 4, 1)
)
me1200IpmcProfileIpv4AddressRangeEntry.setIndexNames(
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeRangeName"),
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeEntry.setStatus("current")


class _Me1200IpmcProfileIpv4AddressRangeRangeName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileIpv4AddressRangeRangeName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileIpv4AddressRangeRangeName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileIpv4AddressRangeRangeName_Object = MibTableColumn
me1200IpmcProfileIpv4AddressRangeRangeName = _Me1200IpmcProfileIpv4AddressRangeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 4, 1, 1),
    _Me1200IpmcProfileIpv4AddressRangeRangeName_Type()
)
me1200IpmcProfileIpv4AddressRangeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeRangeName.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeStartAddress_Type = IpAddress
_Me1200IpmcProfileIpv4AddressRangeStartAddress_Object = MibTableColumn
me1200IpmcProfileIpv4AddressRangeStartAddress = _Me1200IpmcProfileIpv4AddressRangeStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 4, 1, 2),
    _Me1200IpmcProfileIpv4AddressRangeStartAddress_Type()
)
me1200IpmcProfileIpv4AddressRangeStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeStartAddress.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeEndAddress_Type = IpAddress
_Me1200IpmcProfileIpv4AddressRangeEndAddress_Object = MibTableColumn
me1200IpmcProfileIpv4AddressRangeEndAddress = _Me1200IpmcProfileIpv4AddressRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 4, 1, 3),
    _Me1200IpmcProfileIpv4AddressRangeEndAddress_Type()
)
me1200IpmcProfileIpv4AddressRangeEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeEndAddress.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeAction_Type = ME1200RowEditorState
_Me1200IpmcProfileIpv4AddressRangeAction_Object = MibTableColumn
me1200IpmcProfileIpv4AddressRangeAction = _Me1200IpmcProfileIpv4AddressRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 4, 1, 100),
    _Me1200IpmcProfileIpv4AddressRangeAction_Type()
)
me1200IpmcProfileIpv4AddressRangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeAction.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcProfileIpv4AddressRangeTableRowEditor = _Me1200IpmcProfileIpv4AddressRangeTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 5)
)


class _Me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName_Object = MibScalar
me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName = _Me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 5, 1),
    _Me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName_Type()
)
me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress_Type = IpAddress
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress_Object = MibScalar
me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress = _Me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 5, 2),
    _Me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress_Type()
)
me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress_Type = IpAddress
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress_Object = MibScalar
me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress = _Me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 5, 3),
    _Me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress_Type()
)
me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress.setStatus("current")
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcProfileIpv4AddressRangeTableRowEditorAction_Object = MibScalar
me1200IpmcProfileIpv4AddressRangeTableRowEditorAction = _Me1200IpmcProfileIpv4AddressRangeTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 5, 100),
    _Me1200IpmcProfileIpv4AddressRangeTableRowEditorAction_Type()
)
me1200IpmcProfileIpv4AddressRangeTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTableRowEditorAction.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeTable_Object = MibTable
me1200IpmcProfileIpv6AddressRangeTable = _Me1200IpmcProfileIpv6AddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 6)
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTable.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeEntry_Object = MibTableRow
me1200IpmcProfileIpv6AddressRangeEntry = _Me1200IpmcProfileIpv6AddressRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 6, 1)
)
me1200IpmcProfileIpv6AddressRangeEntry.setIndexNames(
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeRangeName"),
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeEntry.setStatus("current")


class _Me1200IpmcProfileIpv6AddressRangeRangeName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileIpv6AddressRangeRangeName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileIpv6AddressRangeRangeName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileIpv6AddressRangeRangeName_Object = MibTableColumn
me1200IpmcProfileIpv6AddressRangeRangeName = _Me1200IpmcProfileIpv6AddressRangeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 6, 1, 1),
    _Me1200IpmcProfileIpv6AddressRangeRangeName_Type()
)
me1200IpmcProfileIpv6AddressRangeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeRangeName.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeStartAddress_Type = InetAddressIPv6
_Me1200IpmcProfileIpv6AddressRangeStartAddress_Object = MibTableColumn
me1200IpmcProfileIpv6AddressRangeStartAddress = _Me1200IpmcProfileIpv6AddressRangeStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 6, 1, 2),
    _Me1200IpmcProfileIpv6AddressRangeStartAddress_Type()
)
me1200IpmcProfileIpv6AddressRangeStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeStartAddress.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeEndAddress_Type = InetAddressIPv6
_Me1200IpmcProfileIpv6AddressRangeEndAddress_Object = MibTableColumn
me1200IpmcProfileIpv6AddressRangeEndAddress = _Me1200IpmcProfileIpv6AddressRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 6, 1, 3),
    _Me1200IpmcProfileIpv6AddressRangeEndAddress_Type()
)
me1200IpmcProfileIpv6AddressRangeEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeEndAddress.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeAction_Type = ME1200RowEditorState
_Me1200IpmcProfileIpv6AddressRangeAction_Object = MibTableColumn
me1200IpmcProfileIpv6AddressRangeAction = _Me1200IpmcProfileIpv6AddressRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 6, 1, 100),
    _Me1200IpmcProfileIpv6AddressRangeAction_Type()
)
me1200IpmcProfileIpv6AddressRangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeAction.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcProfileIpv6AddressRangeTableRowEditor = _Me1200IpmcProfileIpv6AddressRangeTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 7)
)


class _Me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName_Object = MibScalar
me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName = _Me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 7, 1),
    _Me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName_Type()
)
me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress_Type = InetAddressIPv6
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress_Object = MibScalar
me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress = _Me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 7, 2),
    _Me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress_Type()
)
me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress_Type = InetAddressIPv6
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress_Object = MibScalar
me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress = _Me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 7, 3),
    _Me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress_Type()
)
me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress.setStatus("current")
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcProfileIpv6AddressRangeTableRowEditorAction_Object = MibScalar
me1200IpmcProfileIpv6AddressRangeTableRowEditorAction = _Me1200IpmcProfileIpv6AddressRangeTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 7, 100),
    _Me1200IpmcProfileIpv6AddressRangeTableRowEditorAction_Type()
)
me1200IpmcProfileIpv6AddressRangeTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTableRowEditorAction.setStatus("current")
_Me1200IpmcProfileRuleTable_Object = MibTable
me1200IpmcProfileRuleTable = _Me1200IpmcProfileRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8)
)
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTable.setStatus("current")
_Me1200IpmcProfileRuleEntry_Object = MibTableRow
me1200IpmcProfileRuleEntry = _Me1200IpmcProfileRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1)
)
me1200IpmcProfileRuleEntry.setIndexNames(
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleProfileName"),
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleRuleRange"),
)
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleEntry.setStatus("current")


class _Me1200IpmcProfileRuleProfileName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileRuleProfileName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileRuleProfileName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileRuleProfileName_Object = MibTableColumn
me1200IpmcProfileRuleProfileName = _Me1200IpmcProfileRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1, 1),
    _Me1200IpmcProfileRuleProfileName_Type()
)
me1200IpmcProfileRuleProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleProfileName.setStatus("current")


class _Me1200IpmcProfileRuleRuleRange_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileRuleRuleRange based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileRuleRuleRange_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileRuleRuleRange_Object = MibTableColumn
me1200IpmcProfileRuleRuleRange = _Me1200IpmcProfileRuleRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1, 2),
    _Me1200IpmcProfileRuleRuleRange_Type()
)
me1200IpmcProfileRuleRuleRange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleRuleRange.setStatus("current")


class _Me1200IpmcProfileRuleNextRuleRange_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileRuleNextRuleRange based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileRuleNextRuleRange_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileRuleNextRuleRange_Object = MibTableColumn
me1200IpmcProfileRuleNextRuleRange = _Me1200IpmcProfileRuleNextRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1, 3),
    _Me1200IpmcProfileRuleNextRuleRange_Type()
)
me1200IpmcProfileRuleNextRuleRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleNextRuleRange.setStatus("current")
_Me1200IpmcProfileRuleRuleAction_Type = ME1200IpmcProfileRuleActionType
_Me1200IpmcProfileRuleRuleAction_Object = MibTableColumn
me1200IpmcProfileRuleRuleAction = _Me1200IpmcProfileRuleRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1, 4),
    _Me1200IpmcProfileRuleRuleAction_Type()
)
me1200IpmcProfileRuleRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleRuleAction.setStatus("current")
_Me1200IpmcProfileRuleRuleLog_Type = TruthValue
_Me1200IpmcProfileRuleRuleLog_Object = MibTableColumn
me1200IpmcProfileRuleRuleLog = _Me1200IpmcProfileRuleRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1, 5),
    _Me1200IpmcProfileRuleRuleLog_Type()
)
me1200IpmcProfileRuleRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleRuleLog.setStatus("current")
_Me1200IpmcProfileRuleAction_Type = ME1200RowEditorState
_Me1200IpmcProfileRuleAction_Object = MibTableColumn
me1200IpmcProfileRuleAction = _Me1200IpmcProfileRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 8, 1, 100),
    _Me1200IpmcProfileRuleAction_Type()
)
me1200IpmcProfileRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleAction.setStatus("current")
_Me1200IpmcProfileRuleTableRowEditor_ObjectIdentity = ObjectIdentity
me1200IpmcProfileRuleTableRowEditor = _Me1200IpmcProfileRuleTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9)
)


class _Me1200IpmcProfileRuleTableRowEditorProfileName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileRuleTableRowEditorProfileName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileRuleTableRowEditorProfileName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileRuleTableRowEditorProfileName_Object = MibScalar
me1200IpmcProfileRuleTableRowEditorProfileName = _Me1200IpmcProfileRuleTableRowEditorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9, 1),
    _Me1200IpmcProfileRuleTableRowEditorProfileName_Type()
)
me1200IpmcProfileRuleTableRowEditorProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorProfileName.setStatus("current")


class _Me1200IpmcProfileRuleTableRowEditorRuleRange_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileRuleTableRowEditorRuleRange based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileRuleTableRowEditorRuleRange_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileRuleTableRowEditorRuleRange_Object = MibScalar
me1200IpmcProfileRuleTableRowEditorRuleRange = _Me1200IpmcProfileRuleTableRowEditorRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9, 2),
    _Me1200IpmcProfileRuleTableRowEditorRuleRange_Type()
)
me1200IpmcProfileRuleTableRowEditorRuleRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorRuleRange.setStatus("current")


class _Me1200IpmcProfileRuleTableRowEditorNextRuleRange_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfileRuleTableRowEditorNextRuleRange based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfileRuleTableRowEditorNextRuleRange_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfileRuleTableRowEditorNextRuleRange_Object = MibScalar
me1200IpmcProfileRuleTableRowEditorNextRuleRange = _Me1200IpmcProfileRuleTableRowEditorNextRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9, 3),
    _Me1200IpmcProfileRuleTableRowEditorNextRuleRange_Type()
)
me1200IpmcProfileRuleTableRowEditorNextRuleRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorNextRuleRange.setStatus("current")
_Me1200IpmcProfileRuleTableRowEditorRuleAction_Type = ME1200IpmcProfileRuleActionType
_Me1200IpmcProfileRuleTableRowEditorRuleAction_Object = MibScalar
me1200IpmcProfileRuleTableRowEditorRuleAction = _Me1200IpmcProfileRuleTableRowEditorRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9, 4),
    _Me1200IpmcProfileRuleTableRowEditorRuleAction_Type()
)
me1200IpmcProfileRuleTableRowEditorRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorRuleAction.setStatus("current")
_Me1200IpmcProfileRuleTableRowEditorRuleLog_Type = TruthValue
_Me1200IpmcProfileRuleTableRowEditorRuleLog_Object = MibScalar
me1200IpmcProfileRuleTableRowEditorRuleLog = _Me1200IpmcProfileRuleTableRowEditorRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9, 5),
    _Me1200IpmcProfileRuleTableRowEditorRuleLog_Type()
)
me1200IpmcProfileRuleTableRowEditorRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorRuleLog.setStatus("current")
_Me1200IpmcProfileRuleTableRowEditorAction_Type = ME1200RowEditorState
_Me1200IpmcProfileRuleTableRowEditorAction_Object = MibScalar
me1200IpmcProfileRuleTableRowEditorAction = _Me1200IpmcProfileRuleTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 9, 100),
    _Me1200IpmcProfileRuleTableRowEditorAction_Type()
)
me1200IpmcProfileRuleTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorAction.setStatus("current")
_Me1200IpmcProfilePrecedenceTable_Object = MibTable
me1200IpmcProfilePrecedenceTable = _Me1200IpmcProfilePrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10)
)
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceTable.setStatus("current")
_Me1200IpmcProfilePrecedenceEntry_Object = MibTableRow
me1200IpmcProfilePrecedenceEntry = _Me1200IpmcProfilePrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1)
)
me1200IpmcProfilePrecedenceEntry.setIndexNames(
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceProfileName"),
    (0, "ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceRulePrecedence"),
)
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceEntry.setStatus("current")


class _Me1200IpmcProfilePrecedenceProfileName_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfilePrecedenceProfileName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfilePrecedenceProfileName_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfilePrecedenceProfileName_Object = MibTableColumn
me1200IpmcProfilePrecedenceProfileName = _Me1200IpmcProfilePrecedenceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1, 1),
    _Me1200IpmcProfilePrecedenceProfileName_Type()
)
me1200IpmcProfilePrecedenceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceProfileName.setStatus("current")


class _Me1200IpmcProfilePrecedenceRulePrecedence_Type(Integer32):
    """Custom type me1200IpmcProfilePrecedenceRulePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200IpmcProfilePrecedenceRulePrecedence_Type.__name__ = "Integer32"
_Me1200IpmcProfilePrecedenceRulePrecedence_Object = MibTableColumn
me1200IpmcProfilePrecedenceRulePrecedence = _Me1200IpmcProfilePrecedenceRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1, 2),
    _Me1200IpmcProfilePrecedenceRulePrecedence_Type()
)
me1200IpmcProfilePrecedenceRulePrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceRulePrecedence.setStatus("current")


class _Me1200IpmcProfilePrecedenceRuleRange_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfilePrecedenceRuleRange based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfilePrecedenceRuleRange_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfilePrecedenceRuleRange_Object = MibTableColumn
me1200IpmcProfilePrecedenceRuleRange = _Me1200IpmcProfilePrecedenceRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1, 3),
    _Me1200IpmcProfilePrecedenceRuleRange_Type()
)
me1200IpmcProfilePrecedenceRuleRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceRuleRange.setStatus("current")


class _Me1200IpmcProfilePrecedenceNextRuleRange_Type(ME1200DisplayString):
    """Custom type me1200IpmcProfilePrecedenceNextRuleRange based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Me1200IpmcProfilePrecedenceNextRuleRange_Type.__name__ = "ME1200DisplayString"
_Me1200IpmcProfilePrecedenceNextRuleRange_Object = MibTableColumn
me1200IpmcProfilePrecedenceNextRuleRange = _Me1200IpmcProfilePrecedenceNextRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1, 4),
    _Me1200IpmcProfilePrecedenceNextRuleRange_Type()
)
me1200IpmcProfilePrecedenceNextRuleRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceNextRuleRange.setStatus("current")
_Me1200IpmcProfilePrecedenceRuleAction_Type = ME1200IpmcProfileRuleActionType
_Me1200IpmcProfilePrecedenceRuleAction_Object = MibTableColumn
me1200IpmcProfilePrecedenceRuleAction = _Me1200IpmcProfilePrecedenceRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1, 5),
    _Me1200IpmcProfilePrecedenceRuleAction_Type()
)
me1200IpmcProfilePrecedenceRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceRuleAction.setStatus("current")
_Me1200IpmcProfilePrecedenceRuleLog_Type = TruthValue
_Me1200IpmcProfilePrecedenceRuleLog_Object = MibTableColumn
me1200IpmcProfilePrecedenceRuleLog = _Me1200IpmcProfilePrecedenceRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 1, 2, 10, 1, 6),
    _Me1200IpmcProfilePrecedenceRuleLog_Type()
)
me1200IpmcProfilePrecedenceRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceRuleLog.setStatus("current")
_Me1200IpmcProfileMIBConformance_ObjectIdentity = ObjectIdentity
me1200IpmcProfileMIBConformance = _Me1200IpmcProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2)
)
_Me1200IpmcProfileMIBCompliances_ObjectIdentity = ObjectIdentity
me1200IpmcProfileMIBCompliances = _Me1200IpmcProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 1)
)
_Me1200IpmcProfileMIBGroups_ObjectIdentity = ObjectIdentity
me1200IpmcProfileMIBGroups = _Me1200IpmcProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2)
)

# Managed Objects groups

me1200IpmcProfileGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 1)
)
me1200IpmcProfileGlobalsInfoGroup.setObjects(
    ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileGlobalsAdminState")
)
if mibBuilder.loadTexts:
    me1200IpmcProfileGlobalsInfoGroup.setStatus("current")

me1200IpmcProfileManagementTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 2)
)
me1200IpmcProfileManagementTableInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementProfileDescription"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementTableInfoGroup.setStatus("current")

me1200IpmcProfileManagementTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 3)
)
me1200IpmcProfileManagementTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementTableRowEditorProfileName"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementTableRowEditorProfileDescription"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileManagementTableRowEditorInfoGroup.setStatus("current")

me1200IpmcProfileIpv4AddressRangeTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 4)
)
me1200IpmcProfileIpv4AddressRangeTableInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeStartAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeEndAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTableInfoGroup.setStatus("current")

me1200IpmcProfileIpv4AddressRangeTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 5)
)
me1200IpmcProfileIpv4AddressRangeTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv4AddressRangeTableRowEditorInfoGroup.setStatus("current")

me1200IpmcProfileIpv6AddressRangeTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 6)
)
me1200IpmcProfileIpv6AddressRangeTableInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeStartAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeEndAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTableInfoGroup.setStatus("current")

me1200IpmcProfileIpv6AddressRangeTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 7)
)
me1200IpmcProfileIpv6AddressRangeTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileIpv6AddressRangeTableRowEditorInfoGroup.setStatus("current")

me1200IpmcProfileRuleTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 8)
)
me1200IpmcProfileRuleTableInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleNextRuleRange"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleRuleAction"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleRuleLog"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableInfoGroup.setStatus("current")

me1200IpmcProfileRuleTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 9)
)
me1200IpmcProfileRuleTableRowEditorInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorProfileName"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorRuleRange"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorNextRuleRange"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorRuleAction"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorRuleLog"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileRuleTableRowEditorInfoGroup.setStatus("current")

me1200IpmcProfilePrecedenceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 2, 10)
)
me1200IpmcProfilePrecedenceTableInfoGroup.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceRuleRange"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceNextRuleRange"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceRuleAction"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceRuleLog"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfilePrecedenceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200IpmcProfileMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 38, 2, 1, 1)
)
me1200IpmcProfileMibCompliance.setObjects(
      *(("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileGlobalsInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementTableInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileManagementTableRowEditorInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeTableInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv4AddressRangeTableRowEditorInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeTableInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileIpv6AddressRangeTableRowEditorInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfileRuleTableRowEditorInfoGroup"),
        ("ME1200-IPMC-PROFILE-MIB", "me1200IpmcProfilePrecedenceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200IpmcProfileMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-IPMC-PROFILE-MIB",
    **{"ME1200IpmcProfileRuleActionType": ME1200IpmcProfileRuleActionType,
       "me1200IpmcProfileMib": me1200IpmcProfileMib,
       "me1200IpmcProfileMIBObjects": me1200IpmcProfileMIBObjects,
       "me1200IpmcProfileConfig": me1200IpmcProfileConfig,
       "me1200IpmcProfileGlobals": me1200IpmcProfileGlobals,
       "me1200IpmcProfileGlobalsAdminState": me1200IpmcProfileGlobalsAdminState,
       "me1200IpmcProfileManagementTable": me1200IpmcProfileManagementTable,
       "me1200IpmcProfileManagementEntry": me1200IpmcProfileManagementEntry,
       "me1200IpmcProfileManagementProfileName": me1200IpmcProfileManagementProfileName,
       "me1200IpmcProfileManagementProfileDescription": me1200IpmcProfileManagementProfileDescription,
       "me1200IpmcProfileManagementAction": me1200IpmcProfileManagementAction,
       "me1200IpmcProfileManagementTableRowEditor": me1200IpmcProfileManagementTableRowEditor,
       "me1200IpmcProfileManagementTableRowEditorProfileName": me1200IpmcProfileManagementTableRowEditorProfileName,
       "me1200IpmcProfileManagementTableRowEditorProfileDescription": me1200IpmcProfileManagementTableRowEditorProfileDescription,
       "me1200IpmcProfileManagementTableRowEditorAction": me1200IpmcProfileManagementTableRowEditorAction,
       "me1200IpmcProfileIpv4AddressRangeTable": me1200IpmcProfileIpv4AddressRangeTable,
       "me1200IpmcProfileIpv4AddressRangeEntry": me1200IpmcProfileIpv4AddressRangeEntry,
       "me1200IpmcProfileIpv4AddressRangeRangeName": me1200IpmcProfileIpv4AddressRangeRangeName,
       "me1200IpmcProfileIpv4AddressRangeStartAddress": me1200IpmcProfileIpv4AddressRangeStartAddress,
       "me1200IpmcProfileIpv4AddressRangeEndAddress": me1200IpmcProfileIpv4AddressRangeEndAddress,
       "me1200IpmcProfileIpv4AddressRangeAction": me1200IpmcProfileIpv4AddressRangeAction,
       "me1200IpmcProfileIpv4AddressRangeTableRowEditor": me1200IpmcProfileIpv4AddressRangeTableRowEditor,
       "me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName": me1200IpmcProfileIpv4AddressRangeTableRowEditorRangeName,
       "me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress": me1200IpmcProfileIpv4AddressRangeTableRowEditorStartAddress,
       "me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress": me1200IpmcProfileIpv4AddressRangeTableRowEditorEndAddress,
       "me1200IpmcProfileIpv4AddressRangeTableRowEditorAction": me1200IpmcProfileIpv4AddressRangeTableRowEditorAction,
       "me1200IpmcProfileIpv6AddressRangeTable": me1200IpmcProfileIpv6AddressRangeTable,
       "me1200IpmcProfileIpv6AddressRangeEntry": me1200IpmcProfileIpv6AddressRangeEntry,
       "me1200IpmcProfileIpv6AddressRangeRangeName": me1200IpmcProfileIpv6AddressRangeRangeName,
       "me1200IpmcProfileIpv6AddressRangeStartAddress": me1200IpmcProfileIpv6AddressRangeStartAddress,
       "me1200IpmcProfileIpv6AddressRangeEndAddress": me1200IpmcProfileIpv6AddressRangeEndAddress,
       "me1200IpmcProfileIpv6AddressRangeAction": me1200IpmcProfileIpv6AddressRangeAction,
       "me1200IpmcProfileIpv6AddressRangeTableRowEditor": me1200IpmcProfileIpv6AddressRangeTableRowEditor,
       "me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName": me1200IpmcProfileIpv6AddressRangeTableRowEditorRangeName,
       "me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress": me1200IpmcProfileIpv6AddressRangeTableRowEditorStartAddress,
       "me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress": me1200IpmcProfileIpv6AddressRangeTableRowEditorEndAddress,
       "me1200IpmcProfileIpv6AddressRangeTableRowEditorAction": me1200IpmcProfileIpv6AddressRangeTableRowEditorAction,
       "me1200IpmcProfileRuleTable": me1200IpmcProfileRuleTable,
       "me1200IpmcProfileRuleEntry": me1200IpmcProfileRuleEntry,
       "me1200IpmcProfileRuleProfileName": me1200IpmcProfileRuleProfileName,
       "me1200IpmcProfileRuleRuleRange": me1200IpmcProfileRuleRuleRange,
       "me1200IpmcProfileRuleNextRuleRange": me1200IpmcProfileRuleNextRuleRange,
       "me1200IpmcProfileRuleRuleAction": me1200IpmcProfileRuleRuleAction,
       "me1200IpmcProfileRuleRuleLog": me1200IpmcProfileRuleRuleLog,
       "me1200IpmcProfileRuleAction": me1200IpmcProfileRuleAction,
       "me1200IpmcProfileRuleTableRowEditor": me1200IpmcProfileRuleTableRowEditor,
       "me1200IpmcProfileRuleTableRowEditorProfileName": me1200IpmcProfileRuleTableRowEditorProfileName,
       "me1200IpmcProfileRuleTableRowEditorRuleRange": me1200IpmcProfileRuleTableRowEditorRuleRange,
       "me1200IpmcProfileRuleTableRowEditorNextRuleRange": me1200IpmcProfileRuleTableRowEditorNextRuleRange,
       "me1200IpmcProfileRuleTableRowEditorRuleAction": me1200IpmcProfileRuleTableRowEditorRuleAction,
       "me1200IpmcProfileRuleTableRowEditorRuleLog": me1200IpmcProfileRuleTableRowEditorRuleLog,
       "me1200IpmcProfileRuleTableRowEditorAction": me1200IpmcProfileRuleTableRowEditorAction,
       "me1200IpmcProfilePrecedenceTable": me1200IpmcProfilePrecedenceTable,
       "me1200IpmcProfilePrecedenceEntry": me1200IpmcProfilePrecedenceEntry,
       "me1200IpmcProfilePrecedenceProfileName": me1200IpmcProfilePrecedenceProfileName,
       "me1200IpmcProfilePrecedenceRulePrecedence": me1200IpmcProfilePrecedenceRulePrecedence,
       "me1200IpmcProfilePrecedenceRuleRange": me1200IpmcProfilePrecedenceRuleRange,
       "me1200IpmcProfilePrecedenceNextRuleRange": me1200IpmcProfilePrecedenceNextRuleRange,
       "me1200IpmcProfilePrecedenceRuleAction": me1200IpmcProfilePrecedenceRuleAction,
       "me1200IpmcProfilePrecedenceRuleLog": me1200IpmcProfilePrecedenceRuleLog,
       "me1200IpmcProfileMIBConformance": me1200IpmcProfileMIBConformance,
       "me1200IpmcProfileMIBCompliances": me1200IpmcProfileMIBCompliances,
       "me1200IpmcProfileMibCompliance": me1200IpmcProfileMibCompliance,
       "me1200IpmcProfileMIBGroups": me1200IpmcProfileMIBGroups,
       "me1200IpmcProfileGlobalsInfoGroup": me1200IpmcProfileGlobalsInfoGroup,
       "me1200IpmcProfileManagementTableInfoGroup": me1200IpmcProfileManagementTableInfoGroup,
       "me1200IpmcProfileManagementTableRowEditorInfoGroup": me1200IpmcProfileManagementTableRowEditorInfoGroup,
       "me1200IpmcProfileIpv4AddressRangeTableInfoGroup": me1200IpmcProfileIpv4AddressRangeTableInfoGroup,
       "me1200IpmcProfileIpv4AddressRangeTableRowEditorInfoGroup": me1200IpmcProfileIpv4AddressRangeTableRowEditorInfoGroup,
       "me1200IpmcProfileIpv6AddressRangeTableInfoGroup": me1200IpmcProfileIpv6AddressRangeTableInfoGroup,
       "me1200IpmcProfileIpv6AddressRangeTableRowEditorInfoGroup": me1200IpmcProfileIpv6AddressRangeTableRowEditorInfoGroup,
       "me1200IpmcProfileRuleTableInfoGroup": me1200IpmcProfileRuleTableInfoGroup,
       "me1200IpmcProfileRuleTableRowEditorInfoGroup": me1200IpmcProfileRuleTableRowEditorInfoGroup,
       "me1200IpmcProfilePrecedenceTableInfoGroup": me1200IpmcProfilePrecedenceTableInfoGroup}
)
