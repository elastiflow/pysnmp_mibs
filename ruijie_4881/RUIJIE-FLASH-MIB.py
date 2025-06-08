# SNMP MIB module (RUIJIE-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-FLASH-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

ruijieFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47)
)
if mibBuilder.loadTexts:
    ruijieFlashMIB.setRevisions(
        ("2009-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieFlashMIBObjects_ObjectIdentity = ObjectIdentity
ruijieFlashMIBObjects = _RuijieFlashMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1)
)
_RuijieFlashDeviceTable_Object = MibTable
ruijieFlashDeviceTable = _RuijieFlashDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieFlashDeviceTable.setStatus("current")
_RuijieFlashDeviceEntry_Object = MibTableRow
ruijieFlashDeviceEntry = _RuijieFlashDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1, 1)
)
ruijieFlashDeviceEntry.setIndexNames(
    (0, "RUIJIE-FLASH-MIB", "ruijieFlashDeviceIndex"),
)
if mibBuilder.loadTexts:
    ruijieFlashDeviceEntry.setStatus("current")
_RuijieFlashDeviceIndex_Type = Unsigned32
_RuijieFlashDeviceIndex_Object = MibTableColumn
ruijieFlashDeviceIndex = _RuijieFlashDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1, 1, 1),
    _RuijieFlashDeviceIndex_Type()
)
ruijieFlashDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFlashDeviceIndex.setStatus("current")
_RuijieFlashDeviceName_Type = DisplayString
_RuijieFlashDeviceName_Object = MibTableColumn
ruijieFlashDeviceName = _RuijieFlashDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1, 1, 2),
    _RuijieFlashDeviceName_Type()
)
ruijieFlashDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFlashDeviceName.setStatus("current")
_RuijieFlashDeviceSize_Type = Unsigned32
_RuijieFlashDeviceSize_Object = MibTableColumn
ruijieFlashDeviceSize = _RuijieFlashDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1, 1, 3),
    _RuijieFlashDeviceSize_Type()
)
ruijieFlashDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFlashDeviceSize.setStatus("current")
_RuijieFlashDeviceUsed_Type = Unsigned32
_RuijieFlashDeviceUsed_Object = MibTableColumn
ruijieFlashDeviceUsed = _RuijieFlashDeviceUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1, 1, 4),
    _RuijieFlashDeviceUsed_Type()
)
ruijieFlashDeviceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFlashDeviceUsed.setStatus("current")
_RuijieFlashDeviceFree_Type = Unsigned32
_RuijieFlashDeviceFree_Object = MibTableColumn
ruijieFlashDeviceFree = _RuijieFlashDeviceFree_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 1, 1, 5),
    _RuijieFlashDeviceFree_Type()
)
ruijieFlashDeviceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFlashDeviceFree.setStatus("current")
_RuijieBootromDeviceTable_Object = MibTable
ruijieBootromDeviceTable = _RuijieBootromDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieBootromDeviceTable.setStatus("current")
_RuijieBootromDeviceEntry_Object = MibTableRow
ruijieBootromDeviceEntry = _RuijieBootromDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 2, 1)
)
ruijieBootromDeviceEntry.setIndexNames(
    (0, "RUIJIE-FLASH-MIB", "ruijieBootromDeviceIndex"),
)
if mibBuilder.loadTexts:
    ruijieBootromDeviceEntry.setStatus("current")
