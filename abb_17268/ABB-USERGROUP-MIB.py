# SNMP MIB module (ABB-USERGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/ABB-USERGROUP-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

(hmConfiguration,) = mibBuilder.importSymbols(
    "ABB-PRIVATE-MIB",
    "hmConfiguration")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MemberID(OctetString):
    """Custom type MemberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmUserGroup_ObjectIdentity = ObjectIdentity
hmUserGroup = _HmUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3)
)
_HmUserGroupTable_Object = MibTable
hmUserGroupTable = _HmUserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 1)
)
if mibBuilder.loadTexts:
    hmUserGroupTable.setStatus("mandatory")
_HmUserGroupEntry_Object = MibTableRow
hmUserGroupEntry = _HmUserGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 1, 1)
)
hmUserGroupEntry.setIndexNames(
    (0, "ABB-USERGROUP-MIB", "hmUserGroupID"),
)
if mibBuilder.loadTexts:
    hmUserGroupEntry.setStatus("mandatory")
_HmUserGroupID_Type = Integer32
_HmUserGroupID_Object = MibTableColumn
hmUserGroupID = _HmUserGroupID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 1, 1, 1),
    _HmUserGroupID_Type()
)
hmUserGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmUserGroupID.setStatus("mandatory")
_HmUserGroupDescription_Type = DisplayString
_HmUserGroupDescription_Object = MibTableColumn
hmUserGroupDescription = _HmUserGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 1, 1, 2),
    _HmUserGroupDescription_Type()
)
hmUserGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmUserGroupDescription.setStatus("mandatory")


class _HmUserGroupRestricted_Type(Integer32):
    """Custom type hmUserGroupRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_HmUserGroupRestricted_Type.__name__ = "Integer32"
_HmUserGroupRestricted_Object = MibTableColumn
hmUserGroupRestricted = _HmUserGroupRestricted_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 1, 1, 3),
    _HmUserGroupRestricted_Type()
)
hmUserGroupRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmUserGroupRestricted.setStatus("mandatory")


class _HmUserGroupSecAction_Type(Integer32):
    """Custom type hmUserGroupSecAction based on Integer32"""
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
          ("trapOnly", 2),
          ("portDisable", 3))
    )


_HmUserGroupSecAction_Type.__name__ = "Integer32"
_HmUserGroupSecAction_Object = MibTableColumn
hmUserGroupSecAction = _HmUserGroupSecAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 1, 1, 4),
    _HmUserGroupSecAction_Type()
)
hmUserGroupSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmUserGroupSecAction.setStatus("mandatory")
_HmUserGroupMemberTable_Object = MibTable
hmUserGroupMemberTable = _HmUserGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 2)
)
if mibBuilder.loadTexts:
    hmUserGroupMemberTable.setStatus("mandatory")
_HmUserGroupMemberEntry_Object = MibTableRow
hmUserGroupMemberEntry = _HmUserGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 2, 1)
)
hmUserGroupMemberEntry.setIndexNames(
    (0, "ABB-USERGROUP-MIB", "hmUserGroupMemberGroupID"),
    (0, "ABB-USERGROUP-MIB", "hmUserGroupMemberUserID"),
)
if mibBuilder.loadTexts:
    hmUserGroupMemberEntry.setStatus("mandatory")
_HmUserGroupMemberGroupID_Type = Integer32
_HmUserGroupMemberGroupID_Object = MibTableColumn
hmUserGroupMemberGroupID = _HmUserGroupMemberGroupID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 2, 1, 1),
    _HmUserGroupMemberGroupID_Type()
)
hmUserGroupMemberGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmUserGroupMemberGroupID.setStatus("mandatory")
_HmUserGroupMemberUserID_Type = MemberID
_HmUserGroupMemberUserID_Object = MibTableColumn
hmUserGroupMemberUserID = _HmUserGroupMemberUserID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 2, 1, 2),
    _HmUserGroupMemberUserID_Type()
)
hmUserGroupMemberUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmUserGroupMemberUserID.setStatus("mandatory")
_HmUserTable_Object = MibTable
hmUserTable = _HmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 3)
)
if mibBuilder.loadTexts:
    hmUserTable.setStatus("mandatory")
_HmUserEntry_Object = MibTableRow
hmUserEntry = _HmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 3, 1)
)
hmUserEntry.setIndexNames(
    (0, "ABB-USERGROUP-MIB", "hmUserID"),
)
if mibBuilder.loadTexts:
    hmUserEntry.setStatus("mandatory")
