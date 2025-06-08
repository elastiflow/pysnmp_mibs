# SNMP MIB module (CIE1000-IPMC-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-IPMC-PROFILE-MIB.mib
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

(CIE1000DisplayString,
 CIE1000RowEditorState) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000RowEditorState")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000IpmcProfileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38)
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileMib.setRevisions(
        ("2014-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000IpmcProfileRuleActionType(TextualConvention, Integer32):
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

_Cie1000IpmcProfileMibObjects_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileMibObjects = _Cie1000IpmcProfileMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1)
)
_Cie1000IpmcProfileConfig_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileConfig = _Cie1000IpmcProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2)
)
_Cie1000IpmcProfileConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileConfigGlobals = _Cie1000IpmcProfileConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 1)
)
_Cie1000IpmcProfileConfigGlobalsAdminState_Type = TruthValue
_Cie1000IpmcProfileConfigGlobalsAdminState_Object = MibScalar
cie1000IpmcProfileConfigGlobalsAdminState = _Cie1000IpmcProfileConfigGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 1, 1),
    _Cie1000IpmcProfileConfigGlobalsAdminState_Type()
)
cie1000IpmcProfileConfigGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigGlobalsAdminState.setStatus("current")
_Cie1000IpmcProfileConfigMgmtTable_Object = MibTable
cie1000IpmcProfileConfigMgmtTable = _Cie1000IpmcProfileConfigMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtTable.setStatus("current")
_Cie1000IpmcProfileConfigMgmtEntry_Object = MibTableRow
cie1000IpmcProfileConfigMgmtEntry = _Cie1000IpmcProfileConfigMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 2, 1)
)
cie1000IpmcProfileConfigMgmtEntry.setIndexNames(
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtProfileName"),
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtEntry.setStatus("current")


class _Cie1000IpmcProfileConfigMgmtProfileName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigMgmtProfileName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigMgmtProfileName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigMgmtProfileName_Object = MibTableColumn
cie1000IpmcProfileConfigMgmtProfileName = _Cie1000IpmcProfileConfigMgmtProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 2, 1, 1),
    _Cie1000IpmcProfileConfigMgmtProfileName_Type()
)
cie1000IpmcProfileConfigMgmtProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtProfileName.setStatus("current")


class _Cie1000IpmcProfileConfigMgmtProfileDescription_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigMgmtProfileDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000IpmcProfileConfigMgmtProfileDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigMgmtProfileDescription_Object = MibTableColumn
cie1000IpmcProfileConfigMgmtProfileDescription = _Cie1000IpmcProfileConfigMgmtProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 2, 1, 2),
    _Cie1000IpmcProfileConfigMgmtProfileDescription_Type()
)
cie1000IpmcProfileConfigMgmtProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtProfileDescription.setStatus("current")
_Cie1000IpmcProfileConfigMgmtAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigMgmtAction_Object = MibTableColumn
cie1000IpmcProfileConfigMgmtAction = _Cie1000IpmcProfileConfigMgmtAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 2, 1, 100),
    _Cie1000IpmcProfileConfigMgmtAction_Type()
)
cie1000IpmcProfileConfigMgmtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtAction.setStatus("current")
_Cie1000IpmcProfileConfigMgmtTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileConfigMgmtTableRowEditor = _Cie1000IpmcProfileConfigMgmtTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 3)
)


class _Cie1000IpmcProfileConfigMgmtTableRowEditorProfileName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigMgmtTableRowEditorProfileName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigMgmtTableRowEditorProfileName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigMgmtTableRowEditorProfileName_Object = MibScalar
cie1000IpmcProfileConfigMgmtTableRowEditorProfileName = _Cie1000IpmcProfileConfigMgmtTableRowEditorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 3, 1),
    _Cie1000IpmcProfileConfigMgmtTableRowEditorProfileName_Type()
)
cie1000IpmcProfileConfigMgmtTableRowEditorProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtTableRowEditorProfileName.setStatus("current")


