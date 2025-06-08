# SNMP MIB module (ME1200-PRIVILEGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-PRIVILEGE-MIB.mib
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

(ME1200DisplayString,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

me1200PrivilegeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59)
)
if mibBuilder.loadTexts:
    me1200PrivilegeMib.setRevisions(
        ("2014-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200PrivilegeMibObjects_ObjectIdentity = ObjectIdentity
me1200PrivilegeMibObjects = _Me1200PrivilegeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1)
)
_Me1200PrivilegeConfig_ObjectIdentity = ObjectIdentity
me1200PrivilegeConfig = _Me1200PrivilegeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2)
)
_Me1200PrivilegeConfigWebTable_Object = MibTable
me1200PrivilegeConfigWebTable = _Me1200PrivilegeConfigWebTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebTable.setStatus("current")
_Me1200PrivilegeConfigWebEntry_Object = MibTableRow
me1200PrivilegeConfigWebEntry = _Me1200PrivilegeConfigWebEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1)
)
me1200PrivilegeConfigWebEntry.setIndexNames(
    (0, "ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebModuleName"),
)
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebEntry.setStatus("current")


class _Me1200PrivilegeConfigWebModuleName_Type(ME1200DisplayString):
    """Custom type me1200PrivilegeConfigWebModuleName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200PrivilegeConfigWebModuleName_Type.__name__ = "ME1200DisplayString"
_Me1200PrivilegeConfigWebModuleName_Object = MibTableColumn
me1200PrivilegeConfigWebModuleName = _Me1200PrivilegeConfigWebModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 1),
    _Me1200PrivilegeConfigWebModuleName_Type()
)
me1200PrivilegeConfigWebModuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebModuleName.setStatus("current")
_Me1200PrivilegeConfigWebConfigRoPriv_Type = Unsigned32
_Me1200PrivilegeConfigWebConfigRoPriv_Object = MibTableColumn
me1200PrivilegeConfigWebConfigRoPriv = _Me1200PrivilegeConfigWebConfigRoPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 2),
    _Me1200PrivilegeConfigWebConfigRoPriv_Type()
)
me1200PrivilegeConfigWebConfigRoPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebConfigRoPriv.setStatus("current")
_Me1200PrivilegeConfigWebConfigRwPriv_Type = Unsigned32
_Me1200PrivilegeConfigWebConfigRwPriv_Object = MibTableColumn
me1200PrivilegeConfigWebConfigRwPriv = _Me1200PrivilegeConfigWebConfigRwPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 3),
    _Me1200PrivilegeConfigWebConfigRwPriv_Type()
)
me1200PrivilegeConfigWebConfigRwPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebConfigRwPriv.setStatus("current")
_Me1200PrivilegeConfigWebStatusRoPriv_Type = Unsigned32
_Me1200PrivilegeConfigWebStatusRoPriv_Object = MibTableColumn
me1200PrivilegeConfigWebStatusRoPriv = _Me1200PrivilegeConfigWebStatusRoPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 4),
    _Me1200PrivilegeConfigWebStatusRoPriv_Type()
)
me1200PrivilegeConfigWebStatusRoPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebStatusRoPriv.setStatus("current")
_Me1200PrivilegeConfigWebStatusRwPriv_Type = Unsigned32
_Me1200PrivilegeConfigWebStatusRwPriv_Object = MibTableColumn
me1200PrivilegeConfigWebStatusRwPriv = _Me1200PrivilegeConfigWebStatusRwPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 5),
    _Me1200PrivilegeConfigWebStatusRwPriv_Type()
)
me1200PrivilegeConfigWebStatusRwPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebStatusRwPriv.setStatus("current")
_Me1200PrivilegeMibConformance_ObjectIdentity = ObjectIdentity
me1200PrivilegeMibConformance = _Me1200PrivilegeMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2)
)
_Me1200PrivilegeMibCompliances_ObjectIdentity = ObjectIdentity
me1200PrivilegeMibCompliances = _Me1200PrivilegeMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 1)
)
_Me1200PrivilegeMibGroups_ObjectIdentity = ObjectIdentity
me1200PrivilegeMibGroups = _Me1200PrivilegeMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 2)
)

# Managed Objects groups

me1200PrivilegeConfigWebInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 2, 1)
)
me1200PrivilegeConfigWebInfoGroup.setObjects(
      *(("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebConfigRoPriv"),
        ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebConfigRwPriv"),
        ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebStatusRoPriv"),
        ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebStatusRwPriv"))
)
if mibBuilder.loadTexts:
    me1200PrivilegeConfigWebInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200PrivilegeMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 1, 1)
)
me1200PrivilegeMibCompliance.setObjects(
    ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebInfoGroup")
)
if mibBuilder.loadTexts:
    me1200PrivilegeMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-PRIVILEGE-MIB",
    **{"me1200PrivilegeMib": me1200PrivilegeMib,
       "me1200PrivilegeMibObjects": me1200PrivilegeMibObjects,
       "me1200PrivilegeConfig": me1200PrivilegeConfig,
       "me1200PrivilegeConfigWebTable": me1200PrivilegeConfigWebTable,
       "me1200PrivilegeConfigWebEntry": me1200PrivilegeConfigWebEntry,
       "me1200PrivilegeConfigWebModuleName": me1200PrivilegeConfigWebModuleName,
       "me1200PrivilegeConfigWebConfigRoPriv": me1200PrivilegeConfigWebConfigRoPriv,
       "me1200PrivilegeConfigWebConfigRwPriv": me1200PrivilegeConfigWebConfigRwPriv,
       "me1200PrivilegeConfigWebStatusRoPriv": me1200PrivilegeConfigWebStatusRoPriv,
       "me1200PrivilegeConfigWebStatusRwPriv": me1200PrivilegeConfigWebStatusRwPriv,
       "me1200PrivilegeMibConformance": me1200PrivilegeMibConformance,
       "me1200PrivilegeMibCompliances": me1200PrivilegeMibCompliances,
       "me1200PrivilegeMibCompliance": me1200PrivilegeMibCompliance,
       "me1200PrivilegeMibGroups": me1200PrivilegeMibGroups,
       "me1200PrivilegeConfigWebInfoGroup": me1200PrivilegeConfigWebInfoGroup}
)