_RuijieBootromDeviceIndex_Type = Unsigned32
_RuijieBootromDeviceIndex_Object = MibTableColumn
ruijieBootromDeviceIndex = _RuijieBootromDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 2, 1, 1),
    _RuijieBootromDeviceIndex_Type()
)
ruijieBootromDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBootromDeviceIndex.setStatus("current")
_RuijieBootromDeviceName_Type = DisplayString
_RuijieBootromDeviceName_Object = MibTableColumn
ruijieBootromDeviceName = _RuijieBootromDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 2, 1, 2),
    _RuijieBootromDeviceName_Type()
)
ruijieBootromDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBootromDeviceName.setStatus("current")
_RuijieBootromDeviceSize_Type = Unsigned32
_RuijieBootromDeviceSize_Object = MibTableColumn
ruijieBootromDeviceSize = _RuijieBootromDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 1, 2, 1, 3),
    _RuijieBootromDeviceSize_Type()
)
ruijieBootromDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBootromDeviceSize.setStatus("current")
_RuijieFlashMIBConformance_ObjectIdentity = ObjectIdentity
ruijieFlashMIBConformance = _RuijieFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 2)
)
_RuijieFlashMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieFlashMIBCompliances = _RuijieFlashMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 2, 1)
)
_RuijieFlashMIBGroups_ObjectIdentity = ObjectIdentity
ruijieFlashMIBGroups = _RuijieFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 2, 2)
)

# Managed Objects groups

ruijieFlashMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 2, 2, 1)
)
ruijieFlashMIBGroup.setObjects(
      *(("RUIJIE-FLASH-MIB", "ruijieFlashDeviceIndex"),
        ("RUIJIE-FLASH-MIB", "ruijieFlashDeviceName"),
        ("RUIJIE-FLASH-MIB", "ruijieFlashDeviceSize"),
        ("RUIJIE-FLASH-MIB", "ruijieFlashDeviceUsed"),
        ("RUIJIE-FLASH-MIB", "ruijieFlashDeviceFree"))
)
if mibBuilder.loadTexts:
    ruijieFlashMIBGroup.setStatus("current")

ruijieBootromDeviceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 2, 2, 2)
)
ruijieBootromDeviceMIBGroup.setObjects(
      *(("RUIJIE-FLASH-MIB", "ruijieBootromDeviceIndex"),
        ("RUIJIE-FLASH-MIB", "ruijieBootromDeviceName"),
        ("RUIJIE-FLASH-MIB", "ruijieBootromDeviceSize"))
)
if mibBuilder.loadTexts:
    ruijieBootromDeviceMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieFlashMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 47, 2, 1, 1)
)
ruijieFlashMIBCompliance.setObjects(
    ("RUIJIE-FLASH-MIB", "ruijieFlashMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieFlashMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-FLASH-MIB",
    **{"ruijieFlashMIB": ruijieFlashMIB,
       "ruijieFlashMIBObjects": ruijieFlashMIBObjects,
       "ruijieFlashDeviceTable": ruijieFlashDeviceTable,
       "ruijieFlashDeviceEntry": ruijieFlashDeviceEntry,
       "ruijieFlashDeviceIndex": ruijieFlashDeviceIndex,
       "ruijieFlashDeviceName": ruijieFlashDeviceName,
       "ruijieFlashDeviceSize": ruijieFlashDeviceSize,
       "ruijieFlashDeviceUsed": ruijieFlashDeviceUsed,
       "ruijieFlashDeviceFree": ruijieFlashDeviceFree,
       "ruijieBootromDeviceTable": ruijieBootromDeviceTable,
       "ruijieBootromDeviceEntry": ruijieBootromDeviceEntry,
       "ruijieBootromDeviceIndex": ruijieBootromDeviceIndex,
       "ruijieBootromDeviceName": ruijieBootromDeviceName,
       "ruijieBootromDeviceSize": ruijieBootromDeviceSize,
       "ruijieFlashMIBConformance": ruijieFlashMIBConformance,
       "ruijieFlashMIBCompliances": ruijieFlashMIBCompliances,
       "ruijieFlashMIBCompliance": ruijieFlashMIBCompliance,
       "ruijieFlashMIBGroups": ruijieFlashMIBGroups,
       "ruijieFlashMIBGroup": ruijieFlashMIBGroup,
       "ruijieBootromDeviceMIBGroup": ruijieBootromDeviceMIBGroup}
)