class _Cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription_Object = MibScalar
cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription = _Cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 3, 2),
    _Cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription_Type()
)
cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription.setStatus("current")
_Cie1000IpmcProfileConfigMgmtTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigMgmtTableRowEditorAction_Object = MibScalar
cie1000IpmcProfileConfigMgmtTableRowEditorAction = _Cie1000IpmcProfileConfigMgmtTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 3, 100),
    _Cie1000IpmcProfileConfigMgmtTableRowEditorAction_Type()
)
cie1000IpmcProfileConfigMgmtTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtTableRowEditorAction.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeTable_Object = MibTable
cie1000IpmcProfileConfigIpv4AddrRangeTable = _Cie1000IpmcProfileConfigIpv4AddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTable.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeEntry_Object = MibTableRow
cie1000IpmcProfileConfigIpv4AddrRangeEntry = _Cie1000IpmcProfileConfigIpv4AddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 4, 1)
)
cie1000IpmcProfileConfigIpv4AddrRangeEntry.setIndexNames(
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeRangeName"),
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeEntry.setStatus("current")


class _Cie1000IpmcProfileConfigIpv4AddrRangeRangeName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigIpv4AddrRangeRangeName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigIpv4AddrRangeRangeName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigIpv4AddrRangeRangeName_Object = MibTableColumn
cie1000IpmcProfileConfigIpv4AddrRangeRangeName = _Cie1000IpmcProfileConfigIpv4AddrRangeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 4, 1, 1),
    _Cie1000IpmcProfileConfigIpv4AddrRangeRangeName_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeRangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeRangeName.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeStartAddress_Type = IpAddress
_Cie1000IpmcProfileConfigIpv4AddrRangeStartAddress_Object = MibTableColumn
cie1000IpmcProfileConfigIpv4AddrRangeStartAddress = _Cie1000IpmcProfileConfigIpv4AddrRangeStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 4, 1, 2),
    _Cie1000IpmcProfileConfigIpv4AddrRangeStartAddress_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeStartAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeEndAddress_Type = IpAddress
_Cie1000IpmcProfileConfigIpv4AddrRangeEndAddress_Object = MibTableColumn
cie1000IpmcProfileConfigIpv4AddrRangeEndAddress = _Cie1000IpmcProfileConfigIpv4AddrRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 4, 1, 3),
    _Cie1000IpmcProfileConfigIpv4AddrRangeEndAddress_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeEndAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigIpv4AddrRangeAction_Object = MibTableColumn
cie1000IpmcProfileConfigIpv4AddrRangeAction = _Cie1000IpmcProfileConfigIpv4AddrRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 4, 1, 100),
    _Cie1000IpmcProfileConfigIpv4AddrRangeAction_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeAction.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditor = _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 5)
)


class _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName_Object = MibScalar
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName = _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 5, 1),
    _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress_Type = IpAddress
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress_Object = MibScalar
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress = _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 5, 2),
    _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress_Type = IpAddress
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress_Object = MibScalar
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress = _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 5, 3),
    _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction_Object = MibScalar
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction = _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 5, 100),
    _Cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction_Type()
)
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeTable_Object = MibTable
cie1000IpmcProfileConfigIpv6AddrRangeTable = _Cie1000IpmcProfileConfigIpv6AddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTable.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeEntry_Object = MibTableRow
cie1000IpmcProfileConfigIpv6AddrRangeEntry = _Cie1000IpmcProfileConfigIpv6AddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 6, 1)
)
cie1000IpmcProfileConfigIpv6AddrRangeEntry.setIndexNames(
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeRangeName"),
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeEntry.setStatus("current")


class _Cie1000IpmcProfileConfigIpv6AddrRangeRangeName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigIpv6AddrRangeRangeName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigIpv6AddrRangeRangeName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigIpv6AddrRangeRangeName_Object = MibTableColumn
cie1000IpmcProfileConfigIpv6AddrRangeRangeName = _Cie1000IpmcProfileConfigIpv6AddrRangeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 6, 1, 1),
    _Cie1000IpmcProfileConfigIpv6AddrRangeRangeName_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeRangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeRangeName.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeStartAddress_Type = InetAddressIPv6
