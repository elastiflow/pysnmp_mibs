# SNMP MIB module (USERGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/schneider_3833/USERGROUP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:06:19 2025
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

(everything,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "everything")

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

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Groupeschneider_ObjectIdentity = ObjectIdentity
groupeschneider = _Groupeschneider_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833)
)
_TransparentFactoryEthernet_ObjectIdentity = ObjectIdentity
transparentFactoryEthernet = _TransparentFactoryEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1)
)
_SaConfiguration_ObjectIdentity = ObjectIdentity
saConfiguration = _SaConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14)
)
_SaUserGroup_ObjectIdentity = ObjectIdentity
saUserGroup = _SaUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3)
)
_SaPortSecurityTable_Object = MibTable
saPortSecurityTable = _SaPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4)
)
if mibBuilder.loadTexts:
    saPortSecurityTable.setStatus("mandatory")
_SaPortSecurityEntry_Object = MibTableRow
saPortSecurityEntry = _SaPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1)
)
saPortSecurityEntry.setIndexNames(
    (0, "USERGROUP-MIB", "saPortSecSlotID"),
    (0, "USERGROUP-MIB", "saPortSecPortID"),
)
if mibBuilder.loadTexts:
    saPortSecurityEntry.setStatus("mandatory")


class _SaPortSecSlotID_Type(Integer32):
    """Custom type saPortSecSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SaPortSecSlotID_Type.__name__ = "Integer32"
_SaPortSecSlotID_Object = MibTableColumn
saPortSecSlotID = _SaPortSecSlotID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 1),
    _SaPortSecSlotID_Type()
)
saPortSecSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPortSecSlotID.setStatus("mandatory")


class _SaPortSecPortID_Type(Integer32):
    """Custom type saPortSecPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SaPortSecPortID_Type.__name__ = "Integer32"
_SaPortSecPortID_Object = MibTableColumn
saPortSecPortID = _SaPortSecPortID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 2),
    _SaPortSecPortID_Type()
)
saPortSecPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPortSecPortID.setStatus("mandatory")


class _SaPortSecPermission_Type(Integer32):
    """Custom type saPortSecPermission based on Integer32"""
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


_SaPortSecPermission_Type.__name__ = "Integer32"
_SaPortSecPermission_Object = MibTableColumn
saPortSecPermission = _SaPortSecPermission_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 3),
    _SaPortSecPermission_Type()
)
saPortSecPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPortSecPermission.setStatus("mandatory")


class _SaPortSecAllowedUserID_Type(DisplayString):
    """Custom type saPortSecAllowedUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_SaPortSecAllowedUserID_Type.__name__ = "DisplayString"
_SaPortSecAllowedUserID_Object = MibTableColumn
saPortSecAllowedUserID = _SaPortSecAllowedUserID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 4),
    _SaPortSecAllowedUserID_Type()
)
saPortSecAllowedUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPortSecAllowedUserID.setStatus("mandatory")


class _SaPortSecAllowedGroupIDs_Type(OctetString):
    """Custom type saPortSecAllowedGroupIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_SaPortSecAllowedGroupIDs_Type.__name__ = "OctetString"
_SaPortSecAllowedGroupIDs_Object = MibTableColumn
saPortSecAllowedGroupIDs = _SaPortSecAllowedGroupIDs_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 5),
    _SaPortSecAllowedGroupIDs_Type()
)
saPortSecAllowedGroupIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPortSecAllowedGroupIDs.setStatus("mandatory")
_SaPortSecConnectedUserID_Type = MemberID
_SaPortSecConnectedUserID_Object = MibTableColumn
saPortSecConnectedUserID = _SaPortSecConnectedUserID_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 6),
    _SaPortSecConnectedUserID_Type()
)
saPortSecConnectedUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPortSecConnectedUserID.setStatus("mandatory")


class _SaPortSecAction_Type(Integer32):
    """Custom type saPortSecAction based on Integer32"""
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


_SaPortSecAction_Type.__name__ = "Integer32"
_SaPortSecAction_Object = MibTableColumn
saPortSecAction = _SaPortSecAction_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 7),
    _SaPortSecAction_Type()
)
saPortSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPortSecAction.setStatus("mandatory")


class _SaPortSecAutoReconfigure_Type(Integer32):
    """Custom type saPortSecAutoReconfigure based on Integer32"""
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


_SaPortSecAutoReconfigure_Type.__name__ = "Integer32"
_SaPortSecAutoReconfigure_Object = MibTableColumn
saPortSecAutoReconfigure = _SaPortSecAutoReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 4, 1, 8),
    _SaPortSecAutoReconfigure_Type()
)
saPortSecAutoReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPortSecAutoReconfigure.setStatus("mandatory")

# Managed Objects groups


# Notification objects

saPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3833, 1, 1, 14, 3, 0, 2)
)
saPortSecurityTrap.setObjects(
      *(("USERGROUP-MIB", "saPortSecPermission"),
        ("USERGROUP-MIB", "saPortSecAllowedUserID"),
        ("USERGROUP-MIB", "saPortSecAllowedGroupIDs"),
        ("USERGROUP-MIB", "saPortSecConnectedUserID"),
        ("USERGROUP-MIB", "saPortSecAction"))
)
if mibBuilder.loadTexts:
    saPortSecurityTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "USERGROUP-MIB",
    **{"MemberID": MemberID,
       "private": private,
       "enterprises": enterprises,
       "groupeschneider": groupeschneider,
       "transparentFactoryEthernet": transparentFactoryEthernet,
       "switch": switch,
       "saConfiguration": saConfiguration,
       "saUserGroup": saUserGroup,
       "saPortSecurityTrap": saPortSecurityTrap,
       "saPortSecurityTable": saPortSecurityTable,
       "saPortSecurityEntry": saPortSecurityEntry,
       "saPortSecSlotID": saPortSecSlotID,
       "saPortSecPortID": saPortSecPortID,
       "saPortSecPermission": saPortSecPermission,
       "saPortSecAllowedUserID": saPortSecAllowedUserID,
       "saPortSecAllowedGroupIDs": saPortSecAllowedGroupIDs,
       "saPortSecConnectedUserID": saPortSecConnectedUserID,
       "saPortSecAction": saPortSecAction,
       "saPortSecAutoReconfigure": saPortSecAutoReconfigure}
)
