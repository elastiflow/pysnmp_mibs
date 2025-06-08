# SNMP MIB module (RUIJIE-VPLS-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VPLS-BGP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(ruijievplsConfigIndex,
 ruijievplsPwBindIndex) = mibBuilder.importSymbols(
    "RUIJIE-VPLS-GENERIC-MIB",
    "ruijievplsConfigIndex",
    "ruijievplsPwBindIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ruijievplsBgpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79)
)
if mibBuilder.loadTexts:
    ruijievplsBgpDraft01MIB.setRevisions(
        ("2010-04-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuijieVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class RuijieVplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_RuijievplsBgpObjects_ObjectIdentity = ObjectIdentity
ruijievplsBgpObjects = _RuijievplsBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1)
)
_RuijievplsBgpVETable_Object = MibTable
ruijievplsBgpVETable = _RuijievplsBgpVETable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1)
)
if mibBuilder.loadTexts:
    ruijievplsBgpVETable.setStatus("current")
_RuijievplsBgpVEEntry_Object = MibTableRow
ruijievplsBgpVEEntry = _RuijievplsBgpVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1, 1)
)
ruijievplsBgpVEEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
    (0, "RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpVEindex"),
)
if mibBuilder.loadTexts:
    ruijievplsBgpVEEntry.setStatus("current")


class _RuijievplsBgpVEindex_Type(Unsigned32):
    """Custom type ruijievplsBgpVEindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijievplsBgpVEindex_Type.__name__ = "Unsigned32"
_RuijievplsBgpVEindex_Object = MibTableColumn
ruijievplsBgpVEindex = _RuijievplsBgpVEindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1, 1, 1),
    _RuijievplsBgpVEindex_Type()
)
ruijievplsBgpVEindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijievplsBgpVEindex.setStatus("current")


class _RuijievplsBgpVEId_Type(Unsigned32):
    """Custom type ruijievplsBgpVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RuijievplsBgpVEId_Type.__name__ = "Unsigned32"
_RuijievplsBgpVEId_Object = MibTableColumn
ruijievplsBgpVEId = _RuijievplsBgpVEId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1, 1, 2),
    _RuijievplsBgpVEId_Type()
)
ruijievplsBgpVEId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpVEId.setStatus("current")


class _RuijievplsBgpRangeSize_Type(Unsigned32):
    """Custom type ruijievplsBgpRangeSize based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RuijievplsBgpRangeSize_Type.__name__ = "Unsigned32"
_RuijievplsBgpRangeSize_Object = MibTableColumn
ruijievplsBgpRangeSize = _RuijievplsBgpRangeSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1, 1, 3),
    _RuijievplsBgpRangeSize_Type()
)
ruijievplsBgpRangeSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpRangeSize.setStatus("current")


class _RuijievplsBgpVEPreference_Type(Unsigned32):
    """Custom type ruijievplsBgpVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RuijievplsBgpVEPreference_Type.__name__ = "Unsigned32"
_RuijievplsBgpVEPreference_Object = MibTableColumn
ruijievplsBgpVEPreference = _RuijievplsBgpVEPreference_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1, 1, 4),
    _RuijievplsBgpVEPreference_Type()
)
ruijievplsBgpVEPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsBgpVEPreference.setStatus("current")
_RuijievplsBgpVERowStatus_Type = RowStatus
_RuijievplsBgpVERowStatus_Object = MibTableColumn
ruijievplsBgpVERowStatus = _RuijievplsBgpVERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 1, 1, 5),
    _RuijievplsBgpVERowStatus_Type()
)
ruijievplsBgpVERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijievplsBgpVERowStatus.setStatus("current")
_RuijievplsBgpPwBindTable_Object = MibTable
ruijievplsBgpPwBindTable = _RuijievplsBgpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 2)
)
if mibBuilder.loadTexts:
    ruijievplsBgpPwBindTable.setStatus("current")