_Cie1000IpmcProfileConfigIpv6AddrRangeStartAddress_Object = MibTableColumn
cie1000IpmcProfileConfigIpv6AddrRangeStartAddress = _Cie1000IpmcProfileConfigIpv6AddrRangeStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 6, 1, 2),
    _Cie1000IpmcProfileConfigIpv6AddrRangeStartAddress_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeStartAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeEndAddress_Type = InetAddressIPv6
_Cie1000IpmcProfileConfigIpv6AddrRangeEndAddress_Object = MibTableColumn
cie1000IpmcProfileConfigIpv6AddrRangeEndAddress = _Cie1000IpmcProfileConfigIpv6AddrRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 6, 1, 3),
    _Cie1000IpmcProfileConfigIpv6AddrRangeEndAddress_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeEndAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigIpv6AddrRangeAction_Object = MibTableColumn
cie1000IpmcProfileConfigIpv6AddrRangeAction = _Cie1000IpmcProfileConfigIpv6AddrRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 6, 1, 100),
    _Cie1000IpmcProfileConfigIpv6AddrRangeAction_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeAction.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditor = _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 7)
)


class _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName_Object = MibScalar
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName = _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 7, 1),
    _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress_Type = InetAddressIPv6
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress_Object = MibScalar
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress = _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 7, 2),
    _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress_Type = InetAddressIPv6
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress_Object = MibScalar
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress = _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 7, 3),
    _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress.setStatus("current")
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction_Object = MibScalar
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction = _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 7, 100),
    _Cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction_Type()
)
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction.setStatus("current")
_Cie1000IpmcProfileConfigRuleTable_Object = MibTable
cie1000IpmcProfileConfigRuleTable = _Cie1000IpmcProfileConfigRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTable.setStatus("current")
_Cie1000IpmcProfileConfigRuleEntry_Object = MibTableRow
cie1000IpmcProfileConfigRuleEntry = _Cie1000IpmcProfileConfigRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1)
)
cie1000IpmcProfileConfigRuleEntry.setIndexNames(
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleProfileName"),
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleRuleRange"),
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleEntry.setStatus("current")


class _Cie1000IpmcProfileConfigRuleProfileName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigRuleProfileName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigRuleProfileName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigRuleProfileName_Object = MibTableColumn
cie1000IpmcProfileConfigRuleProfileName = _Cie1000IpmcProfileConfigRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1, 1),
    _Cie1000IpmcProfileConfigRuleProfileName_Type()
)
cie1000IpmcProfileConfigRuleProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleProfileName.setStatus("current")


class _Cie1000IpmcProfileConfigRuleRuleRange_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigRuleRuleRange based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigRuleRuleRange_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigRuleRuleRange_Object = MibTableColumn
cie1000IpmcProfileConfigRuleRuleRange = _Cie1000IpmcProfileConfigRuleRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1, 2),
    _Cie1000IpmcProfileConfigRuleRuleRange_Type()
)
cie1000IpmcProfileConfigRuleRuleRange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleRuleRange.setStatus("current")


