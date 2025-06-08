# SNMP MIB module (CISCO-PORT-CHANNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-PORT-CHANNEL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:25 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PortMemberList,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "PortMemberList")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoPortChannelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285)
)
if mibBuilder.loadTexts:
    ciscoPortChannelMIB.setRevisions(
        ("2017-02-28 00:00",
         "2004-09-13 00:00",
         "2004-06-08 00:00",
         "2004-03-11 00:00",
         "2003-05-28 00:00",
         "2002-10-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortChannelMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("on", 2),
          ("off", 3),
          ("desirable", 4))
    )



class PortChannelGroupMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("active", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPortChannelObjects_ObjectIdentity = ObjectIdentity
ciscoPortChannelObjects = _CiscoPortChannelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1)
)
_PortChannelConfig_ObjectIdentity = ObjectIdentity
portChannelConfig = _PortChannelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1)
)
_PortChannelTable_Object = MibTable
portChannelTable = _PortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1)
)
if mibBuilder.loadTexts:
    portChannelTable.setStatus("current")
_PortChannelEntry_Object = MibTableRow
portChannelEntry = _PortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1)
)
portChannelEntry.setIndexNames(
    (0, "CISCO-PORT-CHANNEL-MIB", "portChannelIndex"),
)
if mibBuilder.loadTexts:
    portChannelEntry.setStatus("current")


class _PortChannelIndex_Type(Unsigned32):
    """Custom type portChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_PortChannelIndex_Type.__name__ = "Unsigned32"
_PortChannelIndex_Object = MibTableColumn
portChannelIndex = _PortChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 1),
    _PortChannelIndex_Type()
)
portChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portChannelIndex.setStatus("current")
_PortChannelIfIndex_Type = InterfaceIndex
_PortChannelIfIndex_Object = MibTableColumn
portChannelIfIndex = _PortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 2),
    _PortChannelIfIndex_Type()
)
portChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelIfIndex.setStatus("current")


class _PortChannelAdminChannelMode_Type(PortChannelMode):
    """Custom type portChannelAdminChannelMode based on PortChannelMode"""
    defaultValue = 2


_PortChannelAdminChannelMode_Type.__name__ = "PortChannelMode"
_PortChannelAdminChannelMode_Object = MibTableColumn
portChannelAdminChannelMode = _PortChannelAdminChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 3),
    _PortChannelAdminChannelMode_Type()
)
portChannelAdminChannelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portChannelAdminChannelMode.setStatus("current")
_PortChannelOperChannelMode_Type = PortChannelMode
_PortChannelOperChannelMode_Object = MibTableColumn
portChannelOperChannelMode = _PortChannelOperChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 4),
    _PortChannelOperChannelMode_Type()
)
portChannelOperChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelOperChannelMode.setStatus("current")


class _PortChannelAddType_Type(Integer32):
    """Custom type portChannelAddType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("force", 2))
    )


_PortChannelAddType_Type.__name__ = "Integer32"
_PortChannelAddType_Object = MibTableColumn
portChannelAddType = _PortChannelAddType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 5),
    _PortChannelAddType_Type()
)
portChannelAddType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portChannelAddType.setStatus("current")


