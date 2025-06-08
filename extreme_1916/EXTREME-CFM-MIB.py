# SNMP MIB module (EXTREME-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-CFM-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:22:20 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmMepId,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmMepId",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

extremeCfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47)
)
if mibBuilder.loadTexts:
    extremeCfm.setRevisions(
        ("2015-05-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ExtremeCfmGroupOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeCfmNotifications_ObjectIdentity = ObjectIdentity
extremeCfmNotifications = _ExtremeCfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 0)
)
_ExtremeCfmMibObjects_ObjectIdentity = ObjectIdentity
extremeCfmMibObjects = _ExtremeCfmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1)
)
_ExtremeCfmGroup_ObjectIdentity = ObjectIdentity
extremeCfmGroup = _ExtremeCfmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1)
)
_ExtremeCfmGroupNextIndexTable_Object = MibTable
extremeCfmGroupNextIndexTable = _ExtremeCfmGroupNextIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 1)
)
if mibBuilder.loadTexts:
    extremeCfmGroupNextIndexTable.setStatus("current")
_ExtremeCfmGroupNextIndexEntry_Object = MibTableRow
extremeCfmGroupNextIndexEntry = _ExtremeCfmGroupNextIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 1, 1)
)
extremeCfmGroupNextIndexEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    extremeCfmGroupNextIndexEntry.setStatus("current")
_ExtremeCfmGroupNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_ExtremeCfmGroupNextIndex_Object = MibTableColumn
extremeCfmGroupNextIndex = _ExtremeCfmGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 1, 1, 1),
    _ExtremeCfmGroupNextIndex_Type()
)
extremeCfmGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCfmGroupNextIndex.setStatus("current")
_ExtremeCfmGroupTable_Object = MibTable
extremeCfmGroupTable = _ExtremeCfmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2)
)
if mibBuilder.loadTexts:
    extremeCfmGroupTable.setStatus("current")
_ExtremeCfmGroupEntry_Object = MibTableRow
extremeCfmGroupEntry = _ExtremeCfmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1)
)
extremeCfmGroupEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "EXTREME-CFM-MIB", "extremeCfmGroupIndex"),
)
if mibBuilder.loadTexts:
    extremeCfmGroupEntry.setStatus("current")


class _ExtremeCfmGroupIndex_Type(Unsigned32):
    """Custom type extremeCfmGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExtremeCfmGroupIndex_Type.__name__ = "Unsigned32"
_ExtremeCfmGroupIndex_Object = MibTableColumn
extremeCfmGroupIndex = _ExtremeCfmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 1),
    _ExtremeCfmGroupIndex_Type()
)
extremeCfmGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeCfmGroupIndex.setStatus("current")


class _ExtremeCfmGroupName_Type(DisplayString):
    """Custom type extremeCfmGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExtremeCfmGroupName_Type.__name__ = "DisplayString"
_ExtremeCfmGroupName_Object = MibTableColumn
extremeCfmGroupName = _ExtremeCfmGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 2),
    _ExtremeCfmGroupName_Type()
)
extremeCfmGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeCfmGroupName.setStatus("current")
_ExtremeCfmGroupStatus_Type = ExtremeCfmGroupOperStatus
_ExtremeCfmGroupStatus_Object = MibTableColumn
extremeCfmGroupStatus = _ExtremeCfmGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 3),
    _ExtremeCfmGroupStatus_Type()
)
extremeCfmGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCfmGroupStatus.setStatus("current")
_ExtremeCfmMepIfIndex_Type = InterfaceIndexOrZero
_ExtremeCfmMepIfIndex_Object = MibTableColumn
extremeCfmMepIfIndex = _ExtremeCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 4),
    _ExtremeCfmMepIfIndex_Type()
)
extremeCfmMepIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCfmMepIfIndex.setStatus("current")


