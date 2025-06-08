# SNMP MIB module (RUIJIE-PFXV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PFXV6-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijiePFXv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134)
)
if mibBuilder.loadTexts:
    ruijiePFXv6MIB.setRevisions(
        ("2015-01-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiePFXv6MIBObjects_ObjectIdentity = ObjectIdentity
ruijiePFXv6MIBObjects = _RuijiePFXv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1)
)
_RuijiePFXv6Table_Object = MibTable
ruijiePFXv6Table = _RuijiePFXv6Table_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiePFXv6Table.setStatus("current")
_RuijiePFXv6Entry_Object = MibTableRow
ruijiePFXv6Entry = _RuijiePFXv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1)
)
ruijiePFXv6Entry.setIndexNames(
    (0, "RUIJIE-PFXV6-MIB", "ruijiePFXv6Name"),
)
if mibBuilder.loadTexts:
    ruijiePFXv6Entry.setStatus("current")


class _RuijiePFXv6Name_Type(DisplayString):
    """Custom type ruijiePFXv6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijiePFXv6Name_Type.__name__ = "DisplayString"
_RuijiePFXv6Name_Object = MibTableColumn
ruijiePFXv6Name = _RuijiePFXv6Name_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1, 1),
    _RuijiePFXv6Name_Type()
)
ruijiePFXv6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6Name.setStatus("current")
_RuijiePFXv6Total_Type = Integer32
_RuijiePFXv6Total_Object = MibTableColumn
ruijiePFXv6Total = _RuijiePFXv6Total_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1, 2),
    _RuijiePFXv6Total_Type()
)
ruijiePFXv6Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6Total.setStatus("current")
_RuijiePFXv6Rejects_Type = Integer32
_RuijiePFXv6Rejects_Object = MibTableColumn
ruijiePFXv6Rejects = _RuijiePFXv6Rejects_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1, 3),
    _RuijiePFXv6Rejects_Type()
)
ruijiePFXv6Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6Rejects.setStatus("current")
_RuijiePFXv6Accepts_Type = Integer32
_RuijiePFXv6Accepts_Object = MibTableColumn
ruijiePFXv6Accepts = _RuijiePFXv6Accepts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1, 4),
    _RuijiePFXv6Accepts_Type()
)
ruijiePFXv6Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6Accepts.setStatus("current")
_RuijiePFXv6Frees_Type = Integer32
_RuijiePFXv6Frees_Object = MibTableColumn
ruijiePFXv6Frees = _RuijiePFXv6Frees_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1, 5),
    _RuijiePFXv6Frees_Type()
)
ruijiePFXv6Frees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6Frees.setStatus("current")


class _RuijiePFXv6Userate_Type(Integer32):
    """Custom type ruijiePFXv6Userate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijiePFXv6Userate_Type.__name__ = "Integer32"
_RuijiePFXv6Userate_Object = MibTableColumn
ruijiePFXv6Userate = _RuijiePFXv6Userate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 1, 1, 6),
    _RuijiePFXv6Userate_Type()
)
ruijiePFXv6Userate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6Userate.setStatus("current")
_RuijiePFXv6IfTable_Object = MibTable
ruijiePFXv6IfTable = _RuijiePFXv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2)
)
if mibBuilder.loadTexts:
    ruijiePFXv6IfTable.setStatus("current")
_RuijiePFXv6IfEntry_Object = MibTableRow
ruijiePFXv6IfEntry = _RuijiePFXv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1)
)
ruijiePFXv6IfEntry.setIndexNames(
    (0, "RUIJIE-PFXV6-MIB", "ruijiePFXv6IfIfIndex"),
)
if mibBuilder.loadTexts:
    ruijiePFXv6IfEntry.setStatus("current")
_RuijiePFXv6IfIfIndex_Type = IfIndex
_RuijiePFXv6IfIfIndex_Object = MibTableColumn
ruijiePFXv6IfIfIndex = _RuijiePFXv6IfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 1),
    _RuijiePFXv6IfIfIndex_Type()
)
ruijiePFXv6IfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfIfIndex.setStatus("current")


class _RuijiePFXv6IfName_Type(DisplayString):
    """Custom type ruijiePFXv6IfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijiePFXv6IfName_Type.__name__ = "DisplayString"
_RuijiePFXv6IfName_Object = MibTableColumn
ruijiePFXv6IfName = _RuijiePFXv6IfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 2),
    _RuijiePFXv6IfName_Type()
)
ruijiePFXv6IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfName.setStatus("current")
_RuijiePFXv6IfTotal_Type = Integer32
_RuijiePFXv6IfTotal_Object = MibTableColumn
ruijiePFXv6IfTotal = _RuijiePFXv6IfTotal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 3),
    _RuijiePFXv6IfTotal_Type()
)
ruijiePFXv6IfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfTotal.setStatus("current")
_RuijiePFXv6IfRejects_Type = Integer32
_RuijiePFXv6IfRejects_Object = MibTableColumn
ruijiePFXv6IfRejects = _RuijiePFXv6IfRejects_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 4),
    _RuijiePFXv6IfRejects_Type()
)
ruijiePFXv6IfRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfRejects.setStatus("current")
_RuijiePFXv6IfAccepts_Type = Integer32
_RuijiePFXv6IfAccepts_Object = MibTableColumn
ruijiePFXv6IfAccepts = _RuijiePFXv6IfAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 5),
    _RuijiePFXv6IfAccepts_Type()
)
ruijiePFXv6IfAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfAccepts.setStatus("current")
_RuijiePFXv6IfFrees_Type = Integer32
_RuijiePFXv6IfFrees_Object = MibTableColumn
ruijiePFXv6IfFrees = _RuijiePFXv6IfFrees_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 6),
    _RuijiePFXv6IfFrees_Type()
)
ruijiePFXv6IfFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfFrees.setStatus("current")


class _RuijiePFXv6IfUserate_Type(Integer32):
    """Custom type ruijiePFXv6IfUserate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijiePFXv6IfUserate_Type.__name__ = "Integer32"