_RuijievplsBgpPwBindEntry_Object = MibTableRow
ruijievplsBgpPwBindEntry = _RuijievplsBgpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 2, 1)
)
ruijievplsBgpPwBindEntry.setIndexNames(
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsConfigIndex"),
    (0, "RUIJIE-VPLS-GENERIC-MIB", "ruijievplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    ruijievplsBgpPwBindEntry.setStatus("current")


class _RuijievplsBgpPwBindLocalVEId_Type(Unsigned32):
    """Custom type ruijievplsBgpPwBindLocalVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RuijievplsBgpPwBindLocalVEId_Type.__name__ = "Unsigned32"
_RuijievplsBgpPwBindLocalVEId_Object = MibTableColumn
ruijievplsBgpPwBindLocalVEId = _RuijievplsBgpPwBindLocalVEId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 2, 1, 1),
    _RuijievplsBgpPwBindLocalVEId_Type()
)
ruijievplsBgpPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsBgpPwBindLocalVEId.setStatus("current")


class _RuijievplsBgpPwBindRemoteVEId_Type(Unsigned32):
    """Custom type ruijievplsBgpPwBindRemoteVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RuijievplsBgpPwBindRemoteVEId_Type.__name__ = "Unsigned32"
_RuijievplsBgpPwBindRemoteVEId_Object = MibTableColumn
ruijievplsBgpPwBindRemoteVEId = _RuijievplsBgpPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 1, 2, 1, 2),
    _RuijievplsBgpPwBindRemoteVEId_Type()
)
ruijievplsBgpPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijievplsBgpPwBindRemoteVEId.setStatus("current")
_RuijievplsBgpConformance_ObjectIdentity = ObjectIdentity
ruijievplsBgpConformance = _RuijievplsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2)
)
_RuijievplsBgpCompliances_ObjectIdentity = ObjectIdentity
ruijievplsBgpCompliances = _RuijievplsBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2, 1)
)
_RuijievplsBgpGroups_ObjectIdentity = ObjectIdentity
ruijievplsBgpGroups = _RuijievplsBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2, 2)
)

# Managed Objects groups

ruijievplsBgpVEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2, 2, 2)
)
ruijievplsBgpVEGroup.setObjects(
    ("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpVEPreference")
)
if mibBuilder.loadTexts:
    ruijievplsBgpVEGroup.setStatus("current")

ruijievplsBgpPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2, 2, 3)
)
ruijievplsBgpPwBindGroup.setObjects(
      *(("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpPwBindLocalVEId"),
        ("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpPwBindRemoteVEId"))
)
if mibBuilder.loadTexts:
    ruijievplsBgpPwBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijievplsBgpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2, 1, 1)
)
ruijievplsBgpModuleFullCompliance.setObjects(
      *(("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpVEGroup"),
        ("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    ruijievplsBgpModuleFullCompliance.setStatus(
        "current"
    )

ruijievplsBgpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 79, 2, 1, 2)
)
ruijievplsBgpModuleReadOnlyCompliance.setObjects(
      *(("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpVEGroup"),
        ("RUIJIE-VPLS-BGP-MIB", "ruijievplsBgpPwBindGroup"))
)
if mibBuilder.loadTexts:
    ruijievplsBgpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VPLS-BGP-MIB",
    **{"RuijieVplsBgpRouteDistinguisher": RuijieVplsBgpRouteDistinguisher,
       "RuijieVplsBgpRouteTarget": RuijieVplsBgpRouteTarget,
       "ruijievplsBgpDraft01MIB": ruijievplsBgpDraft01MIB,
       "ruijievplsBgpObjects": ruijievplsBgpObjects,
       "ruijievplsBgpVETable": ruijievplsBgpVETable,
       "ruijievplsBgpVEEntry": ruijievplsBgpVEEntry,
       "ruijievplsBgpVEindex": ruijievplsBgpVEindex,
       "ruijievplsBgpVEId": ruijievplsBgpVEId,
       "ruijievplsBgpRangeSize": ruijievplsBgpRangeSize,
       "ruijievplsBgpVEPreference": ruijievplsBgpVEPreference,
       "ruijievplsBgpVERowStatus": ruijievplsBgpVERowStatus,
       "ruijievplsBgpPwBindTable": ruijievplsBgpPwBindTable,
       "ruijievplsBgpPwBindEntry": ruijievplsBgpPwBindEntry,
       "ruijievplsBgpPwBindLocalVEId": ruijievplsBgpPwBindLocalVEId,
       "ruijievplsBgpPwBindRemoteVEId": ruijievplsBgpPwBindRemoteVEId,
       "ruijievplsBgpConformance": ruijievplsBgpConformance,
       "ruijievplsBgpCompliances": ruijievplsBgpCompliances,
       "ruijievplsBgpModuleFullCompliance": ruijievplsBgpModuleFullCompliance,
       "ruijievplsBgpModuleReadOnlyCompliance": ruijievplsBgpModuleReadOnlyCompliance,
       "ruijievplsBgpGroups": ruijievplsBgpGroups,
       "ruijievplsBgpVEGroup": ruijievplsBgpVEGroup,
       "ruijievplsBgpPwBindGroup": ruijievplsBgpPwBindGroup}
)
