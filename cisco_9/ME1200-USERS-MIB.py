# SNMP MIB module (ME1200-USERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-USERS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

me1200UsersMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58)
)
if mibBuilder.loadTexts:
    me1200UsersMIB.setRevisions(
        ("2014-01-29 00:00",
         "2014-01-22 00:00",
         "2013-12-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200UsersMIBObjects_ObjectIdentity = ObjectIdentity
me1200UsersMIBObjects = _Me1200UsersMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1)
)
_Me1200UsersConfig_ObjectIdentity = ObjectIdentity
me1200UsersConfig = _Me1200UsersConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2)
)
_Me1200UsersConfigTable_Object = MibTable
me1200UsersConfigTable = _Me1200UsersConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200UsersConfigTable.setStatus("current")
_Me1200UsersConfigEntry_Object = MibTableRow
me1200UsersConfigEntry = _Me1200UsersConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1, 1)
)
me1200UsersConfigEntry.setIndexNames(
    (0, "ME1200-USERS-MIB", "me1200UsersConfigUsername"),
)
if mibBuilder.loadTexts:
    me1200UsersConfigEntry.setStatus("current")


class _Me1200UsersConfigUsername_Type(ME1200DisplayString):
    """Custom type me1200UsersConfigUsername based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200UsersConfigUsername_Type.__name__ = "ME1200DisplayString"
_Me1200UsersConfigUsername_Object = MibTableColumn
me1200UsersConfigUsername = _Me1200UsersConfigUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1, 1, 1),
    _Me1200UsersConfigUsername_Type()
)
me1200UsersConfigUsername.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200UsersConfigUsername.setStatus("current")
_Me1200UsersConfigPrivilege_Type = Unsigned32
_Me1200UsersConfigPrivilege_Object = MibTableColumn
me1200UsersConfigPrivilege = _Me1200UsersConfigPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1, 1, 2),
    _Me1200UsersConfigPrivilege_Type()
)
me1200UsersConfigPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigPrivilege.setStatus("current")
_Me1200UsersConfigEncrypted_Type = TruthValue
_Me1200UsersConfigEncrypted_Object = MibTableColumn
me1200UsersConfigEncrypted = _Me1200UsersConfigEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1, 1, 3),
    _Me1200UsersConfigEncrypted_Type()
)
me1200UsersConfigEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigEncrypted.setStatus("current")


class _Me1200UsersConfigPassword_Type(ME1200DisplayString):
    """Custom type me1200UsersConfigPassword based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_Me1200UsersConfigPassword_Type.__name__ = "ME1200DisplayString"
_Me1200UsersConfigPassword_Object = MibTableColumn
me1200UsersConfigPassword = _Me1200UsersConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1, 1, 4),
    _Me1200UsersConfigPassword_Type()
)
me1200UsersConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigPassword.setStatus("current")
_Me1200UsersConfigAction_Type = ME1200RowEditorState
_Me1200UsersConfigAction_Object = MibTableColumn
me1200UsersConfigAction = _Me1200UsersConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 1, 1, 100),
    _Me1200UsersConfigAction_Type()
)
me1200UsersConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigAction.setStatus("current")
_Me1200UsersConfigTableRowEditor_ObjectIdentity = ObjectIdentity
me1200UsersConfigTableRowEditor = _Me1200UsersConfigTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 2)
)


class _Me1200UsersConfigTableRowEditorUsername_Type(ME1200DisplayString):
    """Custom type me1200UsersConfigTableRowEditorUsername based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200UsersConfigTableRowEditorUsername_Type.__name__ = "ME1200DisplayString"
_Me1200UsersConfigTableRowEditorUsername_Object = MibScalar
me1200UsersConfigTableRowEditorUsername = _Me1200UsersConfigTableRowEditorUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 2, 1),
    _Me1200UsersConfigTableRowEditorUsername_Type()
)
me1200UsersConfigTableRowEditorUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigTableRowEditorUsername.setStatus("current")
_Me1200UsersConfigTableRowEditorPrivilege_Type = Unsigned32
_Me1200UsersConfigTableRowEditorPrivilege_Object = MibScalar
me1200UsersConfigTableRowEditorPrivilege = _Me1200UsersConfigTableRowEditorPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 2, 2),
    _Me1200UsersConfigTableRowEditorPrivilege_Type()
)
me1200UsersConfigTableRowEditorPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigTableRowEditorPrivilege.setStatus("current")
_Me1200UsersConfigTableRowEditorEncrypted_Type = TruthValue
_Me1200UsersConfigTableRowEditorEncrypted_Object = MibScalar
me1200UsersConfigTableRowEditorEncrypted = _Me1200UsersConfigTableRowEditorEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 2, 3),
    _Me1200UsersConfigTableRowEditorEncrypted_Type()
)
me1200UsersConfigTableRowEditorEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigTableRowEditorEncrypted.setStatus("current")


class _Me1200UsersConfigTableRowEditorPassword_Type(ME1200DisplayString):
    """Custom type me1200UsersConfigTableRowEditorPassword based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_Me1200UsersConfigTableRowEditorPassword_Type.__name__ = "ME1200DisplayString"