class _Cie1000IpmcProfileConfigRuleNextRuleRange_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigRuleNextRuleRange based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigRuleNextRuleRange_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigRuleNextRuleRange_Object = MibTableColumn
cie1000IpmcProfileConfigRuleNextRuleRange = _Cie1000IpmcProfileConfigRuleNextRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1, 3),
    _Cie1000IpmcProfileConfigRuleNextRuleRange_Type()
)
cie1000IpmcProfileConfigRuleNextRuleRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleNextRuleRange.setStatus("current")
_Cie1000IpmcProfileConfigRuleRuleAction_Type = CIE1000IpmcProfileRuleActionType
_Cie1000IpmcProfileConfigRuleRuleAction_Object = MibTableColumn
cie1000IpmcProfileConfigRuleRuleAction = _Cie1000IpmcProfileConfigRuleRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1, 4),
    _Cie1000IpmcProfileConfigRuleRuleAction_Type()
)
cie1000IpmcProfileConfigRuleRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleRuleAction.setStatus("current")
_Cie1000IpmcProfileConfigRuleRuleLog_Type = TruthValue
_Cie1000IpmcProfileConfigRuleRuleLog_Object = MibTableColumn
cie1000IpmcProfileConfigRuleRuleLog = _Cie1000IpmcProfileConfigRuleRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1, 5),
    _Cie1000IpmcProfileConfigRuleRuleLog_Type()
)
cie1000IpmcProfileConfigRuleRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleRuleLog.setStatus("current")
_Cie1000IpmcProfileConfigRuleAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigRuleAction_Object = MibTableColumn
cie1000IpmcProfileConfigRuleAction = _Cie1000IpmcProfileConfigRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 8, 1, 100),
    _Cie1000IpmcProfileConfigRuleAction_Type()
)
cie1000IpmcProfileConfigRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleAction.setStatus("current")
_Cie1000IpmcProfileConfigRuleTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileConfigRuleTableRowEditor = _Cie1000IpmcProfileConfigRuleTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9)
)


class _Cie1000IpmcProfileConfigRuleTableRowEditorProfileName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigRuleTableRowEditorProfileName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigRuleTableRowEditorProfileName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigRuleTableRowEditorProfileName_Object = MibScalar
cie1000IpmcProfileConfigRuleTableRowEditorProfileName = _Cie1000IpmcProfileConfigRuleTableRowEditorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9, 1),
    _Cie1000IpmcProfileConfigRuleTableRowEditorProfileName_Type()
)
cie1000IpmcProfileConfigRuleTableRowEditorProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorProfileName.setStatus("current")


class _Cie1000IpmcProfileConfigRuleTableRowEditorRuleRange_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigRuleTableRowEditorRuleRange based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigRuleTableRowEditorRuleRange_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigRuleTableRowEditorRuleRange_Object = MibScalar
cie1000IpmcProfileConfigRuleTableRowEditorRuleRange = _Cie1000IpmcProfileConfigRuleTableRowEditorRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9, 2),
    _Cie1000IpmcProfileConfigRuleTableRowEditorRuleRange_Type()
)
cie1000IpmcProfileConfigRuleTableRowEditorRuleRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorRuleRange.setStatus("current")


class _Cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange_Object = MibScalar
cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange = _Cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9, 3),
    _Cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange_Type()
)
cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange.setStatus("current")
_Cie1000IpmcProfileConfigRuleTableRowEditorRuleAction_Type = CIE1000IpmcProfileRuleActionType
_Cie1000IpmcProfileConfigRuleTableRowEditorRuleAction_Object = MibScalar
cie1000IpmcProfileConfigRuleTableRowEditorRuleAction = _Cie1000IpmcProfileConfigRuleTableRowEditorRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9, 4),
    _Cie1000IpmcProfileConfigRuleTableRowEditorRuleAction_Type()
)
cie1000IpmcProfileConfigRuleTableRowEditorRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorRuleAction.setStatus("current")
_Cie1000IpmcProfileConfigRuleTableRowEditorRuleLog_Type = TruthValue
_Cie1000IpmcProfileConfigRuleTableRowEditorRuleLog_Object = MibScalar
cie1000IpmcProfileConfigRuleTableRowEditorRuleLog = _Cie1000IpmcProfileConfigRuleTableRowEditorRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9, 5),
    _Cie1000IpmcProfileConfigRuleTableRowEditorRuleLog_Type()
)
cie1000IpmcProfileConfigRuleTableRowEditorRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorRuleLog.setStatus("current")
_Cie1000IpmcProfileConfigRuleTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000IpmcProfileConfigRuleTableRowEditorAction_Object = MibScalar
cie1000IpmcProfileConfigRuleTableRowEditorAction = _Cie1000IpmcProfileConfigRuleTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 9, 100),
    _Cie1000IpmcProfileConfigRuleTableRowEditorAction_Type()
)
cie1000IpmcProfileConfigRuleTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorAction.setStatus("current")
_Cie1000IpmcProfileConfigPrecedenceTable_Object = MibTable
cie1000IpmcProfileConfigPrecedenceTable = _Cie1000IpmcProfileConfigPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceTable.setStatus("current")
_Cie1000IpmcProfileConfigPrecedenceEntry_Object = MibTableRow
cie1000IpmcProfileConfigPrecedenceEntry = _Cie1000IpmcProfileConfigPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1)
)
cie1000IpmcProfileConfigPrecedenceEntry.setIndexNames(
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceProfileName"),
    (0, "CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceRulePrecedence"),
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceEntry.setStatus("current")


class _Cie1000IpmcProfileConfigPrecedenceProfileName_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigPrecedenceProfileName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigPrecedenceProfileName_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigPrecedenceProfileName_Object = MibTableColumn
cie1000IpmcProfileConfigPrecedenceProfileName = _Cie1000IpmcProfileConfigPrecedenceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1, 1),
    _Cie1000IpmcProfileConfigPrecedenceProfileName_Type()
)
cie1000IpmcProfileConfigPrecedenceProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceProfileName.setStatus("current")


