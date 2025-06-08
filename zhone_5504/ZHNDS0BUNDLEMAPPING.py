# SNMP MIB module (ZHNDS0BUNDLEMAPPING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHNDS0BUNDLEMAPPING.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:24:44 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

zhnDs0BundleMapping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35)
)
if mibBuilder.loadTexts:
    zhnDs0BundleMapping.setRevisions(
        ("2011-10-06 00:00",
         "2011-09-08 00:00",
         "2008-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhnDs0BundleMappingNotifications_ObjectIdentity = ObjectIdentity
zhnDs0BundleMappingNotifications = _ZhnDs0BundleMappingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 0)
)
_ZhnDs0BundleMappingObjects_ObjectIdentity = ObjectIdentity
zhnDs0BundleMappingObjects = _ZhnDs0BundleMappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1)
)
_ZhnDs0BundleMappingTable_Object = MibTable
zhnDs0BundleMappingTable = _ZhnDs0BundleMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 1)
)
if mibBuilder.loadTexts:
    zhnDs0BundleMappingTable.setStatus("current")
_ZhnDs0BundleMappingEntry_Object = MibTableRow
zhnDs0BundleMappingEntry = _ZhnDs0BundleMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 1, 1)
)
zhnDs0BundleMappingEntry.setIndexNames(
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0BundleName"),
)
if mibBuilder.loadTexts:
    zhnDs0BundleMappingEntry.setStatus("current")


class _ZhnDs0BundleName_Type(DisplayString):
    """Custom type zhnDs0BundleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0BundleName_Type.__name__ = "DisplayString"
_ZhnDs0BundleName_Object = MibTableColumn
zhnDs0BundleName = _ZhnDs0BundleName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 1, 1, 1),
    _ZhnDs0BundleName_Type()
)
zhnDs0BundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnDs0BundleName.setStatus("current")


class _ZhnDs0BundleStartInterfaceName_Type(DisplayString):
    """Custom type zhnDs0BundleStartInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0BundleStartInterfaceName_Type.__name__ = "DisplayString"
_ZhnDs0BundleStartInterfaceName_Object = MibTableColumn
zhnDs0BundleStartInterfaceName = _ZhnDs0BundleStartInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 1, 1, 2),
    _ZhnDs0BundleStartInterfaceName_Type()
)
zhnDs0BundleStartInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhnDs0BundleStartInterfaceName.setStatus("current")


class _ZhnDs0BundleEndInterfaceName_Type(DisplayString):
    """Custom type zhnDs0BundleEndInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0BundleEndInterfaceName_Type.__name__ = "DisplayString"
_ZhnDs0BundleEndInterfaceName_Object = MibTableColumn
zhnDs0BundleEndInterfaceName = _ZhnDs0BundleEndInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 1, 1, 3),
    _ZhnDs0BundleEndInterfaceName_Type()
)
zhnDs0BundleEndInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnDs0BundleEndInterfaceName.setStatus("current")
_ZhnDs0BundleMappingRowStatus_Type = RowStatus
_ZhnDs0BundleMappingRowStatus_Object = MibTableColumn
zhnDs0BundleMappingRowStatus = _ZhnDs0BundleMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 1, 1, 4),
    _ZhnDs0BundleMappingRowStatus_Type()
)
zhnDs0BundleMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnDs0BundleMappingRowStatus.setStatus("current")
_ZhnDs0ChannelMappingTable_Object = MibTable
zhnDs0ChannelMappingTable = _ZhnDs0ChannelMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 2)
)
if mibBuilder.loadTexts:
    zhnDs0ChannelMappingTable.setStatus("current")
_ZhnDs0ChannelMappingEntry_Object = MibTableRow
zhnDs0ChannelMappingEntry = _ZhnDs0ChannelMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 2, 1)
)
zhnDs0ChannelMappingEntry.setIndexNames(
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0ChannelNumber"),
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0ChannelDs1PortName"),
)
if mibBuilder.loadTexts:
    zhnDs0ChannelMappingEntry.setStatus("current")


class _ZhnDs0ChannelNumber_Type(Integer32):
    """Custom type zhnDs0ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ZhnDs0ChannelNumber_Type.__name__ = "Integer32"
_ZhnDs0ChannelNumber_Object = MibTableColumn
zhnDs0ChannelNumber = _ZhnDs0ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 2, 1, 1),
    _ZhnDs0ChannelNumber_Type()
)
zhnDs0ChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhnDs0ChannelNumber.setStatus("current")