_HmUserID_Type = MemberID
_HmUserID_Object = MibTableColumn
hmUserID = _HmUserID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 3, 1, 1),
    _HmUserID_Type()
)
hmUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmUserID.setStatus("mandatory")


class _HmUserRestricted_Type(Integer32):
    """Custom type hmUserRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_HmUserRestricted_Type.__name__ = "Integer32"
_HmUserRestricted_Object = MibTableColumn
hmUserRestricted = _HmUserRestricted_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 3, 1, 2),
    _HmUserRestricted_Type()
)
hmUserRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmUserRestricted.setStatus("mandatory")
_HmPortSecurityTable_Object = MibTable
hmPortSecurityTable = _HmPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4)
)
if mibBuilder.loadTexts:
    hmPortSecurityTable.setStatus("mandatory")
_HmPortSecurityEntry_Object = MibTableRow
hmPortSecurityEntry = _HmPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1)
)
hmPortSecurityEntry.setIndexNames(
    (0, "ABB-USERGROUP-MIB", "hmPortSecSlotID"),
    (0, "ABB-USERGROUP-MIB", "hmPortSecPortID"),
)
if mibBuilder.loadTexts:
    hmPortSecurityEntry.setStatus("mandatory")


class _HmPortSecSlotID_Type(Integer32):
    """Custom type hmPortSecSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HmPortSecSlotID_Type.__name__ = "Integer32"
_HmPortSecSlotID_Object = MibTableColumn
hmPortSecSlotID = _HmPortSecSlotID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 1),
    _HmPortSecSlotID_Type()
)
hmPortSecSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecSlotID.setStatus("mandatory")


class _HmPortSecPortID_Type(Integer32):
    """Custom type hmPortSecPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmPortSecPortID_Type.__name__ = "Integer32"
_HmPortSecPortID_Object = MibTableColumn
hmPortSecPortID = _HmPortSecPortID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 2),
    _HmPortSecPortID_Type()
)
hmPortSecPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecPortID.setStatus("mandatory")


class _HmPortSecPermission_Type(Integer32):
    """Custom type hmPortSecPermission based on Integer32"""
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
        *(("user", 1),
          ("group", 2),
          ("known", 3),
          ("world", 4),
          ("uplink", 5))
    )


_HmPortSecPermission_Type.__name__ = "Integer32"
_HmPortSecPermission_Object = MibTableColumn
hmPortSecPermission = _HmPortSecPermission_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 3),
    _HmPortSecPermission_Type()
)
hmPortSecPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecPermission.setStatus("mandatory")
_HmPortSecAllowedUserID_Type = MemberID
_HmPortSecAllowedUserID_Object = MibTableColumn
hmPortSecAllowedUserID = _HmPortSecAllowedUserID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 4),
    _HmPortSecAllowedUserID_Type()
)
hmPortSecAllowedUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecAllowedUserID.setStatus("mandatory")


class _HmPortSecAllowedGroupIDs_Type(OctetString):
    """Custom type hmPortSecAllowedGroupIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_HmPortSecAllowedGroupIDs_Type.__name__ = "OctetString"
_HmPortSecAllowedGroupIDs_Object = MibTableColumn
hmPortSecAllowedGroupIDs = _HmPortSecAllowedGroupIDs_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 5),
    _HmPortSecAllowedGroupIDs_Type()
)
hmPortSecAllowedGroupIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecAllowedGroupIDs.setStatus("mandatory")
_HmPortSecConnectedUserID_Type = MemberID
_HmPortSecConnectedUserID_Object = MibTableColumn
hmPortSecConnectedUserID = _HmPortSecConnectedUserID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 6),
    _HmPortSecConnectedUserID_Type()
)
hmPortSecConnectedUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecConnectedUserID.setStatus("mandatory")


class _HmPortSecAction_Type(Integer32):
    """Custom type hmPortSecAction based on Integer32"""
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
          ("trapOnly", 2),
          ("portDisable", 3))
    )


_HmPortSecAction_Type.__name__ = "Integer32"
_HmPortSecAction_Object = MibTableColumn
hmPortSecAction = _HmPortSecAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 7),
    _HmPortSecAction_Type()
)
hmPortSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecAction.setStatus("mandatory")


