# SNMP MIB module (CIE1000-USERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-USERS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

cie1000UsersMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58)
)
if mibBuilder.loadTexts:
    cie1000UsersMib.setRevisions(
        ("2016-01-19 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000UsersMibObjects_ObjectIdentity = ObjectIdentity
cie1000UsersMibObjects = _Cie1000UsersMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1)
)
_Cie1000UsersConfig_ObjectIdentity = ObjectIdentity
cie1000UsersConfig = _Cie1000UsersConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2)
)
_Cie1000UsersConfigTable_Object = MibTable
cie1000UsersConfigTable = _Cie1000UsersConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cie1000UsersConfigTable.setStatus("current")
_Cie1000UsersConfigEntry_Object = MibTableRow
cie1000UsersConfigEntry = _Cie1000UsersConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1, 1)
)
cie1000UsersConfigEntry.setIndexNames(
    (0, "CIE1000-USERS-MIB", "cie1000UsersConfigUsername"),
)
if mibBuilder.loadTexts:
    cie1000UsersConfigEntry.setStatus("current")


class _Cie1000UsersConfigUsername_Type(CIE1000DisplayString):
    """Custom type cie1000UsersConfigUsername based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000UsersConfigUsername_Type.__name__ = "CIE1000DisplayString"
_Cie1000UsersConfigUsername_Object = MibTableColumn
cie1000UsersConfigUsername = _Cie1000UsersConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1, 1, 1),
    _Cie1000UsersConfigUsername_Type()
)
cie1000UsersConfigUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000UsersConfigUsername.setStatus("current")
_Cie1000UsersConfigPrivilege_Type = Unsigned32
_Cie1000UsersConfigPrivilege_Object = MibTableColumn
cie1000UsersConfigPrivilege = _Cie1000UsersConfigPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1, 1, 2),
    _Cie1000UsersConfigPrivilege_Type()
)
cie1000UsersConfigPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigPrivilege.setStatus("current")
_Cie1000UsersConfigEncrypted_Type = TruthValue
_Cie1000UsersConfigEncrypted_Object = MibTableColumn
cie1000UsersConfigEncrypted = _Cie1000UsersConfigEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1, 1, 3),
    _Cie1000UsersConfigEncrypted_Type()
)
cie1000UsersConfigEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigEncrypted.setStatus("current")


class _Cie1000UsersConfigPassword_Type(CIE1000DisplayString):
    """Custom type cie1000UsersConfigPassword based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Cie1000UsersConfigPassword_Type.__name__ = "CIE1000DisplayString"
_Cie1000UsersConfigPassword_Object = MibTableColumn
cie1000UsersConfigPassword = _Cie1000UsersConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1, 1, 4),
    _Cie1000UsersConfigPassword_Type()
)
cie1000UsersConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigPassword.setStatus("current")
_Cie1000UsersConfigAction_Type = CIE1000RowEditorState
_Cie1000UsersConfigAction_Object = MibTableColumn
cie1000UsersConfigAction = _Cie1000UsersConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 1, 1, 100),
    _Cie1000UsersConfigAction_Type()
)
cie1000UsersConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigAction.setStatus("current")
_Cie1000UsersConfigTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000UsersConfigTableRowEditor = _Cie1000UsersConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 2)
)


class _Cie1000UsersConfigTableRowEditorUsername_Type(CIE1000DisplayString):
    """Custom type cie1000UsersConfigTableRowEditorUsername based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000UsersConfigTableRowEditorUsername_Type.__name__ = "CIE1000DisplayString"
_Cie1000UsersConfigTableRowEditorUsername_Object = MibScalar
cie1000UsersConfigTableRowEditorUsername = _Cie1000UsersConfigTableRowEditorUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 2, 1),
    _Cie1000UsersConfigTableRowEditorUsername_Type()
)
cie1000UsersConfigTableRowEditorUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigTableRowEditorUsername.setStatus("current")
_Cie1000UsersConfigTableRowEditorPrivilege_Type = Unsigned32
_Cie1000UsersConfigTableRowEditorPrivilege_Object = MibScalar
cie1000UsersConfigTableRowEditorPrivilege = _Cie1000UsersConfigTableRowEditorPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 2, 2),
    _Cie1000UsersConfigTableRowEditorPrivilege_Type()
)
cie1000UsersConfigTableRowEditorPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigTableRowEditorPrivilege.setStatus("current")
_Cie1000UsersConfigTableRowEditorEncrypted_Type = TruthValue
_Cie1000UsersConfigTableRowEditorEncrypted_Object = MibScalar
cie1000UsersConfigTableRowEditorEncrypted = _Cie1000UsersConfigTableRowEditorEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 2, 3),
    _Cie1000UsersConfigTableRowEditorEncrypted_Type()
)
cie1000UsersConfigTableRowEditorEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigTableRowEditorEncrypted.setStatus("current")


class _Cie1000UsersConfigTableRowEditorPassword_Type(CIE1000DisplayString):
    """Custom type cie1000UsersConfigTableRowEditorPassword based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Cie1000UsersConfigTableRowEditorPassword_Type.__name__ = "CIE1000DisplayString"