class _ZhnDs0ChannelDs1PortName_Type(DisplayString):
    """Custom type zhnDs0ChannelDs1PortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0ChannelDs1PortName_Type.__name__ = "DisplayString"
_ZhnDs0ChannelDs1PortName_Object = MibTableColumn
zhnDs0ChannelDs1PortName = _ZhnDs0ChannelDs1PortName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 2, 1, 2),
    _ZhnDs0ChannelDs1PortName_Type()
)
zhnDs0ChannelDs1PortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhnDs0ChannelDs1PortName.setStatus("current")


class _ZhnDs0ChannelMappingBundleName_Type(DisplayString):
    """Custom type zhnDs0ChannelMappingBundleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0ChannelMappingBundleName_Type.__name__ = "DisplayString"
_ZhnDs0ChannelMappingBundleName_Object = MibTableColumn
zhnDs0ChannelMappingBundleName = _ZhnDs0ChannelMappingBundleName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 2, 1, 3),
    _ZhnDs0ChannelMappingBundleName_Type()
)
zhnDs0ChannelMappingBundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnDs0ChannelMappingBundleName.setStatus("current")
_ZhnDs0ChannelMappingRowStatus_Type = RowStatus
_ZhnDs0ChannelMappingRowStatus_Object = MibTableColumn
zhnDs0ChannelMappingRowStatus = _ZhnDs0ChannelMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 2, 1, 4),
    _ZhnDs0ChannelMappingRowStatus_Type()
)
zhnDs0ChannelMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnDs0ChannelMappingRowStatus.setStatus("current")
_ZhnDs0IfIndex_Type = InterfaceIndex
_ZhnDs0IfIndex_Object = MibScalar
zhnDs0IfIndex = _ZhnDs0IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 3),
    _ZhnDs0IfIndex_Type()
)
zhnDs0IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0IfIndex.setStatus("current")
_ZhnDs1IfIndex_Type = InterfaceIndex
_ZhnDs1IfIndex_Object = MibScalar
zhnDs1IfIndex = _ZhnDs1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 4),
    _ZhnDs1IfIndex_Type()
)
zhnDs1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs1IfIndex.setStatus("current")
_ZhnDs0BundleConfigTable_Object = MibTable
zhnDs0BundleConfigTable = _ZhnDs0BundleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 5)
)
if mibBuilder.loadTexts:
    zhnDs0BundleConfigTable.setStatus("current")
_ZhnDs0BundleConfigEntry_Object = MibTableRow
zhnDs0BundleConfigEntry = _ZhnDs0BundleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 5, 1)
)
zhnDs0BundleConfigEntry.setIndexNames(
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0BundleConfigIndex"),
)
if mibBuilder.loadTexts:
    zhnDs0BundleConfigEntry.setStatus("current")


class _ZhnDs0BundleConfigIndex_Type(Integer32):
    """Custom type zhnDs0BundleConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhnDs0BundleConfigIndex_Type.__name__ = "Integer32"
_ZhnDs0BundleConfigIndex_Object = MibTableColumn
zhnDs0BundleConfigIndex = _ZhnDs0BundleConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 5, 1, 1),
    _ZhnDs0BundleConfigIndex_Type()
)
zhnDs0BundleConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0BundleConfigIndex.setStatus("current")


class _ZhnDs0BundleConfigName_Type(DisplayString):
    """Custom type zhnDs0BundleConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0BundleConfigName_Type.__name__ = "DisplayString"
_ZhnDs0BundleConfigName_Object = MibTableColumn
zhnDs0BundleConfigName = _ZhnDs0BundleConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 5, 1, 2),
    _ZhnDs0BundleConfigName_Type()
)
zhnDs0BundleConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0BundleConfigName.setStatus("current")