class _HmPortSecAutoReconfigure_Type(Integer32):
    """Custom type hmPortSecAutoReconfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_HmPortSecAutoReconfigure_Type.__name__ = "Integer32"
_HmPortSecAutoReconfigure_Object = MibTableColumn
hmPortSecAutoReconfigure = _HmPortSecAutoReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 8),
    _HmPortSecAutoReconfigure_Type()
)
hmPortSecAutoReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecAutoReconfigure.setStatus("mandatory")


class _HmPortSecPortStatus_Type(Integer32):
    """Custom type hmPortSecPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("enabledWithWrongAddr", 3))
    )


_HmPortSecPortStatus_Type.__name__ = "Integer32"
_HmPortSecPortStatus_Object = MibTableColumn
hmPortSecPortStatus = _HmPortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 9),
    _HmPortSecPortStatus_Type()
)
hmPortSecPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecPortStatus.setStatus("mandatory")
_HmPortSecAllowedUserIPID_Type = IpAddress
_HmPortSecAllowedUserIPID_Object = MibTableColumn
hmPortSecAllowedUserIPID = _HmPortSecAllowedUserIPID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 4, 1, 10),
    _HmPortSecAllowedUserIPID_Type()
)
hmPortSecAllowedUserIPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecAllowedUserIPID.setStatus("mandatory")


class _HmUserGroupSecurityAction_Type(Integer32):
    """Custom type hmUserGroupSecurityAction based on Integer32"""
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
          ("trapOnly", 2),
          ("portDisable", 3))
    )


_HmUserGroupSecurityAction_Type.__name__ = "Integer32"
_HmUserGroupSecurityAction_Object = MibScalar
hmUserGroupSecurityAction = _HmUserGroupSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 5),
    _HmUserGroupSecurityAction_Type()
)
hmUserGroupSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmUserGroupSecurityAction.setStatus("mandatory")


class _HmUserGroupPortSecurityMode_Type(Integer32):
    """Custom type hmUserGroupPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macAddressBased", 1),
          ("ipAddressBased", 2))
    )


_HmUserGroupPortSecurityMode_Type.__name__ = "Integer32"
_HmUserGroupPortSecurityMode_Object = MibScalar
hmUserGroupPortSecurityMode = _HmUserGroupPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 8),
    _HmUserGroupPortSecurityMode_Type()
)
hmUserGroupPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmUserGroupPortSecurityMode.setStatus("mandatory")
_HmPortSecExtendedGroup_ObjectIdentity = ObjectIdentity
hmPortSecExtendedGroup = _HmPortSecExtendedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10)
)
_HmPortSecExtendedTable_Object = MibTable
hmPortSecExtendedTable = _HmPortSecExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 1)
)
if mibBuilder.loadTexts:
    hmPortSecExtendedTable.setStatus("mandatory")
_HmPortSecExtendedEntry_Object = MibTableRow
hmPortSecExtendedEntry = _HmPortSecExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 1, 1)
)
hmPortSecExtendedEntry.setIndexNames(
    (0, "ABB-USERGROUP-MIB", "hmPortSecExtSlotID"),
    (0, "ABB-USERGROUP-MIB", "hmPortSecExtPortID"),
)
if mibBuilder.loadTexts:
    hmPortSecExtendedEntry.setStatus("mandatory")


class _HmPortSecExtSlotID_Type(Integer32):
    """Custom type hmPortSecExtSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HmPortSecExtSlotID_Type.__name__ = "Integer32"
_HmPortSecExtSlotID_Object = MibTableColumn
hmPortSecExtSlotID = _HmPortSecExtSlotID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 1, 1, 1),
    _HmPortSecExtSlotID_Type()
)
hmPortSecExtSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecExtSlotID.setStatus("mandatory")


class _HmPortSecExtPortID_Type(Integer32):
    """Custom type hmPortSecExtPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmPortSecExtPortID_Type.__name__ = "Integer32"
_HmPortSecExtPortID_Object = MibTableColumn
hmPortSecExtPortID = _HmPortSecExtPortID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 1, 1, 2),
    _HmPortSecExtPortID_Type()
)
hmPortSecExtPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecExtPortID.setStatus("mandatory")


class _HmPortSecExtAction_Type(Integer32):
    """Custom type hmPortSecExtAction based on Integer32"""
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
          ("trapOnly", 2),
          ("portDisable", 3))
    )


_HmPortSecExtAction_Type.__name__ = "Integer32"
_HmPortSecExtAction_Object = MibTableColumn
hmPortSecExtAction = _HmPortSecExtAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 1, 1, 3),
    _HmPortSecExtAction_Type()
)
hmPortSecExtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecExtAction.setStatus("mandatory")


class _HmPortSecExtPortStatus_Type(Integer32):
    """Custom type hmPortSecExtPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("enabledWithWrongAddr", 3))
    )