class _Cie1000IpmcProfileConfigPrecedenceRulePrecedence_Type(Integer32):
    """Custom type cie1000IpmcProfileConfigPrecedenceRulePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cie1000IpmcProfileConfigPrecedenceRulePrecedence_Type.__name__ = "Integer32"
_Cie1000IpmcProfileConfigPrecedenceRulePrecedence_Object = MibTableColumn
cie1000IpmcProfileConfigPrecedenceRulePrecedence = _Cie1000IpmcProfileConfigPrecedenceRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1, 2),
    _Cie1000IpmcProfileConfigPrecedenceRulePrecedence_Type()
)
cie1000IpmcProfileConfigPrecedenceRulePrecedence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceRulePrecedence.setStatus("current")


class _Cie1000IpmcProfileConfigPrecedenceRuleRange_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigPrecedenceRuleRange based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigPrecedenceRuleRange_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigPrecedenceRuleRange_Object = MibTableColumn
cie1000IpmcProfileConfigPrecedenceRuleRange = _Cie1000IpmcProfileConfigPrecedenceRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1, 3),
    _Cie1000IpmcProfileConfigPrecedenceRuleRange_Type()
)
cie1000IpmcProfileConfigPrecedenceRuleRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceRuleRange.setStatus("current")


class _Cie1000IpmcProfileConfigPrecedenceNextRuleRange_Type(CIE1000DisplayString):
    """Custom type cie1000IpmcProfileConfigPrecedenceNextRuleRange based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000IpmcProfileConfigPrecedenceNextRuleRange_Type.__name__ = "CIE1000DisplayString"
_Cie1000IpmcProfileConfigPrecedenceNextRuleRange_Object = MibTableColumn
cie1000IpmcProfileConfigPrecedenceNextRuleRange = _Cie1000IpmcProfileConfigPrecedenceNextRuleRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1, 4),
    _Cie1000IpmcProfileConfigPrecedenceNextRuleRange_Type()
)
cie1000IpmcProfileConfigPrecedenceNextRuleRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceNextRuleRange.setStatus("current")
_Cie1000IpmcProfileConfigPrecedenceRuleAction_Type = CIE1000IpmcProfileRuleActionType
_Cie1000IpmcProfileConfigPrecedenceRuleAction_Object = MibTableColumn
cie1000IpmcProfileConfigPrecedenceRuleAction = _Cie1000IpmcProfileConfigPrecedenceRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1, 5),
    _Cie1000IpmcProfileConfigPrecedenceRuleAction_Type()
)
cie1000IpmcProfileConfigPrecedenceRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceRuleAction.setStatus("current")
_Cie1000IpmcProfileConfigPrecedenceRuleLog_Type = TruthValue
_Cie1000IpmcProfileConfigPrecedenceRuleLog_Object = MibTableColumn
cie1000IpmcProfileConfigPrecedenceRuleLog = _Cie1000IpmcProfileConfigPrecedenceRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 1, 2, 10, 1, 6),
    _Cie1000IpmcProfileConfigPrecedenceRuleLog_Type()
)
cie1000IpmcProfileConfigPrecedenceRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceRuleLog.setStatus("current")
_Cie1000IpmcProfileMibConformance_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileMibConformance = _Cie1000IpmcProfileMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2)
)
_Cie1000IpmcProfileMibCompliances_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileMibCompliances = _Cie1000IpmcProfileMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 1)
)
_Cie1000IpmcProfileMibGroups_ObjectIdentity = ObjectIdentity
cie1000IpmcProfileMibGroups = _Cie1000IpmcProfileMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2)
)