class _ZhnDs0BundleConfigCircuitId_Type(DisplayString):
    """Custom type zhnDs0BundleConfigCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZhnDs0BundleConfigCircuitId_Type.__name__ = "DisplayString"
_ZhnDs0BundleConfigCircuitId_Object = MibTableColumn
zhnDs0BundleConfigCircuitId = _ZhnDs0BundleConfigCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 5, 1, 3),
    _ZhnDs0BundleConfigCircuitId_Type()
)
zhnDs0BundleConfigCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0BundleConfigCircuitId.setStatus("current")
_ZhnDs0TimeslotTable_Object = MibTable
zhnDs0TimeslotTable = _ZhnDs0TimeslotTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6)
)
if mibBuilder.loadTexts:
    zhnDs0TimeslotTable.setStatus("current")
_ZhnDs0TimeslotEntry_Object = MibTableRow
zhnDs0TimeslotEntry = _ZhnDs0TimeslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1)
)
zhnDs0TimeslotEntry.setIndexNames(
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0TimeslotBundleIndex"),
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0TimeslotDsx1LineIndex"),
    (0, "ZHNDS0BUNDLEMAPPING", "zhnDs0TimeslotStartIndex"),
)
if mibBuilder.loadTexts:
    zhnDs0TimeslotEntry.setStatus("current")
_ZhnDs0TimeslotBundleIndex_Type = Integer32
_ZhnDs0TimeslotBundleIndex_Object = MibTableColumn
zhnDs0TimeslotBundleIndex = _ZhnDs0TimeslotBundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 1),
    _ZhnDs0TimeslotBundleIndex_Type()
)
zhnDs0TimeslotBundleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotBundleIndex.setStatus("current")


class _ZhnDs0TimeslotBundleName_Type(DisplayString):
    """Custom type zhnDs0TimeslotBundleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhnDs0TimeslotBundleName_Type.__name__ = "DisplayString"
_ZhnDs0TimeslotBundleName_Object = MibTableColumn
zhnDs0TimeslotBundleName = _ZhnDs0TimeslotBundleName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 2),
    _ZhnDs0TimeslotBundleName_Type()
)
zhnDs0TimeslotBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotBundleName.setStatus("current")
_ZhnDs0TimeslotDsx1LineIndex_Type = Integer32
_ZhnDs0TimeslotDsx1LineIndex_Object = MibTableColumn
zhnDs0TimeslotDsx1LineIndex = _ZhnDs0TimeslotDsx1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 3),
    _ZhnDs0TimeslotDsx1LineIndex_Type()
)
zhnDs0TimeslotDsx1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotDsx1LineIndex.setStatus("current")
_ZhnDs0TimeslotStartIndex_Type = Integer32
_ZhnDs0TimeslotStartIndex_Object = MibTableColumn
zhnDs0TimeslotStartIndex = _ZhnDs0TimeslotStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 4),
    _ZhnDs0TimeslotStartIndex_Type()
)
zhnDs0TimeslotStartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotStartIndex.setStatus("current")


class _ZhnDs0TimeslotStartName_Type(DisplayString):
    """Custom type zhnDs0TimeslotStartName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhnDs0TimeslotStartName_Type.__name__ = "DisplayString"
_ZhnDs0TimeslotStartName_Object = MibTableColumn
zhnDs0TimeslotStartName = _ZhnDs0TimeslotStartName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 5),
    _ZhnDs0TimeslotStartName_Type()
)
zhnDs0TimeslotStartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotStartName.setStatus("current")
_ZhnDs0TimeslotEndIndex_Type = Integer32
_ZhnDs0TimeslotEndIndex_Object = MibTableColumn
zhnDs0TimeslotEndIndex = _ZhnDs0TimeslotEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 6),
    _ZhnDs0TimeslotEndIndex_Type()
)
zhnDs0TimeslotEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotEndIndex.setStatus("current")


class _ZhnDs0TimeslotEndName_Type(DisplayString):
    """Custom type zhnDs0TimeslotEndName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZhnDs0TimeslotEndName_Type.__name__ = "DisplayString"
_ZhnDs0TimeslotEndName_Object = MibTableColumn
zhnDs0TimeslotEndName = _ZhnDs0TimeslotEndName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 7),
    _ZhnDs0TimeslotEndName_Type()
)
zhnDs0TimeslotEndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnDs0TimeslotEndName.setStatus("current")
_ZhnDs0TimeslotMappingRowStatus_Type = RowStatus
_ZhnDs0TimeslotMappingRowStatus_Object = MibTableColumn
zhnDs0TimeslotMappingRowStatus = _ZhnDs0TimeslotMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 1, 6, 1, 8),
    _ZhnDs0TimeslotMappingRowStatus_Type()
)
zhnDs0TimeslotMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnDs0TimeslotMappingRowStatus.setStatus("current")
_ZhnDs0BundleMappingConformance_ObjectIdentity = ObjectIdentity
zhnDs0BundleMappingConformance = _ZhnDs0BundleMappingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 2)
)
_ZhnDs0BundleMappingGroups_ObjectIdentity = ObjectIdentity
zhnDs0BundleMappingGroups = _ZhnDs0BundleMappingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 2, 1)
)
_ZhnDs0BundleMappingCompliances_ObjectIdentity = ObjectIdentity
zhnDs0BundleMappingCompliances = _ZhnDs0BundleMappingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 2, 2)
)

# Managed Objects groups

zhnBundleMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 2, 1, 1)
)
zhnBundleMappingGroup.setObjects(
      *(("ZHNDS0BUNDLEMAPPING", "zhnDs0BundleEndInterfaceName"),
        ("ZHNDS0BUNDLEMAPPING", "zhnDs0BundleMappingRowStatus"))
)
if mibBuilder.loadTexts:
    zhnBundleMappingGroup.setStatus("current")

zhnChannelMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 2, 1, 2)
)
zhnChannelMappingGroup.setObjects(
      *(("ZHNDS0BUNDLEMAPPING", "zhnDs0ChannelMappingBundleName"),
        ("ZHNDS0BUNDLEMAPPING", "zhnDs0ChannelMappingRowStatus"))
)
if mibBuilder.loadTexts:
    zhnChannelMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnDs0BundleMappingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 35, 2, 2, 1)
)
zhnDs0BundleMappingCompliance.setObjects(
      *(("ZHNDS0BUNDLEMAPPING", "zhnBundleMappingGroup"),
        ("ZHNDS0BUNDLEMAPPING", "zhnChannelMappingGroup"))
)
if mibBuilder.loadTexts:
    zhnDs0BundleMappingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNDS0BUNDLEMAPPING",
    **{"zhnDs0BundleMapping": zhnDs0BundleMapping,
       "zhnDs0BundleMappingNotifications": zhnDs0BundleMappingNotifications,
       "zhnDs0BundleMappingObjects": zhnDs0BundleMappingObjects,
       "zhnDs0BundleMappingTable": zhnDs0BundleMappingTable,
       "zhnDs0BundleMappingEntry": zhnDs0BundleMappingEntry,
       "zhnDs0BundleName": zhnDs0BundleName,
       "zhnDs0BundleStartInterfaceName": zhnDs0BundleStartInterfaceName,
       "zhnDs0BundleEndInterfaceName": zhnDs0BundleEndInterfaceName,
       "zhnDs0BundleMappingRowStatus": zhnDs0BundleMappingRowStatus,
       "zhnDs0ChannelMappingTable": zhnDs0ChannelMappingTable,
       "zhnDs0ChannelMappingEntry": zhnDs0ChannelMappingEntry,
       "zhnDs0ChannelNumber": zhnDs0ChannelNumber,
       "zhnDs0ChannelDs1PortName": zhnDs0ChannelDs1PortName,
       "zhnDs0ChannelMappingBundleName": zhnDs0ChannelMappingBundleName,
       "zhnDs0ChannelMappingRowStatus": zhnDs0ChannelMappingRowStatus,
       "zhnDs0IfIndex": zhnDs0IfIndex,
       "zhnDs1IfIndex": zhnDs1IfIndex,
       "zhnDs0BundleConfigTable": zhnDs0BundleConfigTable,
       "zhnDs0BundleConfigEntry": zhnDs0BundleConfigEntry,
       "zhnDs0BundleConfigIndex": zhnDs0BundleConfigIndex,
       "zhnDs0BundleConfigName": zhnDs0BundleConfigName,
       "zhnDs0BundleConfigCircuitId": zhnDs0BundleConfigCircuitId,
       "zhnDs0TimeslotTable": zhnDs0TimeslotTable,
       "zhnDs0TimeslotEntry": zhnDs0TimeslotEntry,
       "zhnDs0TimeslotBundleIndex": zhnDs0TimeslotBundleIndex,
       "zhnDs0TimeslotBundleName": zhnDs0TimeslotBundleName,
       "zhnDs0TimeslotDsx1LineIndex": zhnDs0TimeslotDsx1LineIndex,
       "zhnDs0TimeslotStartIndex": zhnDs0TimeslotStartIndex,
       "zhnDs0TimeslotStartName": zhnDs0TimeslotStartName,
       "zhnDs0TimeslotEndIndex": zhnDs0TimeslotEndIndex,
       "zhnDs0TimeslotEndName": zhnDs0TimeslotEndName,
       "zhnDs0TimeslotMappingRowStatus": zhnDs0TimeslotMappingRowStatus,
       "zhnDs0BundleMappingConformance": zhnDs0BundleMappingConformance,
       "zhnDs0BundleMappingGroups": zhnDs0BundleMappingGroups,
       "zhnBundleMappingGroup": zhnBundleMappingGroup,
       "zhnChannelMappingGroup": zhnChannelMappingGroup,
       "zhnDs0BundleMappingCompliances": zhnDs0BundleMappingCompliances,
       "zhnDs0BundleMappingCompliance": zhnDs0BundleMappingCompliance}
)