_HmPortSecExtPortStatus_Type.__name__ = "Integer32"
_HmPortSecExtPortStatus_Object = MibTableColumn
hmPortSecExtPortStatus = _HmPortSecExtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 1, 1, 4),
    _HmPortSecExtPortStatus_Type()
)
hmPortSecExtPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecExtPortStatus.setStatus("mandatory")
_HmPortSecMultipleAdressesTable_Object = MibTable
hmPortSecMultipleAdressesTable = _HmPortSecMultipleAdressesTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2)
)
if mibBuilder.loadTexts:
    hmPortSecMultipleAdressesTable.setStatus("mandatory")
_HmPortSecMultipleAdressesEntry_Object = MibTableRow
hmPortSecMultipleAdressesEntry = _HmPortSecMultipleAdressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1)
)
hmPortSecMultipleAdressesEntry.setIndexNames(
    (0, "ABB-USERGROUP-MIB", "hmPortSecMASlotID"),
    (0, "ABB-USERGROUP-MIB", "hmPortSecMAPortID"),
    (0, "ABB-USERGROUP-MIB", "hmPortSecMAExtendedIndex"),
)
if mibBuilder.loadTexts:
    hmPortSecMultipleAdressesEntry.setStatus("mandatory")


class _HmPortSecMASlotID_Type(Integer32):
    """Custom type hmPortSecMASlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HmPortSecMASlotID_Type.__name__ = "Integer32"
_HmPortSecMASlotID_Object = MibTableColumn
hmPortSecMASlotID = _HmPortSecMASlotID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1, 1),
    _HmPortSecMASlotID_Type()
)
hmPortSecMASlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecMASlotID.setStatus("mandatory")


class _HmPortSecMAPortID_Type(Integer32):
    """Custom type hmPortSecMAPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmPortSecMAPortID_Type.__name__ = "Integer32"
_HmPortSecMAPortID_Object = MibTableColumn
hmPortSecMAPortID = _HmPortSecMAPortID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1, 2),
    _HmPortSecMAPortID_Type()
)
hmPortSecMAPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecMAPortID.setStatus("mandatory")


class _HmPortSecMAExtendedIndex_Type(Integer32):
    """Custom type hmPortSecMAExtendedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HmPortSecMAExtendedIndex_Type.__name__ = "Integer32"
_HmPortSecMAExtendedIndex_Object = MibTableColumn
hmPortSecMAExtendedIndex = _HmPortSecMAExtendedIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1, 3),
    _HmPortSecMAExtendedIndex_Type()
)
hmPortSecMAExtendedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortSecMAExtendedIndex.setStatus("mandatory")
_HmPortSecMAAllowedUserIDs_Type = MemberID
_HmPortSecMAAllowedUserIDs_Object = MibTableColumn
hmPortSecMAAllowedUserIDs = _HmPortSecMAAllowedUserIDs_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1, 4),
    _HmPortSecMAAllowedUserIDs_Type()
)
hmPortSecMAAllowedUserIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecMAAllowedUserIDs.setStatus("mandatory")
_HmPortSecMAAllowedUserIPIDs_Type = IpAddress
_HmPortSecMAAllowedUserIPIDs_Object = MibTableColumn
hmPortSecMAAllowedUserIPIDs = _HmPortSecMAAllowedUserIPIDs_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1, 5),
    _HmPortSecMAAllowedUserIPIDs_Type()
)
hmPortSecMAAllowedUserIPIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecMAAllowedUserIPIDs.setStatus("mandatory")


class _HmPortSecMAAllowedUserIDMask_Type(Integer32):
    """Custom type hmPortSecMAAllowedUserIDMask based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_HmPortSecMAAllowedUserIDMask_Type.__name__ = "Integer32"
_HmPortSecMAAllowedUserIDMask_Object = MibTableColumn
hmPortSecMAAllowedUserIDMask = _HmPortSecMAAllowedUserIDMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 10, 2, 1, 6),
    _HmPortSecMAAllowedUserIDMask_Type()
)
hmPortSecMAAllowedUserIDMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortSecMAAllowedUserIDMask.setStatus("current")

# Managed Objects groups


# Notification objects

hmNewUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 0, 1)
)
hmNewUserTrap.setObjects(
    ("ABB-USERGROUP-MIB", "hmPortSecConnectedUserID")
)
if mibBuilder.loadTexts:
    hmNewUserTrap.setStatus(
        ""
    )

hmPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 0, 2)
)
hmPortSecurityTrap.setObjects(
      *(("ABB-USERGROUP-MIB", "hmPortSecPermission"),
        ("ABB-USERGROUP-MIB", "hmPortSecAction"),
        ("ABB-USERGROUP-MIB", "hmPortSecConnectedUserID"),
        ("ABB-USERGROUP-MIB", "hmPortSecAllowedUserID"),
        ("ABB-USERGROUP-MIB", "hmPortSecAllowedUserIPID"),
        ("ABB-USERGROUP-MIB", "hmPortSecAllowedGroupIDs"))
)
if mibBuilder.loadTexts:
    hmPortSecurityTrap.setStatus(
        ""
    )

hmPortSecConfigErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 3, 0, 3)
)
hmPortSecConfigErrorTrap.setObjects(
    ("ABB-USERGROUP-MIB", "hmPortSecConnectedUserID")
)
if mibBuilder.loadTexts:
    hmPortSecConfigErrorTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ABB-USERGROUP-MIB",
    **{"MemberID": MemberID,
       "hmUserGroup": hmUserGroup,
       "hmNewUserTrap": hmNewUserTrap,
       "hmPortSecurityTrap": hmPortSecurityTrap,
       "hmPortSecConfigErrorTrap": hmPortSecConfigErrorTrap,
       "hmUserGroupTable": hmUserGroupTable,
       "hmUserGroupEntry": hmUserGroupEntry,
       "hmUserGroupID": hmUserGroupID,
       "hmUserGroupDescription": hmUserGroupDescription,
       "hmUserGroupRestricted": hmUserGroupRestricted,
       "hmUserGroupSecAction": hmUserGroupSecAction,
       "hmUserGroupMemberTable": hmUserGroupMemberTable,
       "hmUserGroupMemberEntry": hmUserGroupMemberEntry,
       "hmUserGroupMemberGroupID": hmUserGroupMemberGroupID,
       "hmUserGroupMemberUserID": hmUserGroupMemberUserID,
       "hmUserTable": hmUserTable,
       "hmUserEntry": hmUserEntry,
       "hmUserID": hmUserID,
       "hmUserRestricted": hmUserRestricted,
       "hmPortSecurityTable": hmPortSecurityTable,
       "hmPortSecurityEntry": hmPortSecurityEntry,
       "hmPortSecSlotID": hmPortSecSlotID,
       "hmPortSecPortID": hmPortSecPortID,
       "hmPortSecPermission": hmPortSecPermission,
       "hmPortSecAllowedUserID": hmPortSecAllowedUserID,
       "hmPortSecAllowedGroupIDs": hmPortSecAllowedGroupIDs,
       "hmPortSecConnectedUserID": hmPortSecConnectedUserID,
       "hmPortSecAction": hmPortSecAction,
       "hmPortSecAutoReconfigure": hmPortSecAutoReconfigure,
       "hmPortSecPortStatus": hmPortSecPortStatus,
       "hmPortSecAllowedUserIPID": hmPortSecAllowedUserIPID,
       "hmUserGroupSecurityAction": hmUserGroupSecurityAction,
       "hmUserGroupPortSecurityMode": hmUserGroupPortSecurityMode,
       "hmPortSecExtendedGroup": hmPortSecExtendedGroup,
       "hmPortSecExtendedTable": hmPortSecExtendedTable,
       "hmPortSecExtendedEntry": hmPortSecExtendedEntry,
       "hmPortSecExtSlotID": hmPortSecExtSlotID,
       "hmPortSecExtPortID": hmPortSecExtPortID,
       "hmPortSecExtAction": hmPortSecExtAction,
       "hmPortSecExtPortStatus": hmPortSecExtPortStatus,
       "hmPortSecMultipleAdressesTable": hmPortSecMultipleAdressesTable,
       "hmPortSecMultipleAdressesEntry": hmPortSecMultipleAdressesEntry,
       "hmPortSecMASlotID": hmPortSecMASlotID,
       "hmPortSecMAPortID": hmPortSecMAPortID,
       "hmPortSecMAExtendedIndex": hmPortSecMAExtendedIndex,
       "hmPortSecMAAllowedUserIDs": hmPortSecMAAllowedUserIDs,
       "hmPortSecMAAllowedUserIPIDs": hmPortSecMAAllowedUserIPIDs,
       "hmPortSecMAAllowedUserIDMask": hmPortSecMAAllowedUserIDMask}
)