# Managed Objects groups

cie1000IpmcProfileConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 1)
)
cie1000IpmcProfileConfigGlobalsInfoGroup.setObjects(
    ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigGlobalsAdminState")
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigGlobalsInfoGroup.setStatus("current")

cie1000IpmcProfileConfigMgmtTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 2)
)
cie1000IpmcProfileConfigMgmtTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtProfileName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtProfileDescription"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtTableInfoGroup.setStatus("current")

cie1000IpmcProfileConfigMgmtTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 3)
)
cie1000IpmcProfileConfigMgmtTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtTableRowEditorProfileName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigMgmtTableRowEditorInfoGroup.setStatus("current")

cie1000IpmcProfileConfigIpv4AddrRangeTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 4)
)
cie1000IpmcProfileConfigIpv4AddrRangeTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeRangeName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeStartAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeEndAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTableInfoGroup.setStatus("current")

cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 5)
)
cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorInfoGroup.setStatus("current")

cie1000IpmcProfileConfigIpv6AddrRangeTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 6)
)
cie1000IpmcProfileConfigIpv6AddrRangeTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeRangeName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeStartAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeEndAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTableInfoGroup.setStatus("current")

cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 7)
)
cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorInfoGroup.setStatus("current")

cie1000IpmcProfileConfigRuleTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 8)
)
cie1000IpmcProfileConfigRuleTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleProfileName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleRuleRange"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleNextRuleRange"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleRuleAction"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleRuleLog"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableInfoGroup.setStatus("current")

cie1000IpmcProfileConfigRuleTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 9)
)
cie1000IpmcProfileConfigRuleTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorProfileName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorRuleRange"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorRuleAction"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorRuleLog"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigRuleTableRowEditorInfoGroup.setStatus("current")

cie1000IpmcProfileConfigPrecedenceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 2, 10)
)
cie1000IpmcProfileConfigPrecedenceTableInfoGroup.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceProfileName"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceRulePrecedence"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceRuleRange"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceNextRuleRange"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceRuleAction"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceRuleLog"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileConfigPrecedenceTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000IpmcProfileMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 38, 2, 1, 1)
)
cie1000IpmcProfileMibCompliance.setObjects(
      *(("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigGlobalsInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtTableInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigMgmtTableRowEditorInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeTableInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeTableInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigRuleTableRowEditorInfoGroup"),
        ("CIE1000-IPMC-PROFILE-MIB", "cie1000IpmcProfileConfigPrecedenceTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000IpmcProfileMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-IPMC-PROFILE-MIB",
    **{"CIE1000IpmcProfileRuleActionType": CIE1000IpmcProfileRuleActionType,
       "cie1000IpmcProfileMib": cie1000IpmcProfileMib,
       "cie1000IpmcProfileMibObjects": cie1000IpmcProfileMibObjects,
       "cie1000IpmcProfileConfig": cie1000IpmcProfileConfig,
       "cie1000IpmcProfileConfigGlobals": cie1000IpmcProfileConfigGlobals,
       "cie1000IpmcProfileConfigGlobalsAdminState": cie1000IpmcProfileConfigGlobalsAdminState,
       "cie1000IpmcProfileConfigMgmtTable": cie1000IpmcProfileConfigMgmtTable,
       "cie1000IpmcProfileConfigMgmtEntry": cie1000IpmcProfileConfigMgmtEntry,
       "cie1000IpmcProfileConfigMgmtProfileName": cie1000IpmcProfileConfigMgmtProfileName,
       "cie1000IpmcProfileConfigMgmtProfileDescription": cie1000IpmcProfileConfigMgmtProfileDescription,
       "cie1000IpmcProfileConfigMgmtAction": cie1000IpmcProfileConfigMgmtAction,
       "cie1000IpmcProfileConfigMgmtTableRowEditor": cie1000IpmcProfileConfigMgmtTableRowEditor,
       "cie1000IpmcProfileConfigMgmtTableRowEditorProfileName": cie1000IpmcProfileConfigMgmtTableRowEditorProfileName,
       "cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription": cie1000IpmcProfileConfigMgmtTableRowEditorProfileDescription,
       "cie1000IpmcProfileConfigMgmtTableRowEditorAction": cie1000IpmcProfileConfigMgmtTableRowEditorAction,
       "cie1000IpmcProfileConfigIpv4AddrRangeTable": cie1000IpmcProfileConfigIpv4AddrRangeTable,
       "cie1000IpmcProfileConfigIpv4AddrRangeEntry": cie1000IpmcProfileConfigIpv4AddrRangeEntry,
       "cie1000IpmcProfileConfigIpv4AddrRangeRangeName": cie1000IpmcProfileConfigIpv4AddrRangeRangeName,
       "cie1000IpmcProfileConfigIpv4AddrRangeStartAddress": cie1000IpmcProfileConfigIpv4AddrRangeStartAddress,
       "cie1000IpmcProfileConfigIpv4AddrRangeEndAddress": cie1000IpmcProfileConfigIpv4AddrRangeEndAddress,
       "cie1000IpmcProfileConfigIpv4AddrRangeAction": cie1000IpmcProfileConfigIpv4AddrRangeAction,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditor": cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditor,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName": cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorRangeName,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress": cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorStartAddress,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress": cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorEndAddress,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction": cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorAction,
       "cie1000IpmcProfileConfigIpv6AddrRangeTable": cie1000IpmcProfileConfigIpv6AddrRangeTable,
       "cie1000IpmcProfileConfigIpv6AddrRangeEntry": cie1000IpmcProfileConfigIpv6AddrRangeEntry,
       "cie1000IpmcProfileConfigIpv6AddrRangeRangeName": cie1000IpmcProfileConfigIpv6AddrRangeRangeName,
       "cie1000IpmcProfileConfigIpv6AddrRangeStartAddress": cie1000IpmcProfileConfigIpv6AddrRangeStartAddress,
       "cie1000IpmcProfileConfigIpv6AddrRangeEndAddress": cie1000IpmcProfileConfigIpv6AddrRangeEndAddress,
       "cie1000IpmcProfileConfigIpv6AddrRangeAction": cie1000IpmcProfileConfigIpv6AddrRangeAction,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditor": cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditor,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName": cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorRangeName,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress": cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorStartAddress,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress": cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorEndAddress,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction": cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorAction,
       "cie1000IpmcProfileConfigRuleTable": cie1000IpmcProfileConfigRuleTable,
       "cie1000IpmcProfileConfigRuleEntry": cie1000IpmcProfileConfigRuleEntry,
       "cie1000IpmcProfileConfigRuleProfileName": cie1000IpmcProfileConfigRuleProfileName,
       "cie1000IpmcProfileConfigRuleRuleRange": cie1000IpmcProfileConfigRuleRuleRange,
       "cie1000IpmcProfileConfigRuleNextRuleRange": cie1000IpmcProfileConfigRuleNextRuleRange,
       "cie1000IpmcProfileConfigRuleRuleAction": cie1000IpmcProfileConfigRuleRuleAction,
       "cie1000IpmcProfileConfigRuleRuleLog": cie1000IpmcProfileConfigRuleRuleLog,
       "cie1000IpmcProfileConfigRuleAction": cie1000IpmcProfileConfigRuleAction,
       "cie1000IpmcProfileConfigRuleTableRowEditor": cie1000IpmcProfileConfigRuleTableRowEditor,
       "cie1000IpmcProfileConfigRuleTableRowEditorProfileName": cie1000IpmcProfileConfigRuleTableRowEditorProfileName,
       "cie1000IpmcProfileConfigRuleTableRowEditorRuleRange": cie1000IpmcProfileConfigRuleTableRowEditorRuleRange,
       "cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange": cie1000IpmcProfileConfigRuleTableRowEditorNextRuleRange,
       "cie1000IpmcProfileConfigRuleTableRowEditorRuleAction": cie1000IpmcProfileConfigRuleTableRowEditorRuleAction,
       "cie1000IpmcProfileConfigRuleTableRowEditorRuleLog": cie1000IpmcProfileConfigRuleTableRowEditorRuleLog,
       "cie1000IpmcProfileConfigRuleTableRowEditorAction": cie1000IpmcProfileConfigRuleTableRowEditorAction,
       "cie1000IpmcProfileConfigPrecedenceTable": cie1000IpmcProfileConfigPrecedenceTable,
       "cie1000IpmcProfileConfigPrecedenceEntry": cie1000IpmcProfileConfigPrecedenceEntry,
       "cie1000IpmcProfileConfigPrecedenceProfileName": cie1000IpmcProfileConfigPrecedenceProfileName,
       "cie1000IpmcProfileConfigPrecedenceRulePrecedence": cie1000IpmcProfileConfigPrecedenceRulePrecedence,
       "cie1000IpmcProfileConfigPrecedenceRuleRange": cie1000IpmcProfileConfigPrecedenceRuleRange,
       "cie1000IpmcProfileConfigPrecedenceNextRuleRange": cie1000IpmcProfileConfigPrecedenceNextRuleRange,
       "cie1000IpmcProfileConfigPrecedenceRuleAction": cie1000IpmcProfileConfigPrecedenceRuleAction,
       "cie1000IpmcProfileConfigPrecedenceRuleLog": cie1000IpmcProfileConfigPrecedenceRuleLog,
       "cie1000IpmcProfileMibConformance": cie1000IpmcProfileMibConformance,
       "cie1000IpmcProfileMibCompliances": cie1000IpmcProfileMibCompliances,
       "cie1000IpmcProfileMibCompliance": cie1000IpmcProfileMibCompliance,
       "cie1000IpmcProfileMibGroups": cie1000IpmcProfileMibGroups,
       "cie1000IpmcProfileConfigGlobalsInfoGroup": cie1000IpmcProfileConfigGlobalsInfoGroup,
       "cie1000IpmcProfileConfigMgmtTableInfoGroup": cie1000IpmcProfileConfigMgmtTableInfoGroup,
       "cie1000IpmcProfileConfigMgmtTableRowEditorInfoGroup": cie1000IpmcProfileConfigMgmtTableRowEditorInfoGroup,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableInfoGroup": cie1000IpmcProfileConfigIpv4AddrRangeTableInfoGroup,
       "cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorInfoGroup": cie1000IpmcProfileConfigIpv4AddrRangeTableRowEditorInfoGroup,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableInfoGroup": cie1000IpmcProfileConfigIpv6AddrRangeTableInfoGroup,
       "cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorInfoGroup": cie1000IpmcProfileConfigIpv6AddrRangeTableRowEditorInfoGroup,
       "cie1000IpmcProfileConfigRuleTableInfoGroup": cie1000IpmcProfileConfigRuleTableInfoGroup,
       "cie1000IpmcProfileConfigRuleTableRowEditorInfoGroup": cie1000IpmcProfileConfigRuleTableRowEditorInfoGroup,
       "cie1000IpmcProfileConfigPrecedenceTableInfoGroup": cie1000IpmcProfileConfigPrecedenceTableInfoGroup}
)