class _ExtremeCfmGroupRemoteMEPs_Type(DisplayString):
    """Custom type extremeCfmGroupRemoteMEPs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtremeCfmGroupRemoteMEPs_Type.__name__ = "DisplayString"
_ExtremeCfmGroupRemoteMEPs_Object = MibTableColumn
extremeCfmGroupRemoteMEPs = _ExtremeCfmGroupRemoteMEPs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 5),
    _ExtremeCfmGroupRemoteMEPs_Type()
)
extremeCfmGroupRemoteMEPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCfmGroupRemoteMEPs.setStatus("current")


class _ExtremeCfmGroupClients_Type(DisplayString):
    """Custom type extremeCfmGroupClients based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtremeCfmGroupClients_Type.__name__ = "DisplayString"
_ExtremeCfmGroupClients_Object = MibTableColumn
extremeCfmGroupClients = _ExtremeCfmGroupClients_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 6),
    _ExtremeCfmGroupClients_Type()
)
extremeCfmGroupClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeCfmGroupClients.setStatus("current")
_ExtremeCfmGroupRowStatus_Type = RowStatus
_ExtremeCfmGroupRowStatus_Object = MibTableColumn
extremeCfmGroupRowStatus = _ExtremeCfmGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 2, 1, 7),
    _ExtremeCfmGroupRowStatus_Type()
)
extremeCfmGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeCfmGroupRowStatus.setStatus("current")
_ExtremeCfmGroupMepDbTable_Object = MibTable
extremeCfmGroupMepDbTable = _ExtremeCfmGroupMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 3)
)
if mibBuilder.loadTexts:
    extremeCfmGroupMepDbTable.setStatus("current")
_ExtremeCfmGroupMepDbEntry_Object = MibTableRow
extremeCfmGroupMepDbEntry = _ExtremeCfmGroupMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 3, 1)
)
extremeCfmGroupMepDbEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "EXTREME-CFM-MIB", "extremeCfmGroupIndex"),
    (0, "EXTREME-CFM-MIB", "extremeCfmGroupMepDbRMepId"),
)
if mibBuilder.loadTexts:
    extremeCfmGroupMepDbEntry.setStatus("current")
_ExtremeCfmGroupMepDbRMepId_Type = Dot1agCfmMepId
_ExtremeCfmGroupMepDbRMepId_Object = MibTableColumn
extremeCfmGroupMepDbRMepId = _ExtremeCfmGroupMepDbRMepId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 3, 1, 1),
    _ExtremeCfmGroupMepDbRMepId_Type()
)
extremeCfmGroupMepDbRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeCfmGroupMepDbRMepId.setStatus("current")
_ExtremeCfmGroupMepDbRowStatus_Type = RowStatus
_ExtremeCfmGroupMepDbRowStatus_Object = MibTableColumn
extremeCfmGroupMepDbRowStatus = _ExtremeCfmGroupMepDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 1, 1, 3, 1, 2),
    _ExtremeCfmGroupMepDbRowStatus_Type()
)
extremeCfmGroupMepDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeCfmGroupMepDbRowStatus.setStatus("current")
_ExtremeCfmMibConformance_ObjectIdentity = ObjectIdentity
extremeCfmMibConformance = _ExtremeCfmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2)
)
_ExtremeCfmMibCompliances_ObjectIdentity = ObjectIdentity
extremeCfmMibCompliances = _ExtremeCfmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2, 1)
)
_ExtremeCfmMibGroups_ObjectIdentity = ObjectIdentity
extremeCfmMibGroups = _ExtremeCfmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2, 2)
)

# Managed Objects groups

extremeCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2, 2, 1)
)
extremeCfmMepGroup.setObjects(
      *(("EXTREME-CFM-MIB", "extremeCfmGroupNextIndex"),
        ("EXTREME-CFM-MIB", "extremeCfmGroupName"),
        ("EXTREME-CFM-MIB", "extremeCfmGroupStatus"),
        ("EXTREME-CFM-MIB", "extremeCfmMepIfIndex"),
        ("EXTREME-CFM-MIB", "extremeCfmGroupRemoteMEPs"),
        ("EXTREME-CFM-MIB", "extremeCfmGroupClients"),
        ("EXTREME-CFM-MIB", "extremeCfmGroupRowStatus"))
)
if mibBuilder.loadTexts:
    extremeCfmMepGroup.setStatus("current")

extremeCfmMepDbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2, 2, 2)
)
extremeCfmMepDbGroup.setObjects(
    ("EXTREME-CFM-MIB", "extremeCfmGroupMepDbRowStatus")
)
if mibBuilder.loadTexts:
    extremeCfmMepDbGroup.setStatus("current")


# Notification objects

extremeCfmGroupStatusDownUpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 0, 1)
)
extremeCfmGroupStatusDownUpAlarm.setObjects(
    ("EXTREME-CFM-MIB", "extremeCfmGroupStatus")
)
if mibBuilder.loadTexts:
    extremeCfmGroupStatusDownUpAlarm.setStatus(
        "current"
    )


# Notifications groups

extremeCfmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2, 2, 3)
)
extremeCfmNotificationsGroup.setObjects(
    ("EXTREME-CFM-MIB", "extremeCfmGroupStatusDownUpAlarm")
)
if mibBuilder.loadTexts:
    extremeCfmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

extremeCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47, 2, 1, 1)
)
extremeCfmCompliance.setObjects(
      *(("EXTREME-CFM-MIB", "extremeCfmMepGroup"),
        ("EXTREME-CFM-MIB", "extremeCfmMepDbGroup"),
        ("EXTREME-CFM-MIB", "extremeCfmNotificationsGroup"))
)
if mibBuilder.loadTexts:
    extremeCfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-CFM-MIB",
    **{"ExtremeCfmGroupOperStatus": ExtremeCfmGroupOperStatus,
       "extremeCfm": extremeCfm,
       "extremeCfmNotifications": extremeCfmNotifications,
       "extremeCfmGroupStatusDownUpAlarm": extremeCfmGroupStatusDownUpAlarm,
       "extremeCfmMibObjects": extremeCfmMibObjects,
       "extremeCfmGroup": extremeCfmGroup,
       "extremeCfmGroupNextIndexTable": extremeCfmGroupNextIndexTable,
       "extremeCfmGroupNextIndexEntry": extremeCfmGroupNextIndexEntry,
       "extremeCfmGroupNextIndex": extremeCfmGroupNextIndex,
       "extremeCfmGroupTable": extremeCfmGroupTable,
       "extremeCfmGroupEntry": extremeCfmGroupEntry,
       "extremeCfmGroupIndex": extremeCfmGroupIndex,
       "extremeCfmGroupName": extremeCfmGroupName,
       "extremeCfmGroupStatus": extremeCfmGroupStatus,
       "extremeCfmMepIfIndex": extremeCfmMepIfIndex,
       "extremeCfmGroupRemoteMEPs": extremeCfmGroupRemoteMEPs,
       "extremeCfmGroupClients": extremeCfmGroupClients,
       "extremeCfmGroupRowStatus": extremeCfmGroupRowStatus,
       "extremeCfmGroupMepDbTable": extremeCfmGroupMepDbTable,
       "extremeCfmGroupMepDbEntry": extremeCfmGroupMepDbEntry,
       "extremeCfmGroupMepDbRMepId": extremeCfmGroupMepDbRMepId,
       "extremeCfmGroupMepDbRowStatus": extremeCfmGroupMepDbRowStatus,
       "extremeCfmMibConformance": extremeCfmMibConformance,
       "extremeCfmMibCompliances": extremeCfmMibCompliances,
       "extremeCfmCompliance": extremeCfmCompliance,
       "extremeCfmMibGroups": extremeCfmMibGroups,
       "extremeCfmMepGroup": extremeCfmMepGroup,
       "extremeCfmMepDbGroup": extremeCfmMepDbGroup,
       "extremeCfmNotificationsGroup": extremeCfmNotificationsGroup}
)
