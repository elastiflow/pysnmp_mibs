# SNMP MIB module (RUIJIE-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-LICENSE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57)
)
if mibBuilder.loadTexts:
    ruijieLicenseMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieLicenseMIBObjects_ObjectIdentity = ObjectIdentity
ruijieLicenseMIBObjects = _RuijieLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1)
)
_RuijieShowLicense_Type = Integer32
_RuijieShowLicense_Object = MibScalar
ruijieShowLicense = _RuijieShowLicense_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1, 1),
    _RuijieShowLicense_Type()
)
ruijieShowLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieShowLicense.setStatus("current")
_RuijieLicenseTable_Object = MibTable
ruijieLicenseTable = _RuijieLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieLicenseTable.setStatus("current")
_RuijieLicenseEntry_Object = MibTableRow
ruijieLicenseEntry = _RuijieLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1, 2, 1)
)
ruijieLicenseEntry.setIndexNames(
    (0, "RUIJIE-LICENSE-MIB", "ruijieLicenseIndex"),
)
if mibBuilder.loadTexts:
    ruijieLicenseEntry.setStatus("current")
_RuijieLicenseIndex_Type = Integer32
_RuijieLicenseIndex_Object = MibTableColumn
ruijieLicenseIndex = _RuijieLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1, 2, 1, 1),
    _RuijieLicenseIndex_Type()
)
ruijieLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieLicenseIndex.setStatus("current")
_RuijieLicenseString_Type = DisplayString
_RuijieLicenseString_Object = MibTableColumn
ruijieLicenseString = _RuijieLicenseString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1, 2, 1, 2),
    _RuijieLicenseString_Type()
)
ruijieLicenseString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLicenseString.setStatus("current")
_RuijieLicenseValue_Type = Integer32
_RuijieLicenseValue_Object = MibTableColumn
ruijieLicenseValue = _RuijieLicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 1, 2, 1, 3),
    _RuijieLicenseValue_Type()
)
ruijieLicenseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLicenseValue.setStatus("current")
_RuijieLicenseMIBConformance_ObjectIdentity = ObjectIdentity
ruijieLicenseMIBConformance = _RuijieLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 2)
)
_RuijieLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieLicenseMIBCompliances = _RuijieLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 2, 1)
)
_RuijieLicenseMIBGroups_ObjectIdentity = ObjectIdentity
ruijieLicenseMIBGroups = _RuijieLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 2, 2)
)

# Managed Objects groups

ruijieLicenseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 2, 2, 1)
)
ruijieLicenseMIBGroup.setObjects(
      *(("RUIJIE-LICENSE-MIB", "ruijieShowLicense"),
        ("RUIJIE-LICENSE-MIB", "ruijieLicenseString"),
        ("RUIJIE-LICENSE-MIB", "ruijieLicenseValue"))
)
if mibBuilder.loadTexts:
    ruijieLicenseMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieLicenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 57, 2, 1, 1)
)
ruijieLicenseMIBCompliance.setObjects(
    ("RUIJIE-LICENSE-MIB", "ruijieLicenseMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieLicenseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-LICENSE-MIB",
    **{"ruijieLicenseMIB": ruijieLicenseMIB,
       "ruijieLicenseMIBObjects": ruijieLicenseMIBObjects,
       "ruijieShowLicense": ruijieShowLicense,
       "ruijieLicenseTable": ruijieLicenseTable,
       "ruijieLicenseEntry": ruijieLicenseEntry,
       "ruijieLicenseIndex": ruijieLicenseIndex,
       "ruijieLicenseString": ruijieLicenseString,
       "ruijieLicenseValue": ruijieLicenseValue,
       "ruijieLicenseMIBConformance": ruijieLicenseMIBConformance,
       "ruijieLicenseMIBCompliances": ruijieLicenseMIBCompliances,
       "ruijieLicenseMIBCompliance": ruijieLicenseMIBCompliance,
       "ruijieLicenseMIBGroups": ruijieLicenseMIBGroups,
       "ruijieLicenseMIBGroup": ruijieLicenseMIBGroup}
)