_Me1200UsersConfigTableRowEditorPassword_Object = MibScalar
me1200UsersConfigTableRowEditorPassword = _Me1200UsersConfigTableRowEditorPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 2, 4),
    _Me1200UsersConfigTableRowEditorPassword_Type()
)
me1200UsersConfigTableRowEditorPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigTableRowEditorPassword.setStatus("current")
_Me1200UsersConfigTableRowEditorAction_Type = ME1200RowEditorState
_Me1200UsersConfigTableRowEditorAction_Object = MibScalar
me1200UsersConfigTableRowEditorAction = _Me1200UsersConfigTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 1, 2, 2, 100),
    _Me1200UsersConfigTableRowEditorAction_Type()
)
me1200UsersConfigTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UsersConfigTableRowEditorAction.setStatus("current")
_Me1200UsersMIBConformance_ObjectIdentity = ObjectIdentity
me1200UsersMIBConformance = _Me1200UsersMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 2)
)
_Me1200UsersMIBCompliances_ObjectIdentity = ObjectIdentity
me1200UsersMIBCompliances = _Me1200UsersMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 2, 1)
)
_Me1200UsersMIBGroups_ObjectIdentity = ObjectIdentity
me1200UsersMIBGroups = _Me1200UsersMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 2, 2)
)

# Managed Objects groups

me1200UsersConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 2, 2, 1)
)
me1200UsersConfigTableInfoGroup.setObjects(
      *(("ME1200-USERS-MIB", "me1200UsersConfigPrivilege"),
        ("ME1200-USERS-MIB", "me1200UsersConfigEncrypted"),
        ("ME1200-USERS-MIB", "me1200UsersConfigPassword"),
        ("ME1200-USERS-MIB", "me1200UsersConfigAction"))
)
if mibBuilder.loadTexts:
    me1200UsersConfigTableInfoGroup.setStatus("current")

me1200UsersConfigTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 2, 2, 2)
)
me1200UsersConfigTableRowEditorInfoGroup.setObjects(
      *(("ME1200-USERS-MIB", "me1200UsersConfigTableRowEditorUsername"),
        ("ME1200-USERS-MIB", "me1200UsersConfigTableRowEditorPrivilege"),
        ("ME1200-USERS-MIB", "me1200UsersConfigTableRowEditorEncrypted"),
        ("ME1200-USERS-MIB", "me1200UsersConfigTableRowEditorPassword"),
        ("ME1200-USERS-MIB", "me1200UsersConfigTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200UsersConfigTableRowEditorInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200UsersMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 58, 2, 1, 1)
)
me1200UsersMIBCompliance.setObjects(
      *(("ME1200-USERS-MIB", "me1200UsersConfigTableInfoGroup"),
        ("ME1200-USERS-MIB", "me1200UsersConfigTableRowEditorInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200UsersMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-USERS-MIB",
    **{"me1200UsersMIB": me1200UsersMIB,
       "me1200UsersMIBObjects": me1200UsersMIBObjects,
       "me1200UsersConfig": me1200UsersConfig,
       "me1200UsersConfigTable": me1200UsersConfigTable,
       "me1200UsersConfigEntry": me1200UsersConfigEntry,
       "me1200UsersConfigUsername": me1200UsersConfigUsername,
       "me1200UsersConfigPrivilege": me1200UsersConfigPrivilege,
       "me1200UsersConfigEncrypted": me1200UsersConfigEncrypted,
       "me1200UsersConfigPassword": me1200UsersConfigPassword,
       "me1200UsersConfigAction": me1200UsersConfigAction,
       "me1200UsersConfigTableRowEditor": me1200UsersConfigTableRowEditor,
       "me1200UsersConfigTableRowEditorUsername": me1200UsersConfigTableRowEditorUsername,
       "me1200UsersConfigTableRowEditorPrivilege": me1200UsersConfigTableRowEditorPrivilege,
       "me1200UsersConfigTableRowEditorEncrypted": me1200UsersConfigTableRowEditorEncrypted,
       "me1200UsersConfigTableRowEditorPassword": me1200UsersConfigTableRowEditorPassword,
       "me1200UsersConfigTableRowEditorAction": me1200UsersConfigTableRowEditorAction,
       "me1200UsersMIBConformance": me1200UsersMIBConformance,
       "me1200UsersMIBCompliances": me1200UsersMIBCompliances,
       "me1200UsersMIBCompliance": me1200UsersMIBCompliance,
       "me1200UsersMIBGroups": me1200UsersMIBGroups,
       "me1200UsersConfigTableInfoGroup": me1200UsersConfigTableInfoGroup,
       "me1200UsersConfigTableRowEditorInfoGroup": me1200UsersConfigTableRowEditorInfoGroup}
)