class _PortChannelLastActionStatus_Type(Integer32):
    """Custom type portChannelLastActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("successful", 1),
          ("failed", 2))
    )


_PortChannelLastActionStatus_Type.__name__ = "Integer32"
_PortChannelLastActionStatus_Object = MibTableColumn
portChannelLastActionStatus = _PortChannelLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 6),
    _PortChannelLastActionStatus_Type()
)
portChannelLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelLastActionStatus.setStatus("current")
_PortChannelLastActionStatusCause_Type = SnmpAdminString
_PortChannelLastActionStatusCause_Object = MibTableColumn
portChannelLastActionStatusCause = _PortChannelLastActionStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 7),
    _PortChannelLastActionStatusCause_Type()
)
portChannelLastActionStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelLastActionStatusCause.setStatus("current")
_PortChannelLastActionTime_Type = TimeStamp
_PortChannelLastActionTime_Object = MibTableColumn
portChannelLastActionTime = _PortChannelLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 8),
    _PortChannelLastActionTime_Type()
)
portChannelLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelLastActionTime.setStatus("current")


class _PortChannelMemberList_Type(PortMemberList):
    """Custom type portChannelMemberList based on PortMemberList"""
    defaultHexValue = ""


_PortChannelMemberList_Type.__name__ = "PortMemberList"
_PortChannelMemberList_Object = MibTableColumn
portChannelMemberList = _PortChannelMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 9),
    _PortChannelMemberList_Type()
)
portChannelMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portChannelMemberList.setStatus("current")
_PortChannelCreationTime_Type = TimeStamp
_PortChannelCreationTime_Object = MibTableColumn
portChannelCreationTime = _PortChannelCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 10),
    _PortChannelCreationTime_Type()
)
portChannelCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelCreationTime.setStatus("current")
_PortChannelRowStatus_Type = RowStatus
_PortChannelRowStatus_Object = MibTableColumn
portChannelRowStatus = _PortChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 11),
    _PortChannelRowStatus_Type()
)
portChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portChannelRowStatus.setStatus("current")


class _PortChannelMemberOperStatus_Type(PortMemberList):
    """Custom type portChannelMemberOperStatus based on PortMemberList"""
    defaultHexValue = ""


_PortChannelMemberOperStatus_Type.__name__ = "PortMemberList"
_PortChannelMemberOperStatus_Object = MibTableColumn
portChannelMemberOperStatus = _PortChannelMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 12),
    _PortChannelMemberOperStatus_Type()
)
portChannelMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelMemberOperStatus.setStatus("current")
_PortChannelProtocolEnable_Type = TruthValue
_PortChannelProtocolEnable_Object = MibScalar
portChannelProtocolEnable = _PortChannelProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 2),
    _PortChannelProtocolEnable_Type()
)
portChannelProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelProtocolEnable.setStatus("current")
_PortChannelGrpIfExtTable_Object = MibTable
portChannelGrpIfExtTable = _PortChannelGrpIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 3)
)
if mibBuilder.loadTexts:
    portChannelGrpIfExtTable.setStatus("current")
_PortChannelGrpIfExtEntry_Object = MibTableRow
portChannelGrpIfExtEntry = _PortChannelGrpIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 3, 1)
)
portChannelGrpIfExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portChannelGrpIfExtEntry.setStatus("current")
_PortChannelGrpIfAutoCreation_Type = TruthValue
_PortChannelGrpIfAutoCreation_Object = MibTableColumn
portChannelGrpIfAutoCreation = _PortChannelGrpIfAutoCreation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 3, 1, 1),
    _PortChannelGrpIfAutoCreation_Type()
)
portChannelGrpIfAutoCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelGrpIfAutoCreation.setStatus("current")
_PortChannelExtTable_Object = MibTable
portChannelExtTable = _PortChannelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4)
)
if mibBuilder.loadTexts:
    portChannelExtTable.setStatus("current")
_PortChannelExtEntry_Object = MibTableRow
portChannelExtEntry = _PortChannelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    portChannelExtEntry.setStatus("current")
_PortChannelExtChannelGrpMode_Type = PortChannelGroupMode
_PortChannelExtChannelGrpMode_Object = MibTableColumn
portChannelExtChannelGrpMode = _PortChannelExtChannelGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 1),
    _PortChannelExtChannelGrpMode_Type()
)
portChannelExtChannelGrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelExtChannelGrpMode.setStatus("current")
_PortChannelExtAutoCreated_Type = TruthValue
_PortChannelExtAutoCreated_Object = MibTableColumn
portChannelExtAutoCreated = _PortChannelExtAutoCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 2),
    _PortChannelExtAutoCreated_Type()
)
portChannelExtAutoCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelExtAutoCreated.setStatus("current")


class _PortChannelExtPersistent_Type(Integer32):
    """Custom type portChannelExtPersistent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("enable", 2))
    )