_RuijiePFXv6IfUserate_Object = MibTableColumn
ruijiePFXv6IfUserate = _RuijiePFXv6IfUserate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 2, 1, 7),
    _RuijiePFXv6IfUserate_Type()
)
ruijiePFXv6IfUserate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePFXv6IfUserate.setStatus("current")
_RuijieSlaacRequestNumber_Type = Counter32
_RuijieSlaacRequestNumber_Object = MibScalar
ruijieSlaacRequestNumber = _RuijieSlaacRequestNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 3),
    _RuijieSlaacRequestNumber_Type()
)
ruijieSlaacRequestNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlaacRequestNumber.setStatus("current")
_RuijieSlaacRequestSuccessNumber_Type = Counter32
_RuijieSlaacRequestSuccessNumber_Object = MibScalar
ruijieSlaacRequestSuccessNumber = _RuijieSlaacRequestSuccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 1, 4),
    _RuijieSlaacRequestSuccessNumber_Type()
)
ruijieSlaacRequestSuccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlaacRequestSuccessNumber.setStatus("current")
_RuijiePFXv6MIBConformance_ObjectIdentity = ObjectIdentity
ruijiePFXv6MIBConformance = _RuijiePFXv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 2)
)
_RuijiePFXv6MIBCompliances_ObjectIdentity = ObjectIdentity
ruijiePFXv6MIBCompliances = _RuijiePFXv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 2, 1)
)
_RuijiePFXv6MIBGroups_ObjectIdentity = ObjectIdentity
ruijiePFXv6MIBGroups = _RuijiePFXv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 2, 2)
)

# Managed Objects groups

ruijiePFXv6MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 2, 2, 1)
)
ruijiePFXv6MIBGroup.setObjects(
      *(("RUIJIE-PFXV6-MIB", "ruijiePFXv6Name"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6Total"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6Rejects"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6Accepts"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6Frees"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6Userate"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfIfIndex"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfName"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfTotal"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfRejects"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfAccepts"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfFrees"),
        ("RUIJIE-PFXV6-MIB", "ruijiePFXv6IfUserate"),
        ("RUIJIE-PFXV6-MIB", "ruijieSlaacRequestNumber"),
        ("RUIJIE-PFXV6-MIB", "ruijieSlaacRequestSuccessNumber"))
)
if mibBuilder.loadTexts:
    ruijiePFXv6MIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijiePFXv6MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 134, 2, 1, 1)
)
ruijiePFXv6MIBCompliance.setObjects(
    ("RUIJIE-PFXV6-MIB", "ruijiePFXv6MIBGroup")
)
if mibBuilder.loadTexts:
    ruijiePFXv6MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PFXV6-MIB",
    **{"ruijiePFXv6MIB": ruijiePFXv6MIB,
       "ruijiePFXv6MIBObjects": ruijiePFXv6MIBObjects,
       "ruijiePFXv6Table": ruijiePFXv6Table,
       "ruijiePFXv6Entry": ruijiePFXv6Entry,
       "ruijiePFXv6Name": ruijiePFXv6Name,
       "ruijiePFXv6Total": ruijiePFXv6Total,
       "ruijiePFXv6Rejects": ruijiePFXv6Rejects,
       "ruijiePFXv6Accepts": ruijiePFXv6Accepts,
       "ruijiePFXv6Frees": ruijiePFXv6Frees,
       "ruijiePFXv6Userate": ruijiePFXv6Userate,
       "ruijiePFXv6IfTable": ruijiePFXv6IfTable,
       "ruijiePFXv6IfEntry": ruijiePFXv6IfEntry,
       "ruijiePFXv6IfIfIndex": ruijiePFXv6IfIfIndex,
       "ruijiePFXv6IfName": ruijiePFXv6IfName,
       "ruijiePFXv6IfTotal": ruijiePFXv6IfTotal,
       "ruijiePFXv6IfRejects": ruijiePFXv6IfRejects,
       "ruijiePFXv6IfAccepts": ruijiePFXv6IfAccepts,
       "ruijiePFXv6IfFrees": ruijiePFXv6IfFrees,
       "ruijiePFXv6IfUserate": ruijiePFXv6IfUserate,
       "ruijieSlaacRequestNumber": ruijieSlaacRequestNumber,
       "ruijieSlaacRequestSuccessNumber": ruijieSlaacRequestSuccessNumber,
       "ruijiePFXv6MIBConformance": ruijiePFXv6MIBConformance,
       "ruijiePFXv6MIBCompliances": ruijiePFXv6MIBCompliances,
       "ruijiePFXv6MIBCompliance": ruijiePFXv6MIBCompliance,
       "ruijiePFXv6MIBGroups": ruijiePFXv6MIBGroups,
       "ruijiePFXv6MIBGroup": ruijiePFXv6MIBGroup}
)
