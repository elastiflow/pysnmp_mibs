# SNMP MIB module (UVF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/univef_48804/UVF-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:50 2025
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

uvfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48804)
)
if mibBuilder.loadTexts:
    uvfMIB.setRevisions(
        ("2016-11-07 12:55",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UvfSlaPlugins_ObjectIdentity = ObjectIdentity
uvfSlaPlugins = _UvfSlaPlugins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48804, 1)
)
_UvfTestPluginRttTable_Object = MibTable
uvfTestPluginRttTable = _UvfTestPluginRttTable_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 4)
)
if mibBuilder.loadTexts:
    uvfTestPluginRttTable.setStatus("current")
_UvfTestPluginRttEntry_Object = MibTableRow
uvfTestPluginRttEntry = _UvfTestPluginRttEntry_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 4, 1)
)
uvfTestPluginRttEntry.setIndexNames(
    (0, "UVF-MIB", "uvfTestPluginRttId"),
)
if mibBuilder.loadTexts:
    uvfTestPluginRttEntry.setStatus("current")


class _UvfTestPluginRttId_Type(OctetString):
    """Custom type uvfTestPluginRttId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65000),
    )


_UvfTestPluginRttId_Type.__name__ = "OctetString"
_UvfTestPluginRttId_Object = MibTableColumn
uvfTestPluginRttId = _UvfTestPluginRttId_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 4, 1, 1),
    _UvfTestPluginRttId_Type()
)
uvfTestPluginRttId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uvfTestPluginRttId.setStatus("current")
_UvfTestPluginRttAddress_Type = OctetString
_UvfTestPluginRttAddress_Object = MibTableColumn
uvfTestPluginRttAddress = _UvfTestPluginRttAddress_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 4, 1, 2),
    _UvfTestPluginRttAddress_Type()
)
uvfTestPluginRttAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uvfTestPluginRttAddress.setStatus("current")
_UvfTestPluginOwampTable_Object = MibTable
uvfTestPluginOwampTable = _UvfTestPluginOwampTable_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 6)
)
if mibBuilder.loadTexts:
    uvfTestPluginOwampTable.setStatus("current")
_UvfTestPluginOwampEntry_Object = MibTableRow
uvfTestPluginOwampEntry = _UvfTestPluginOwampEntry_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 6, 1)
)
uvfTestPluginOwampEntry.setIndexNames(
    (0, "UVF-MIB", "uvfTestPluginOwampId"),
)
if mibBuilder.loadTexts:
    uvfTestPluginOwampEntry.setStatus("current")


class _UvfTestPluginOwampId_Type(OctetString):
    """Custom type uvfTestPluginOwampId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65000),
    )


_UvfTestPluginOwampId_Type.__name__ = "OctetString"
_UvfTestPluginOwampId_Object = MibTableColumn
uvfTestPluginOwampId = _UvfTestPluginOwampId_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 6, 1, 1),
    _UvfTestPluginOwampId_Type()
)
uvfTestPluginOwampId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uvfTestPluginOwampId.setStatus("current")
_UvfTestPluginOwampAddress_Type = OctetString
_UvfTestPluginOwampAddress_Object = MibTableColumn
uvfTestPluginOwampAddress = _UvfTestPluginOwampAddress_Object(
    (1, 3, 6, 1, 4, 1, 48804, 1, 6, 1, 2),
    _UvfTestPluginOwampAddress_Type()
)
uvfTestPluginOwampAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uvfTestPluginOwampAddress.setStatus("current")
_UvfSla_ObjectIdentity = ObjectIdentity
uvfSla = _UvfSla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48804, 3)
)

# Managed Objects groups

uvfChannelObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48804, 3, 2)
)
uvfChannelObjects.setObjects(
      *(("UVF-MIB", "uvfTestPluginRttAddress"),
        ("UVF-MIB", "uvfTestPluginOwampAddress"))
)
if mibBuilder.loadTexts:
    uvfChannelObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UVF-MIB",
    **{"uvfMIB": uvfMIB,
       "uvfSlaPlugins": uvfSlaPlugins,
       "uvfTestPluginRttTable": uvfTestPluginRttTable,
       "uvfTestPluginRttEntry": uvfTestPluginRttEntry,
       "uvfTestPluginRttId": uvfTestPluginRttId,
       "uvfTestPluginRttAddress": uvfTestPluginRttAddress,
       "uvfTestPluginOwampTable": uvfTestPluginOwampTable,
       "uvfTestPluginOwampEntry": uvfTestPluginOwampEntry,
       "uvfTestPluginOwampId": uvfTestPluginOwampId,
       "uvfTestPluginOwampAddress": uvfTestPluginOwampAddress,
       "uvfSla": uvfSla,
       "uvfChannelObjects": uvfChannelObjects}
)