_PortChannelExtPersistent_Type.__name__ = "Integer32"
_PortChannelExtPersistent_Object = MibTableColumn
portChannelExtPersistent = _PortChannelExtPersistent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 3),
    _PortChannelExtPersistent_Type()
)
portChannelExtPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelExtPersistent.setStatus("current")
_PortChannelExtOperChannelGrpMode_Type = PortChannelGroupMode
_PortChannelExtOperChannelGrpMode_Object = MibTableColumn
portChannelExtOperChannelGrpMode = _PortChannelExtOperChannelGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 4),
    _PortChannelExtOperChannelGrpMode_Type()
)
portChannelExtOperChannelGrpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelExtOperChannelGrpMode.setStatus("current")


class _PortChannelExtFcipEnhanced_Type(Integer32):
    """Custom type portChannelExtFcipEnhanced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortChannelExtFcipEnhanced_Type.__name__ = "Integer32"
_PortChannelExtFcipEnhanced_Object = MibTableColumn
portChannelExtFcipEnhanced = _PortChannelExtFcipEnhanced_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 5),
    _PortChannelExtFcipEnhanced_Type()
)
portChannelExtFcipEnhanced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelExtFcipEnhanced.setStatus("current")
_PortChannelStatistics_ObjectIdentity = ObjectIdentity
portChannelStatistics = _PortChannelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 2)
)
_PortChannelNotification_ObjectIdentity = ObjectIdentity
portChannelNotification = _PortChannelNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 3)
)
_PortChannelNotifications_ObjectIdentity = ObjectIdentity
portChannelNotifications = _PortChannelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 3, 0)
)
_PortChannelMIBConformance_ObjectIdentity = ObjectIdentity
portChannelMIBConformance = _PortChannelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2)
)
_PortChannelMIBCompliances_ObjectIdentity = ObjectIdentity
portChannelMIBCompliances = _PortChannelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1)
)
_PortChannelMIBGroups_ObjectIdentity = ObjectIdentity
portChannelMIBGroups = _PortChannelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2)
)
portChannelEntry.registerAugmentions(
    ("CISCO-PORT-CHANNEL-MIB",
     "portChannelExtEntry")
)
portChannelExtEntry.setIndexNames(*portChannelEntry.getIndexNames())

# Managed Objects groups

portChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 1)
)
portChannelGroup.setObjects(
      *(("CISCO-PORT-CHANNEL-MIB", "portChannelIfIndex"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelAdminChannelMode"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelOperChannelMode"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelAddType"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelLastActionStatus"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelLastActionStatusCause"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelLastActionTime"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelMemberList"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelCreationTime"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelRowStatus"))
)
if mibBuilder.loadTexts:
    portChannelGroup.setStatus("current")

portChannelGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 2)
)
portChannelGroupRev1.setObjects(
    ("CISCO-PORT-CHANNEL-MIB", "portChannelMemberOperStatus")
)
if mibBuilder.loadTexts:
    portChannelGroupRev1.setStatus("current")

portChannelProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 3)
)
portChannelProtocolGroup.setObjects(
      *(("CISCO-PORT-CHANNEL-MIB", "portChannelProtocolEnable"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelGrpIfAutoCreation"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelExtChannelGrpMode"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelExtAutoCreated"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelExtPersistent"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelExtOperChannelGrpMode"))
)
if mibBuilder.loadTexts:
    portChannelProtocolGroup.setStatus("current")

portChannelFcipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 4)
)
portChannelFcipGroup.setObjects(
    ("CISCO-PORT-CHANNEL-MIB", "portChannelExtFcipEnhanced")
)
if mibBuilder.loadTexts:
    portChannelFcipGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

portChannelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 1)
)
portChannelMIBCompliance.setObjects(
    ("CISCO-PORT-CHANNEL-MIB", "portChannelGroup")
)
if mibBuilder.loadTexts:
    portChannelMIBCompliance.setStatus(
        "deprecated"
    )

portChannelMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 2)
)
portChannelMIBCompliance1.setObjects(
    ("CISCO-PORT-CHANNEL-MIB", "portChannelGroup")
)
if mibBuilder.loadTexts:
    portChannelMIBCompliance1.setStatus(
        "deprecated"
    )

portChannelMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 3)
)
portChannelMIBCompliance2.setObjects(
      *(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelGroupRev1"))
)
if mibBuilder.loadTexts:
    portChannelMIBCompliance2.setStatus(
        "deprecated"
    )

portChannelMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 4)
)
portChannelMIBCompliance3.setObjects(
      *(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelGroupRev1"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelProtocolGroup"))
)
if mibBuilder.loadTexts:
    portChannelMIBCompliance3.setStatus(
        "deprecated"
    )

portChannelMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 5)
)
portChannelMIBCompliance4.setObjects(
      *(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelGroupRev1"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelProtocolGroup"),
        ("CISCO-PORT-CHANNEL-MIB", "portChannelFcipGroup"))
)
if mibBuilder.loadTexts:
    portChannelMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PORT-CHANNEL-MIB",
    **{"PortChannelMode": PortChannelMode,
       "PortChannelGroupMode": PortChannelGroupMode,
       "ciscoPortChannelMIB": ciscoPortChannelMIB,
       "ciscoPortChannelObjects": ciscoPortChannelObjects,
       "portChannelConfig": portChannelConfig,
       "portChannelTable": portChannelTable,
       "portChannelEntry": portChannelEntry,
       "portChannelIndex": portChannelIndex,
       "portChannelIfIndex": portChannelIfIndex,
       "portChannelAdminChannelMode": portChannelAdminChannelMode,
       "portChannelOperChannelMode": portChannelOperChannelMode,
       "portChannelAddType": portChannelAddType,
       "portChannelLastActionStatus": portChannelLastActionStatus,
       "portChannelLastActionStatusCause": portChannelLastActionStatusCause,
       "portChannelLastActionTime": portChannelLastActionTime,
       "portChannelMemberList": portChannelMemberList,
       "portChannelCreationTime": portChannelCreationTime,
       "portChannelRowStatus": portChannelRowStatus,
       "portChannelMemberOperStatus": portChannelMemberOperStatus,
       "portChannelProtocolEnable": portChannelProtocolEnable,
       "portChannelGrpIfExtTable": portChannelGrpIfExtTable,
       "portChannelGrpIfExtEntry": portChannelGrpIfExtEntry,
       "portChannelGrpIfAutoCreation": portChannelGrpIfAutoCreation,
       "portChannelExtTable": portChannelExtTable,
       "portChannelExtEntry": portChannelExtEntry,
       "portChannelExtChannelGrpMode": portChannelExtChannelGrpMode,
       "portChannelExtAutoCreated": portChannelExtAutoCreated,
       "portChannelExtPersistent": portChannelExtPersistent,
       "portChannelExtOperChannelGrpMode": portChannelExtOperChannelGrpMode,
       "portChannelExtFcipEnhanced": portChannelExtFcipEnhanced,
       "portChannelStatistics": portChannelStatistics,
       "portChannelNotification": portChannelNotification,
       "portChannelNotifications": portChannelNotifications,
       "portChannelMIBConformance": portChannelMIBConformance,
       "portChannelMIBCompliances": portChannelMIBCompliances,
       "portChannelMIBCompliance": portChannelMIBCompliance,
       "portChannelMIBCompliance1": portChannelMIBCompliance1,
       "portChannelMIBCompliance2": portChannelMIBCompliance2,
       "portChannelMIBCompliance3": portChannelMIBCompliance3,
       "portChannelMIBCompliance4": portChannelMIBCompliance4,
       "portChannelMIBGroups": portChannelMIBGroups,
       "portChannelGroup": portChannelGroup,
       "portChannelGroupRev1": portChannelGroupRev1,
       "portChannelProtocolGroup": portChannelProtocolGroup,
       "portChannelFcipGroup": portChannelFcipGroup}
)