_Cie1000UsersConfigTableRowEditorPassword_Object = MibScalar
cie1000UsersConfigTableRowEditorPassword = _Cie1000UsersConfigTableRowEditorPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 2, 4),
    _Cie1000UsersConfigTableRowEditorPassword_Type()
)
cie1000UsersConfigTableRowEditorPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigTableRowEditorPassword.setStatus("current")
_Cie1000UsersConfigTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000UsersConfigTableRowEditorAction_Object = MibScalar
cie1000UsersConfigTableRowEditorAction = _Cie1000UsersConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 1, 2, 2, 100),
    _Cie1000UsersConfigTableRowEditorAction_Type()
)
cie1000UsersConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000UsersConfigTableRowEditorAction.setStatus("current")
_Cie1000UsersMibConformance_ObjectIdentity = ObjectIdentity
cie1000UsersMibConformance = _Cie1000UsersMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 2)
)
_Cie1000UsersMibCompliances_ObjectIdentity = ObjectIdentity
cie1000UsersMibCompliances = _Cie1000UsersMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 2, 1)
)
_Cie1000UsersMibGroups_ObjectIdentity = ObjectIdentity
cie1000UsersMibGroups = _Cie1000UsersMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 2, 2)
)

# Managed Objects groups

cie1000UsersConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 2, 2, 1)
)
cie1000UsersConfigTableInfoGroup.setObjects(
      *(("CIE1000-USERS-MIB", "cie1000UsersConfigUsername"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigPrivilege"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigEncrypted"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigPassword"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigAction"))
)
if mibBuilder.loadTexts:
    cie1000UsersConfigTableInfoGroup.setStatus("current")

cie1000UsersConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 2, 2, 2)
)
cie1000UsersConfigTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-USERS-MIB", "cie1000UsersConfigTableRowEditorUsername"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigTableRowEditorPrivilege"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigTableRowEditorEncrypted"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigTableRowEditorPassword"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000UsersConfigTableRowEditorInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000UsersMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 58, 2, 1, 1)
)
cie1000UsersMibCompliance.setObjects(
      *(("CIE1000-USERS-MIB", "cie1000UsersConfigTableInfoGroup"),
        ("CIE1000-USERS-MIB", "cie1000UsersConfigTableRowEditorInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000UsersMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-USERS-MIB",
    **{"cie1000UsersMib": cie1000UsersMib,
       "cie1000UsersMibObjects": cie1000UsersMibObjects,
       "cie1000UsersConfig": cie1000UsersConfig,
       "cie1000UsersConfigTable": cie1000UsersConfigTable,
       "cie1000UsersConfigEntry": cie1000UsersConfigEntry,
       "cie1000UsersConfigUsername": cie1000UsersConfigUsername,
       "cie1000UsersConfigPrivilege": cie1000UsersConfigPrivilege,
       "cie1000UsersConfigEncrypted": cie1000UsersConfigEncrypted,
       "cie1000UsersConfigPassword": cie1000UsersConfigPassword,
       "cie1000UsersConfigAction": cie1000UsersConfigAction,
       "cie1000UsersConfigTableRowEditor": cie1000UsersConfigTableRowEditor,
       "cie1000UsersConfigTableRowEditorUsername": cie1000UsersConfigTableRowEditorUsername,
       "cie1000UsersConfigTableRowEditorPrivilege": cie1000UsersConfigTableRowEditorPrivilege,
       "cie1000UsersConfigTableRowEditorEncrypted": cie1000UsersConfigTableRowEditorEncrypted,
       "cie1000UsersConfigTableRowEditorPassword": cie1000UsersConfigTableRowEditorPassword,
       "cie1000UsersConfigTableRowEditorAction": cie1000UsersConfigTableRowEditorAction,
       "cie1000UsersMibConformance": cie1000UsersMibConformance,
       "cie1000UsersMibCompliances": cie1000UsersMibCompliances,
       "cie1000UsersMibCompliance": cie1000UsersMibCompliance,
       "cie1000UsersMibGroups": cie1000UsersMibGroups,
       "cie1000UsersConfigTableInfoGroup": cie1000UsersConfigTableInfoGroup,
       "cie1000UsersConfigTableRowEditorInfoGroup": cie1000UsersConfigTableRowEditorInfoGroup}
)
