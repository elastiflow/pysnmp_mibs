# SNMP MIB module (ME1200-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-ERPS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(ME1200InterfaceIndex,
 ME1200RowEditorState,
 ME1200VlanListQuarter) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState",
    "ME1200VlanListQuarter")

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

me1200ErpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72)
)
if mibBuilder.loadTexts:
    me1200ErpsMib.setRevisions(
        ("2014-06-23 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-09 00:00",
         "2013-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200ErpsRingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 1),
          ("sub", 2))
    )



class ME1200ErpsRplMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("owner", 2),
          ("neighbour", 3))
    )



class ME1200ErpsPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 1),
          ("port1", 2))
    )



class ME1200ErpsVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class ME1200ErpsProtectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("idle", 2),
          ("protected", 3),
          ("forcedSwitch", 4),
          ("manualSwitch", 5),
          ("pending", 6))
    )



class ME1200ErpsAdminCmd(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manualSwitch", 1),
          ("forcedSwitch", 2),
          ("clear", 3))
    )



class ME1200ErpsRequestState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("manualSwitch", 2),
          ("signalFail", 3),
          ("forcedSwitch", 4),
          ("event", 5))
    )



class ME1200ErpsPortState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("signalFail", 2))
    )



class ME1200ErpsControlCmd(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("admCmdForcedSwitch", 1),
          ("admCmdManualSwitch", 2),
          ("admCmdClear", 3),
          ("statisticsClear", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200ErpsMIBObjects_ObjectIdentity = ObjectIdentity
me1200ErpsMIBObjects = _Me1200ErpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1)
)
_Me1200ErpsCapabilities_ObjectIdentity = ObjectIdentity
me1200ErpsCapabilities = _Me1200ErpsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 1)
)
_Me1200ErpsCapabilitiesMaxGroups_Type = Unsigned32
_Me1200ErpsCapabilitiesMaxGroups_Object = MibScalar
me1200ErpsCapabilitiesMaxGroups = _Me1200ErpsCapabilitiesMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 1, 1),
    _Me1200ErpsCapabilitiesMaxGroups_Type()
)
me1200ErpsCapabilitiesMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsCapabilitiesMaxGroups.setStatus("current")
_Me1200ErpsCapabilitiesMaxVlansPerGroup_Type = Unsigned32
_Me1200ErpsCapabilitiesMaxVlansPerGroup_Object = MibScalar
me1200ErpsCapabilitiesMaxVlansPerGroup = _Me1200ErpsCapabilitiesMaxVlansPerGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 1, 2),
    _Me1200ErpsCapabilitiesMaxVlansPerGroup_Type()
)
me1200ErpsCapabilitiesMaxVlansPerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsCapabilitiesMaxVlansPerGroup.setStatus("current")
_Me1200ErpsConfig_ObjectIdentity = ObjectIdentity
me1200ErpsConfig = _Me1200ErpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2)
)
_Me1200ErpsConfigTable_Object = MibTable
me1200ErpsConfigTable = _Me1200ErpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200ErpsConfigTable.setStatus("current")
_Me1200ErpsConfigEntry_Object = MibTableRow
me1200ErpsConfigEntry = _Me1200ErpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1)
)
me1200ErpsConfigEntry.setIndexNames(
    (0, "ME1200-ERPS-MIB", "me1200ErpsConfigGroupIndex"),
)
if mibBuilder.loadTexts:
    me1200ErpsConfigEntry.setStatus("current")


class _Me1200ErpsConfigGroupIndex_Type(Integer32):
    """Custom type me1200ErpsConfigGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ErpsConfigGroupIndex_Type.__name__ = "Integer32"
_Me1200ErpsConfigGroupIndex_Object = MibTableColumn
me1200ErpsConfigGroupIndex = _Me1200ErpsConfigGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 1),
    _Me1200ErpsConfigGroupIndex_Type()
)
me1200ErpsConfigGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ErpsConfigGroupIndex.setStatus("current")
_Me1200ErpsConfigRingType_Type = ME1200ErpsRingType
_Me1200ErpsConfigRingType_Object = MibTableColumn
me1200ErpsConfigRingType = _Me1200ErpsConfigRingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 2),
    _Me1200ErpsConfigRingType_Type()
)
me1200ErpsConfigRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRingType.setStatus("current")
_Me1200ErpsConfigPort0_Type = ME1200InterfaceIndex
_Me1200ErpsConfigPort0_Object = MibTableColumn
me1200ErpsConfigPort0 = _Me1200ErpsConfigPort0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 3),
    _Me1200ErpsConfigPort0_Type()
)
me1200ErpsConfigPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigPort0.setStatus("current")
_Me1200ErpsConfigPort1_Type = ME1200InterfaceIndex
_Me1200ErpsConfigPort1_Object = MibTableColumn
me1200ErpsConfigPort1 = _Me1200ErpsConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 4),
    _Me1200ErpsConfigPort1_Type()
)
me1200ErpsConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigPort1.setStatus("current")
_Me1200ErpsConfigInterconnectMajorRingGroupIndex_Type = Unsigned32
_Me1200ErpsConfigInterconnectMajorRingGroupIndex_Object = MibTableColumn
me1200ErpsConfigInterconnectMajorRingGroupIndex = _Me1200ErpsConfigInterconnectMajorRingGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 5),
    _Me1200ErpsConfigInterconnectMajorRingGroupIndex_Type()
)
me1200ErpsConfigInterconnectMajorRingGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigInterconnectMajorRingGroupIndex.setStatus("current")
_Me1200ErpsConfigVirtualChannel_Type = TruthValue
_Me1200ErpsConfigVirtualChannel_Object = MibTableColumn
me1200ErpsConfigVirtualChannel = _Me1200ErpsConfigVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 6),
    _Me1200ErpsConfigVirtualChannel_Type()
)
me1200ErpsConfigVirtualChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigVirtualChannel.setStatus("current")
_Me1200ErpsConfigPort0SignalFailMepIndex_Type = Unsigned32
_Me1200ErpsConfigPort0SignalFailMepIndex_Object = MibTableColumn
me1200ErpsConfigPort0SignalFailMepIndex = _Me1200ErpsConfigPort0SignalFailMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 7),
    _Me1200ErpsConfigPort0SignalFailMepIndex_Type()
)
me1200ErpsConfigPort0SignalFailMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigPort0SignalFailMepIndex.setStatus("current")
_Me1200ErpsConfigPort0ApsMepIndex_Type = Unsigned32
_Me1200ErpsConfigPort0ApsMepIndex_Object = MibTableColumn
me1200ErpsConfigPort0ApsMepIndex = _Me1200ErpsConfigPort0ApsMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 8),
    _Me1200ErpsConfigPort0ApsMepIndex_Type()
)
me1200ErpsConfigPort0ApsMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigPort0ApsMepIndex.setStatus("current")
_Me1200ErpsConfigPort1SignalFailMepIndex_Type = Unsigned32
_Me1200ErpsConfigPort1SignalFailMepIndex_Object = MibTableColumn
me1200ErpsConfigPort1SignalFailMepIndex = _Me1200ErpsConfigPort1SignalFailMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 9),
    _Me1200ErpsConfigPort1SignalFailMepIndex_Type()
)
me1200ErpsConfigPort1SignalFailMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigPort1SignalFailMepIndex.setStatus("current")
_Me1200ErpsConfigPort1ApsMepIndex_Type = Unsigned32
_Me1200ErpsConfigPort1ApsMepIndex_Object = MibTableColumn
me1200ErpsConfigPort1ApsMepIndex = _Me1200ErpsConfigPort1ApsMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 10),
    _Me1200ErpsConfigPort1ApsMepIndex_Type()
)
me1200ErpsConfigPort1ApsMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigPort1ApsMepIndex.setStatus("current")
_Me1200ErpsConfigHoldOffTime_Type = Unsigned32
_Me1200ErpsConfigHoldOffTime_Object = MibTableColumn
me1200ErpsConfigHoldOffTime = _Me1200ErpsConfigHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 11),
    _Me1200ErpsConfigHoldOffTime_Type()
)
me1200ErpsConfigHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigHoldOffTime.setStatus("current")
_Me1200ErpsConfigWaitToRestoreTime_Type = Unsigned32
_Me1200ErpsConfigWaitToRestoreTime_Object = MibTableColumn
me1200ErpsConfigWaitToRestoreTime = _Me1200ErpsConfigWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 12),
    _Me1200ErpsConfigWaitToRestoreTime_Type()
)
me1200ErpsConfigWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigWaitToRestoreTime.setStatus("current")
_Me1200ErpsConfigGuardTime_Type = Unsigned32
_Me1200ErpsConfigGuardTime_Object = MibTableColumn
me1200ErpsConfigGuardTime = _Me1200ErpsConfigGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 13),
    _Me1200ErpsConfigGuardTime_Type()
)
me1200ErpsConfigGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigGuardTime.setStatus("current")
_Me1200ErpsConfigRplMode_Type = ME1200ErpsRplMode
_Me1200ErpsConfigRplMode_Object = MibTableColumn
me1200ErpsConfigRplMode = _Me1200ErpsConfigRplMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 14),
    _Me1200ErpsConfigRplMode_Type()
)
me1200ErpsConfigRplMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRplMode.setStatus("current")
_Me1200ErpsConfigRplPort_Type = ME1200ErpsPort
_Me1200ErpsConfigRplPort_Object = MibTableColumn
me1200ErpsConfigRplPort = _Me1200ErpsConfigRplPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 15),
    _Me1200ErpsConfigRplPort_Type()
)
me1200ErpsConfigRplPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRplPort.setStatus("current")
_Me1200ErpsConfigRevertive_Type = TruthValue
_Me1200ErpsConfigRevertive_Object = MibTableColumn
me1200ErpsConfigRevertive = _Me1200ErpsConfigRevertive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 16),
    _Me1200ErpsConfigRevertive_Type()
)
me1200ErpsConfigRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRevertive.setStatus("current")
_Me1200ErpsConfigVersion_Type = ME1200ErpsVersion
_Me1200ErpsConfigVersion_Object = MibTableColumn
me1200ErpsConfigVersion = _Me1200ErpsConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 17),
    _Me1200ErpsConfigVersion_Type()
)
me1200ErpsConfigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigVersion.setStatus("current")
_Me1200ErpsConfigTopologyChange_Type = TruthValue
_Me1200ErpsConfigTopologyChange_Object = MibTableColumn
me1200ErpsConfigTopologyChange = _Me1200ErpsConfigTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 18),
    _Me1200ErpsConfigTopologyChange_Type()
)
me1200ErpsConfigTopologyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigTopologyChange.setStatus("current")
_Me1200ErpsConfigProtectedVlans0Kto1K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigProtectedVlans0Kto1K_Object = MibTableColumn
me1200ErpsConfigProtectedVlans0Kto1K = _Me1200ErpsConfigProtectedVlans0Kto1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 19),
    _Me1200ErpsConfigProtectedVlans0Kto1K_Type()
)
me1200ErpsConfigProtectedVlans0Kto1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigProtectedVlans0Kto1K.setStatus("current")
_Me1200ErpsConfigProtectedVlans1Kto2K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigProtectedVlans1Kto2K_Object = MibTableColumn
me1200ErpsConfigProtectedVlans1Kto2K = _Me1200ErpsConfigProtectedVlans1Kto2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 20),
    _Me1200ErpsConfigProtectedVlans1Kto2K_Type()
)
me1200ErpsConfigProtectedVlans1Kto2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigProtectedVlans1Kto2K.setStatus("current")
_Me1200ErpsConfigProtectedVlans2Kto3K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigProtectedVlans2Kto3K_Object = MibTableColumn
me1200ErpsConfigProtectedVlans2Kto3K = _Me1200ErpsConfigProtectedVlans2Kto3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 21),
    _Me1200ErpsConfigProtectedVlans2Kto3K_Type()
)
me1200ErpsConfigProtectedVlans2Kto3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigProtectedVlans2Kto3K.setStatus("current")
_Me1200ErpsConfigProtectedVlans3Kto4K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigProtectedVlans3Kto4K_Object = MibTableColumn
me1200ErpsConfigProtectedVlans3Kto4K = _Me1200ErpsConfigProtectedVlans3Kto4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 22),
    _Me1200ErpsConfigProtectedVlans3Kto4K_Type()
)
me1200ErpsConfigProtectedVlans3Kto4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigProtectedVlans3Kto4K.setStatus("current")
_Me1200ErpsConfigAction_Type = ME1200RowEditorState
_Me1200ErpsConfigAction_Object = MibTableColumn
me1200ErpsConfigAction = _Me1200ErpsConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 1, 1, 100),
    _Me1200ErpsConfigAction_Type()
)
me1200ErpsConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigAction.setStatus("current")
_Me1200ErpsConfigRowEditor_ObjectIdentity = ObjectIdentity
me1200ErpsConfigRowEditor = _Me1200ErpsConfigRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2)
)


class _Me1200ErpsConfigRowEditorGroupIndex_Type(Integer32):
    """Custom type me1200ErpsConfigRowEditorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ErpsConfigRowEditorGroupIndex_Type.__name__ = "Integer32"
_Me1200ErpsConfigRowEditorGroupIndex_Object = MibScalar
me1200ErpsConfigRowEditorGroupIndex = _Me1200ErpsConfigRowEditorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 1),
    _Me1200ErpsConfigRowEditorGroupIndex_Type()
)
me1200ErpsConfigRowEditorGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorGroupIndex.setStatus("current")
_Me1200ErpsConfigRowEditorRingType_Type = ME1200ErpsRingType
_Me1200ErpsConfigRowEditorRingType_Object = MibScalar
me1200ErpsConfigRowEditorRingType = _Me1200ErpsConfigRowEditorRingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 2),
    _Me1200ErpsConfigRowEditorRingType_Type()
)
me1200ErpsConfigRowEditorRingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorRingType.setStatus("current")
_Me1200ErpsConfigRowEditorPort0_Type = ME1200InterfaceIndex
_Me1200ErpsConfigRowEditorPort0_Object = MibScalar
me1200ErpsConfigRowEditorPort0 = _Me1200ErpsConfigRowEditorPort0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 3),
    _Me1200ErpsConfigRowEditorPort0_Type()
)
me1200ErpsConfigRowEditorPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorPort0.setStatus("current")
_Me1200ErpsConfigRowEditorPort1_Type = ME1200InterfaceIndex
_Me1200ErpsConfigRowEditorPort1_Object = MibScalar
me1200ErpsConfigRowEditorPort1 = _Me1200ErpsConfigRowEditorPort1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 4),
    _Me1200ErpsConfigRowEditorPort1_Type()
)
me1200ErpsConfigRowEditorPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorPort1.setStatus("current")
_Me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex_Type = Unsigned32
_Me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex_Object = MibScalar
me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex = _Me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 5),
    _Me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex_Type()
)
me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex.setStatus("current")
_Me1200ErpsConfigRowEditorVirtualChannel_Type = TruthValue
_Me1200ErpsConfigRowEditorVirtualChannel_Object = MibScalar
me1200ErpsConfigRowEditorVirtualChannel = _Me1200ErpsConfigRowEditorVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 6),
    _Me1200ErpsConfigRowEditorVirtualChannel_Type()
)
me1200ErpsConfigRowEditorVirtualChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorVirtualChannel.setStatus("current")
_Me1200ErpsConfigRowEditorPort0SignalFailMepIndex_Type = Unsigned32
_Me1200ErpsConfigRowEditorPort0SignalFailMepIndex_Object = MibScalar
me1200ErpsConfigRowEditorPort0SignalFailMepIndex = _Me1200ErpsConfigRowEditorPort0SignalFailMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 7),
    _Me1200ErpsConfigRowEditorPort0SignalFailMepIndex_Type()
)
me1200ErpsConfigRowEditorPort0SignalFailMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorPort0SignalFailMepIndex.setStatus("current")
_Me1200ErpsConfigRowEditorPort0ApsMepIndex_Type = Unsigned32
_Me1200ErpsConfigRowEditorPort0ApsMepIndex_Object = MibScalar
me1200ErpsConfigRowEditorPort0ApsMepIndex = _Me1200ErpsConfigRowEditorPort0ApsMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 8),
    _Me1200ErpsConfigRowEditorPort0ApsMepIndex_Type()
)
me1200ErpsConfigRowEditorPort0ApsMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorPort0ApsMepIndex.setStatus("current")
_Me1200ErpsConfigRowEditorPort1SignalFailMepIndex_Type = Unsigned32
_Me1200ErpsConfigRowEditorPort1SignalFailMepIndex_Object = MibScalar
me1200ErpsConfigRowEditorPort1SignalFailMepIndex = _Me1200ErpsConfigRowEditorPort1SignalFailMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 9),
    _Me1200ErpsConfigRowEditorPort1SignalFailMepIndex_Type()
)
me1200ErpsConfigRowEditorPort1SignalFailMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorPort1SignalFailMepIndex.setStatus("current")
_Me1200ErpsConfigRowEditorPort1ApsMepIndex_Type = Unsigned32
_Me1200ErpsConfigRowEditorPort1ApsMepIndex_Object = MibScalar
me1200ErpsConfigRowEditorPort1ApsMepIndex = _Me1200ErpsConfigRowEditorPort1ApsMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 10),
    _Me1200ErpsConfigRowEditorPort1ApsMepIndex_Type()
)
me1200ErpsConfigRowEditorPort1ApsMepIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorPort1ApsMepIndex.setStatus("current")
_Me1200ErpsConfigRowEditorHoldOffTime_Type = Unsigned32
_Me1200ErpsConfigRowEditorHoldOffTime_Object = MibScalar
me1200ErpsConfigRowEditorHoldOffTime = _Me1200ErpsConfigRowEditorHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 11),
    _Me1200ErpsConfigRowEditorHoldOffTime_Type()
)
me1200ErpsConfigRowEditorHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorHoldOffTime.setStatus("current")
_Me1200ErpsConfigRowEditorWaitToRestoreTime_Type = Unsigned32
_Me1200ErpsConfigRowEditorWaitToRestoreTime_Object = MibScalar
me1200ErpsConfigRowEditorWaitToRestoreTime = _Me1200ErpsConfigRowEditorWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 12),
    _Me1200ErpsConfigRowEditorWaitToRestoreTime_Type()
)
me1200ErpsConfigRowEditorWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorWaitToRestoreTime.setStatus("current")
_Me1200ErpsConfigRowEditorGuardTime_Type = Unsigned32
_Me1200ErpsConfigRowEditorGuardTime_Object = MibScalar
me1200ErpsConfigRowEditorGuardTime = _Me1200ErpsConfigRowEditorGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 13),
    _Me1200ErpsConfigRowEditorGuardTime_Type()
)
me1200ErpsConfigRowEditorGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorGuardTime.setStatus("current")
_Me1200ErpsConfigRowEditorRplMode_Type = ME1200ErpsRplMode
_Me1200ErpsConfigRowEditorRplMode_Object = MibScalar
me1200ErpsConfigRowEditorRplMode = _Me1200ErpsConfigRowEditorRplMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 14),
    _Me1200ErpsConfigRowEditorRplMode_Type()
)
me1200ErpsConfigRowEditorRplMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorRplMode.setStatus("current")
_Me1200ErpsConfigRowEditorRplPort_Type = ME1200ErpsPort
_Me1200ErpsConfigRowEditorRplPort_Object = MibScalar
me1200ErpsConfigRowEditorRplPort = _Me1200ErpsConfigRowEditorRplPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 15),
    _Me1200ErpsConfigRowEditorRplPort_Type()
)
me1200ErpsConfigRowEditorRplPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorRplPort.setStatus("current")
_Me1200ErpsConfigRowEditorRevertive_Type = TruthValue
_Me1200ErpsConfigRowEditorRevertive_Object = MibScalar
me1200ErpsConfigRowEditorRevertive = _Me1200ErpsConfigRowEditorRevertive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 16),
    _Me1200ErpsConfigRowEditorRevertive_Type()
)
me1200ErpsConfigRowEditorRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorRevertive.setStatus("current")
_Me1200ErpsConfigRowEditorVersion_Type = ME1200ErpsVersion
_Me1200ErpsConfigRowEditorVersion_Object = MibScalar
me1200ErpsConfigRowEditorVersion = _Me1200ErpsConfigRowEditorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 17),
    _Me1200ErpsConfigRowEditorVersion_Type()
)
me1200ErpsConfigRowEditorVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorVersion.setStatus("current")
_Me1200ErpsConfigRowEditorTopologyChange_Type = TruthValue
_Me1200ErpsConfigRowEditorTopologyChange_Object = MibScalar
me1200ErpsConfigRowEditorTopologyChange = _Me1200ErpsConfigRowEditorTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 18),
    _Me1200ErpsConfigRowEditorTopologyChange_Type()
)
me1200ErpsConfigRowEditorTopologyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorTopologyChange.setStatus("current")
_Me1200ErpsConfigRowEditorProtectedVlans0Kto1K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigRowEditorProtectedVlans0Kto1K_Object = MibScalar
me1200ErpsConfigRowEditorProtectedVlans0Kto1K = _Me1200ErpsConfigRowEditorProtectedVlans0Kto1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 19),
    _Me1200ErpsConfigRowEditorProtectedVlans0Kto1K_Type()
)
me1200ErpsConfigRowEditorProtectedVlans0Kto1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorProtectedVlans0Kto1K.setStatus("current")
_Me1200ErpsConfigRowEditorProtectedVlans1Kto2K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigRowEditorProtectedVlans1Kto2K_Object = MibScalar
me1200ErpsConfigRowEditorProtectedVlans1Kto2K = _Me1200ErpsConfigRowEditorProtectedVlans1Kto2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 20),
    _Me1200ErpsConfigRowEditorProtectedVlans1Kto2K_Type()
)
me1200ErpsConfigRowEditorProtectedVlans1Kto2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorProtectedVlans1Kto2K.setStatus("current")
_Me1200ErpsConfigRowEditorProtectedVlans2Kto3K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigRowEditorProtectedVlans2Kto3K_Object = MibScalar
me1200ErpsConfigRowEditorProtectedVlans2Kto3K = _Me1200ErpsConfigRowEditorProtectedVlans2Kto3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 21),
    _Me1200ErpsConfigRowEditorProtectedVlans2Kto3K_Type()
)
me1200ErpsConfigRowEditorProtectedVlans2Kto3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorProtectedVlans2Kto3K.setStatus("current")
_Me1200ErpsConfigRowEditorProtectedVlans3Kto4K_Type = ME1200VlanListQuarter
_Me1200ErpsConfigRowEditorProtectedVlans3Kto4K_Object = MibScalar
me1200ErpsConfigRowEditorProtectedVlans3Kto4K = _Me1200ErpsConfigRowEditorProtectedVlans3Kto4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 22),
    _Me1200ErpsConfigRowEditorProtectedVlans3Kto4K_Type()
)
me1200ErpsConfigRowEditorProtectedVlans3Kto4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorProtectedVlans3Kto4K.setStatus("current")
_Me1200ErpsConfigRowEditorAction_Type = ME1200RowEditorState
_Me1200ErpsConfigRowEditorAction_Object = MibScalar
me1200ErpsConfigRowEditorAction = _Me1200ErpsConfigRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 2, 2, 100),
    _Me1200ErpsConfigRowEditorAction_Type()
)
me1200ErpsConfigRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorAction.setStatus("current")
_Me1200ErpsStatus_ObjectIdentity = ObjectIdentity
me1200ErpsStatus = _Me1200ErpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3)
)
_Me1200ErpsStatusTable_Object = MibTable
me1200ErpsStatusTable = _Me1200ErpsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200ErpsStatusTable.setStatus("current")
_Me1200ErpsStatusEntry_Object = MibTableRow
me1200ErpsStatusEntry = _Me1200ErpsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1)
)
me1200ErpsStatusEntry.setIndexNames(
    (0, "ME1200-ERPS-MIB", "me1200ErpsStatusGroupIndex"),
)
if mibBuilder.loadTexts:
    me1200ErpsStatusEntry.setStatus("current")


class _Me1200ErpsStatusGroupIndex_Type(Integer32):
    """Custom type me1200ErpsStatusGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ErpsStatusGroupIndex_Type.__name__ = "Integer32"
_Me1200ErpsStatusGroupIndex_Object = MibTableColumn
me1200ErpsStatusGroupIndex = _Me1200ErpsStatusGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 1),
    _Me1200ErpsStatusGroupIndex_Type()
)
me1200ErpsStatusGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ErpsStatusGroupIndex.setStatus("current")
_Me1200ErpsStatusActive_Type = TruthValue
_Me1200ErpsStatusActive_Object = MibTableColumn
me1200ErpsStatusActive = _Me1200ErpsStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 2),
    _Me1200ErpsStatusActive_Type()
)
me1200ErpsStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusActive.setStatus("current")
_Me1200ErpsStatusProtectionState_Type = ME1200ErpsProtectionState
_Me1200ErpsStatusProtectionState_Object = MibTableColumn
me1200ErpsStatusProtectionState = _Me1200ErpsStatusProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 3),
    _Me1200ErpsStatusProtectionState_Type()
)
me1200ErpsStatusProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusProtectionState.setStatus("current")
_Me1200ErpsStatusRplBlocked_Type = TruthValue
_Me1200ErpsStatusRplBlocked_Object = MibTableColumn
me1200ErpsStatusRplBlocked = _Me1200ErpsStatusRplBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 4),
    _Me1200ErpsStatusRplBlocked_Type()
)
me1200ErpsStatusRplBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusRplBlocked.setStatus("current")
_Me1200ErpsStatusWtrRemaining_Type = Unsigned32
_Me1200ErpsStatusWtrRemaining_Object = MibTableColumn
me1200ErpsStatusWtrRemaining = _Me1200ErpsStatusWtrRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 5),
    _Me1200ErpsStatusWtrRemaining_Type()
)
me1200ErpsStatusWtrRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusWtrRemaining.setStatus("current")
_Me1200ErpsStatusAdminCmd_Type = ME1200ErpsAdminCmd
_Me1200ErpsStatusAdminCmd_Object = MibTableColumn
me1200ErpsStatusAdminCmd = _Me1200ErpsStatusAdminCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 6),
    _Me1200ErpsStatusAdminCmd_Type()
)
me1200ErpsStatusAdminCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusAdminCmd.setStatus("current")
_Me1200ErpsStatusFopAlarm_Type = TruthValue
_Me1200ErpsStatusFopAlarm_Object = MibTableColumn
me1200ErpsStatusFopAlarm = _Me1200ErpsStatusFopAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 7),
    _Me1200ErpsStatusFopAlarm_Type()
)
me1200ErpsStatusFopAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusFopAlarm.setStatus("current")
_Me1200ErpsStatusTxActive_Type = TruthValue
_Me1200ErpsStatusTxActive_Object = MibTableColumn
me1200ErpsStatusTxActive = _Me1200ErpsStatusTxActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 8),
    _Me1200ErpsStatusTxActive_Type()
)
me1200ErpsStatusTxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusTxActive.setStatus("current")
_Me1200ErpsStatusTxRequestOrState_Type = ME1200ErpsRequestState
_Me1200ErpsStatusTxRequestOrState_Object = MibTableColumn
me1200ErpsStatusTxRequestOrState = _Me1200ErpsStatusTxRequestOrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 9),
    _Me1200ErpsStatusTxRequestOrState_Type()
)
me1200ErpsStatusTxRequestOrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusTxRequestOrState.setStatus("current")
_Me1200ErpsStatusTxRplBlocked_Type = TruthValue
_Me1200ErpsStatusTxRplBlocked_Object = MibTableColumn
me1200ErpsStatusTxRplBlocked = _Me1200ErpsStatusTxRplBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 10),
    _Me1200ErpsStatusTxRplBlocked_Type()
)
me1200ErpsStatusTxRplBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusTxRplBlocked.setStatus("current")
_Me1200ErpsStatusTxDoNotFlush_Type = TruthValue
_Me1200ErpsStatusTxDoNotFlush_Object = MibTableColumn
me1200ErpsStatusTxDoNotFlush = _Me1200ErpsStatusTxDoNotFlush_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 11),
    _Me1200ErpsStatusTxDoNotFlush_Type()
)
me1200ErpsStatusTxDoNotFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusTxDoNotFlush.setStatus("current")
_Me1200ErpsStatusBlockedPortReference_Type = ME1200ErpsPort
_Me1200ErpsStatusBlockedPortReference_Object = MibTableColumn
me1200ErpsStatusBlockedPortReference = _Me1200ErpsStatusBlockedPortReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 12),
    _Me1200ErpsStatusBlockedPortReference_Type()
)
me1200ErpsStatusBlockedPortReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusBlockedPortReference.setStatus("current")
_Me1200ErpsStatusPort0Blocked_Type = TruthValue
_Me1200ErpsStatusPort0Blocked_Object = MibTableColumn
me1200ErpsStatusPort0Blocked = _Me1200ErpsStatusPort0Blocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 13),
    _Me1200ErpsStatusPort0Blocked_Type()
)
me1200ErpsStatusPort0Blocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0Blocked.setStatus("current")
_Me1200ErpsStatusPort0State_Type = ME1200ErpsPortState
_Me1200ErpsStatusPort0State_Object = MibTableColumn
me1200ErpsStatusPort0State = _Me1200ErpsStatusPort0State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 14),
    _Me1200ErpsStatusPort0State_Type()
)
me1200ErpsStatusPort0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0State.setStatus("current")
_Me1200ErpsStatusPort0RxActive_Type = TruthValue
_Me1200ErpsStatusPort0RxActive_Object = MibTableColumn
me1200ErpsStatusPort0RxActive = _Me1200ErpsStatusPort0RxActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 15),
    _Me1200ErpsStatusPort0RxActive_Type()
)
me1200ErpsStatusPort0RxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0RxActive.setStatus("current")
_Me1200ErpsStatusPort0RxRequestOrState_Type = ME1200ErpsRequestState
_Me1200ErpsStatusPort0RxRequestOrState_Object = MibTableColumn
me1200ErpsStatusPort0RxRequestOrState = _Me1200ErpsStatusPort0RxRequestOrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 16),
    _Me1200ErpsStatusPort0RxRequestOrState_Type()
)
me1200ErpsStatusPort0RxRequestOrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0RxRequestOrState.setStatus("current")
_Me1200ErpsStatusPort0RxRplBlocked_Type = TruthValue
_Me1200ErpsStatusPort0RxRplBlocked_Object = MibTableColumn
me1200ErpsStatusPort0RxRplBlocked = _Me1200ErpsStatusPort0RxRplBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 17),
    _Me1200ErpsStatusPort0RxRplBlocked_Type()
)
me1200ErpsStatusPort0RxRplBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0RxRplBlocked.setStatus("current")
_Me1200ErpsStatusPort0RxDoNotFlush_Type = TruthValue
_Me1200ErpsStatusPort0RxDoNotFlush_Object = MibTableColumn
me1200ErpsStatusPort0RxDoNotFlush = _Me1200ErpsStatusPort0RxDoNotFlush_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 18),
    _Me1200ErpsStatusPort0RxDoNotFlush_Type()
)
me1200ErpsStatusPort0RxDoNotFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0RxDoNotFlush.setStatus("current")
_Me1200ErpsStatusPort0RxBlockedPortReference_Type = ME1200ErpsPort
_Me1200ErpsStatusPort0RxBlockedPortReference_Object = MibTableColumn
me1200ErpsStatusPort0RxBlockedPortReference = _Me1200ErpsStatusPort0RxBlockedPortReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 19),
    _Me1200ErpsStatusPort0RxBlockedPortReference_Type()
)
me1200ErpsStatusPort0RxBlockedPortReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0RxBlockedPortReference.setStatus("current")


class _Me1200ErpsStatusPort0RxNodeId_Type(OctetString):
    """Custom type me1200ErpsStatusPort0RxNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_Me1200ErpsStatusPort0RxNodeId_Type.__name__ = "OctetString"
_Me1200ErpsStatusPort0RxNodeId_Object = MibTableColumn
me1200ErpsStatusPort0RxNodeId = _Me1200ErpsStatusPort0RxNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 20),
    _Me1200ErpsStatusPort0RxNodeId_Type()
)
me1200ErpsStatusPort0RxNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort0RxNodeId.setStatus("current")
_Me1200ErpsStatusPort1Blocked_Type = TruthValue
_Me1200ErpsStatusPort1Blocked_Object = MibTableColumn
me1200ErpsStatusPort1Blocked = _Me1200ErpsStatusPort1Blocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 21),
    _Me1200ErpsStatusPort1Blocked_Type()
)
me1200ErpsStatusPort1Blocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1Blocked.setStatus("current")
_Me1200ErpsStatusPort1State_Type = ME1200ErpsPortState
_Me1200ErpsStatusPort1State_Object = MibTableColumn
me1200ErpsStatusPort1State = _Me1200ErpsStatusPort1State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 22),
    _Me1200ErpsStatusPort1State_Type()
)
me1200ErpsStatusPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1State.setStatus("current")
_Me1200ErpsStatusPort1RxActive_Type = TruthValue
_Me1200ErpsStatusPort1RxActive_Object = MibTableColumn
me1200ErpsStatusPort1RxActive = _Me1200ErpsStatusPort1RxActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 23),
    _Me1200ErpsStatusPort1RxActive_Type()
)
me1200ErpsStatusPort1RxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1RxActive.setStatus("current")
_Me1200ErpsStatusPort1RxRequestOrState_Type = ME1200ErpsRequestState
_Me1200ErpsStatusPort1RxRequestOrState_Object = MibTableColumn
me1200ErpsStatusPort1RxRequestOrState = _Me1200ErpsStatusPort1RxRequestOrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 24),
    _Me1200ErpsStatusPort1RxRequestOrState_Type()
)
me1200ErpsStatusPort1RxRequestOrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1RxRequestOrState.setStatus("current")
_Me1200ErpsStatusPort1RxRplBlocked_Type = TruthValue
_Me1200ErpsStatusPort1RxRplBlocked_Object = MibTableColumn
me1200ErpsStatusPort1RxRplBlocked = _Me1200ErpsStatusPort1RxRplBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 25),
    _Me1200ErpsStatusPort1RxRplBlocked_Type()
)
me1200ErpsStatusPort1RxRplBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1RxRplBlocked.setStatus("current")
_Me1200ErpsStatusPort1RxDoNotFlush_Type = TruthValue
_Me1200ErpsStatusPort1RxDoNotFlush_Object = MibTableColumn
me1200ErpsStatusPort1RxDoNotFlush = _Me1200ErpsStatusPort1RxDoNotFlush_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 26),
    _Me1200ErpsStatusPort1RxDoNotFlush_Type()
)
me1200ErpsStatusPort1RxDoNotFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1RxDoNotFlush.setStatus("current")
_Me1200ErpsStatusPort1RxBlockedPortReference_Type = ME1200ErpsPort
_Me1200ErpsStatusPort1RxBlockedPortReference_Object = MibTableColumn
me1200ErpsStatusPort1RxBlockedPortReference = _Me1200ErpsStatusPort1RxBlockedPortReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 27),
    _Me1200ErpsStatusPort1RxBlockedPortReference_Type()
)
me1200ErpsStatusPort1RxBlockedPortReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1RxBlockedPortReference.setStatus("current")


class _Me1200ErpsStatusPort1RxNodeId_Type(OctetString):
    """Custom type me1200ErpsStatusPort1RxNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_Me1200ErpsStatusPort1RxNodeId_Type.__name__ = "OctetString"
_Me1200ErpsStatusPort1RxNodeId_Object = MibTableColumn
me1200ErpsStatusPort1RxNodeId = _Me1200ErpsStatusPort1RxNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 3, 1, 1, 28),
    _Me1200ErpsStatusPort1RxNodeId_Type()
)
me1200ErpsStatusPort1RxNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatusPort1RxNodeId.setStatus("current")
_Me1200ErpsStatistics_ObjectIdentity = ObjectIdentity
me1200ErpsStatistics = _Me1200ErpsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4)
)
_Me1200ErpsStatisticsTable_Object = MibTable
me1200ErpsStatisticsTable = _Me1200ErpsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200ErpsStatisticsTable.setStatus("current")
_Me1200ErpsStatisticsEntry_Object = MibTableRow
me1200ErpsStatisticsEntry = _Me1200ErpsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1)
)
me1200ErpsStatisticsEntry.setIndexNames(
    (0, "ME1200-ERPS-MIB", "me1200ErpsStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    me1200ErpsStatisticsEntry.setStatus("current")


class _Me1200ErpsStatisticsGroupIndex_Type(Integer32):
    """Custom type me1200ErpsStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ErpsStatisticsGroupIndex_Type.__name__ = "Integer32"
_Me1200ErpsStatisticsGroupIndex_Object = MibTableColumn
me1200ErpsStatisticsGroupIndex = _Me1200ErpsStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 1),
    _Me1200ErpsStatisticsGroupIndex_Type()
)
me1200ErpsStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsGroupIndex.setStatus("current")
_Me1200ErpsStatisticsRapsTx_Type = Counter64
_Me1200ErpsStatisticsRapsTx_Object = MibTableColumn
me1200ErpsStatisticsRapsTx = _Me1200ErpsStatisticsRapsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 2),
    _Me1200ErpsStatisticsRapsTx_Type()
)
me1200ErpsStatisticsRapsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsRapsTx.setStatus("current")
_Me1200ErpsStatisticsRapsRx_Type = Counter64
_Me1200ErpsStatisticsRapsRx_Object = MibTableColumn
me1200ErpsStatisticsRapsRx = _Me1200ErpsStatisticsRapsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 3),
    _Me1200ErpsStatisticsRapsRx_Type()
)
me1200ErpsStatisticsRapsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsRapsRx.setStatus("current")
_Me1200ErpsStatisticsRapsRxDrop_Type = Counter64
_Me1200ErpsStatisticsRapsRxDrop_Object = MibTableColumn
me1200ErpsStatisticsRapsRxDrop = _Me1200ErpsStatisticsRapsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 4),
    _Me1200ErpsStatisticsRapsRxDrop_Type()
)
me1200ErpsStatisticsRapsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsRapsRxDrop.setStatus("current")
_Me1200ErpsStatisticsLocalSF_Type = Counter64
_Me1200ErpsStatisticsLocalSF_Object = MibTableColumn
me1200ErpsStatisticsLocalSF = _Me1200ErpsStatisticsLocalSF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 5),
    _Me1200ErpsStatisticsLocalSF_Type()
)
me1200ErpsStatisticsLocalSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsLocalSF.setStatus("current")
_Me1200ErpsStatisticsLocalSFCleared_Type = Counter64
_Me1200ErpsStatisticsLocalSFCleared_Object = MibTableColumn
me1200ErpsStatisticsLocalSFCleared = _Me1200ErpsStatisticsLocalSFCleared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 6),
    _Me1200ErpsStatisticsLocalSFCleared_Type()
)
me1200ErpsStatisticsLocalSFCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsLocalSFCleared.setStatus("current")
_Me1200ErpsStatisticsRemoteSF_Type = Counter64
_Me1200ErpsStatisticsRemoteSF_Object = MibTableColumn
me1200ErpsStatisticsRemoteSF = _Me1200ErpsStatisticsRemoteSF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 7),
    _Me1200ErpsStatisticsRemoteSF_Type()
)
me1200ErpsStatisticsRemoteSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsRemoteSF.setStatus("current")
_Me1200ErpsStatisticsNR_Type = Counter64
_Me1200ErpsStatisticsNR_Object = MibTableColumn
me1200ErpsStatisticsNR = _Me1200ErpsStatisticsNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 8),
    _Me1200ErpsStatisticsNR_Type()
)
me1200ErpsStatisticsNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsNR.setStatus("current")
_Me1200ErpsStatisticsRemoteMS_Type = Counter64
_Me1200ErpsStatisticsRemoteMS_Object = MibTableColumn
me1200ErpsStatisticsRemoteMS = _Me1200ErpsStatisticsRemoteMS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 9),
    _Me1200ErpsStatisticsRemoteMS_Type()
)
me1200ErpsStatisticsRemoteMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsRemoteMS.setStatus("current")
_Me1200ErpsStatisticsLocalMS_Type = Counter64
_Me1200ErpsStatisticsLocalMS_Object = MibTableColumn
me1200ErpsStatisticsLocalMS = _Me1200ErpsStatisticsLocalMS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 10),
    _Me1200ErpsStatisticsLocalMS_Type()
)
me1200ErpsStatisticsLocalMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsLocalMS.setStatus("current")
_Me1200ErpsStatisticsRemoteFS_Type = Counter64
_Me1200ErpsStatisticsRemoteFS_Object = MibTableColumn
me1200ErpsStatisticsRemoteFS = _Me1200ErpsStatisticsRemoteFS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 11),
    _Me1200ErpsStatisticsRemoteFS_Type()
)
me1200ErpsStatisticsRemoteFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsRemoteFS.setStatus("current")
_Me1200ErpsStatisticsLocalFS_Type = Counter64
_Me1200ErpsStatisticsLocalFS_Object = MibTableColumn
me1200ErpsStatisticsLocalFS = _Me1200ErpsStatisticsLocalFS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 12),
    _Me1200ErpsStatisticsLocalFS_Type()
)
me1200ErpsStatisticsLocalFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsLocalFS.setStatus("current")
_Me1200ErpsStatisticsAdminClear_Type = Counter64
_Me1200ErpsStatisticsAdminClear_Object = MibTableColumn
me1200ErpsStatisticsAdminClear = _Me1200ErpsStatisticsAdminClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 4, 1, 1, 13),
    _Me1200ErpsStatisticsAdminClear_Type()
)
me1200ErpsStatisticsAdminClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200ErpsStatisticsAdminClear.setStatus("current")
_Me1200ErpsControl_ObjectIdentity = ObjectIdentity
me1200ErpsControl = _Me1200ErpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 5)
)
_Me1200ErpsControlTable_Object = MibTable
me1200ErpsControlTable = _Me1200ErpsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    me1200ErpsControlTable.setStatus("current")
_Me1200ErpsControlEntry_Object = MibTableRow
me1200ErpsControlEntry = _Me1200ErpsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 5, 1, 1)
)
me1200ErpsControlEntry.setIndexNames(
    (0, "ME1200-ERPS-MIB", "me1200ErpsControlGroupIndex"),
)
if mibBuilder.loadTexts:
    me1200ErpsControlEntry.setStatus("current")


class _Me1200ErpsControlGroupIndex_Type(Integer32):
    """Custom type me1200ErpsControlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ErpsControlGroupIndex_Type.__name__ = "Integer32"
_Me1200ErpsControlGroupIndex_Object = MibTableColumn
me1200ErpsControlGroupIndex = _Me1200ErpsControlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 5, 1, 1, 1),
    _Me1200ErpsControlGroupIndex_Type()
)
me1200ErpsControlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ErpsControlGroupIndex.setStatus("current")
_Me1200ErpsControlCommand_Type = ME1200ErpsControlCmd
_Me1200ErpsControlCommand_Object = MibTableColumn
me1200ErpsControlCommand = _Me1200ErpsControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 5, 1, 1, 2),
    _Me1200ErpsControlCommand_Type()
)
me1200ErpsControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsControlCommand.setStatus("current")
_Me1200ErpsControlPort_Type = ME1200ErpsPort
_Me1200ErpsControlPort_Object = MibTableColumn
me1200ErpsControlPort = _Me1200ErpsControlPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 1, 5, 1, 1, 3),
    _Me1200ErpsControlPort_Type()
)
me1200ErpsControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ErpsControlPort.setStatus("current")
_Me1200ErpsMIBConformance_ObjectIdentity = ObjectIdentity
me1200ErpsMIBConformance = _Me1200ErpsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2)
)
_Me1200ErpsMIBCompliances_ObjectIdentity = ObjectIdentity
me1200ErpsMIBCompliances = _Me1200ErpsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 1)
)
_Me1200ErpsMIBGroups_ObjectIdentity = ObjectIdentity
me1200ErpsMIBGroups = _Me1200ErpsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2)
)

# Managed Objects groups

me1200ErpsCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2, 1)
)
me1200ErpsCapabilitiesInfoGroup.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsCapabilitiesMaxGroups"),
        ("ME1200-ERPS-MIB", "me1200ErpsCapabilitiesMaxVlansPerGroup"))
)
if mibBuilder.loadTexts:
    me1200ErpsCapabilitiesInfoGroup.setStatus("current")

me1200ErpsConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2, 2)
)
me1200ErpsConfigTableInfoGroup.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsConfigRingType"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigPort0"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigPort1"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigInterconnectMajorRingGroupIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigVirtualChannel"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigPort0SignalFailMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigPort0ApsMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigPort1SignalFailMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigPort1ApsMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigHoldOffTime"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigWaitToRestoreTime"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigGuardTime"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRplMode"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRplPort"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRevertive"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigVersion"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigTopologyChange"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigProtectedVlans0Kto1K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigProtectedVlans1Kto2K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigProtectedVlans2Kto3K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigProtectedVlans3Kto4K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigAction"))
)
if mibBuilder.loadTexts:
    me1200ErpsConfigTableInfoGroup.setStatus("current")

me1200ErpsConfigRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2, 3)
)
me1200ErpsConfigRowEditorInfoGroup.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorGroupIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorRingType"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorPort0"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorPort1"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorVirtualChannel"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorPort0SignalFailMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorPort0ApsMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorPort1SignalFailMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorPort1ApsMepIndex"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorHoldOffTime"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorWaitToRestoreTime"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorGuardTime"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorRplMode"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorRplPort"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorRevertive"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorVersion"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorTopologyChange"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorProtectedVlans0Kto1K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorProtectedVlans1Kto2K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorProtectedVlans2Kto3K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorProtectedVlans3Kto4K"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200ErpsConfigRowEditorInfoGroup.setStatus("current")

me1200ErpsStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2, 4)
)
me1200ErpsStatusTableInfoGroup.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsStatusActive"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusProtectionState"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusRplBlocked"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusWtrRemaining"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusAdminCmd"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusFopAlarm"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusTxActive"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusTxRequestOrState"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusTxRplBlocked"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusTxDoNotFlush"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusBlockedPortReference"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0Blocked"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0State"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0RxActive"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0RxRequestOrState"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0RxRplBlocked"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0RxDoNotFlush"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0RxBlockedPortReference"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort0RxNodeId"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1Blocked"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1State"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1RxActive"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1RxRequestOrState"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1RxRplBlocked"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1RxDoNotFlush"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1RxBlockedPortReference"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusPort1RxNodeId"))
)
if mibBuilder.loadTexts:
    me1200ErpsStatusTableInfoGroup.setStatus("current")

me1200ErpsStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2, 5)
)
me1200ErpsStatisticsTableInfoGroup.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsStatisticsRapsTx"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsRapsRx"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsRapsRxDrop"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsLocalSF"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsLocalSFCleared"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsRemoteSF"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsNR"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsRemoteMS"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsLocalMS"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsRemoteFS"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsLocalFS"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsAdminClear"))
)
if mibBuilder.loadTexts:
    me1200ErpsStatisticsTableInfoGroup.setStatus("current")

me1200ErpsControlTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 2, 6)
)
me1200ErpsControlTableInfoGroup.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsControlCommand"),
        ("ME1200-ERPS-MIB", "me1200ErpsControlPort"))
)
if mibBuilder.loadTexts:
    me1200ErpsControlTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200ErpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 72, 2, 1, 1)
)
me1200ErpsMibCompliance.setObjects(
      *(("ME1200-ERPS-MIB", "me1200ErpsCapabilitiesInfoGroup"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigTableInfoGroup"),
        ("ME1200-ERPS-MIB", "me1200ErpsConfigRowEditorInfoGroup"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatusTableInfoGroup"),
        ("ME1200-ERPS-MIB", "me1200ErpsStatisticsTableInfoGroup"),
        ("ME1200-ERPS-MIB", "me1200ErpsControlTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200ErpsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-ERPS-MIB",
    **{"ME1200ErpsRingType": ME1200ErpsRingType,
       "ME1200ErpsRplMode": ME1200ErpsRplMode,
       "ME1200ErpsPort": ME1200ErpsPort,
       "ME1200ErpsVersion": ME1200ErpsVersion,
       "ME1200ErpsProtectionState": ME1200ErpsProtectionState,
       "ME1200ErpsAdminCmd": ME1200ErpsAdminCmd,
       "ME1200ErpsRequestState": ME1200ErpsRequestState,
       "ME1200ErpsPortState": ME1200ErpsPortState,
       "ME1200ErpsControlCmd": ME1200ErpsControlCmd,
       "me1200ErpsMib": me1200ErpsMib,
       "me1200ErpsMIBObjects": me1200ErpsMIBObjects,
       "me1200ErpsCapabilities": me1200ErpsCapabilities,
       "me1200ErpsCapabilitiesMaxGroups": me1200ErpsCapabilitiesMaxGroups,
       "me1200ErpsCapabilitiesMaxVlansPerGroup": me1200ErpsCapabilitiesMaxVlansPerGroup,
       "me1200ErpsConfig": me1200ErpsConfig,
       "me1200ErpsConfigTable": me1200ErpsConfigTable,
       "me1200ErpsConfigEntry": me1200ErpsConfigEntry,
       "me1200ErpsConfigGroupIndex": me1200ErpsConfigGroupIndex,
       "me1200ErpsConfigRingType": me1200ErpsConfigRingType,
       "me1200ErpsConfigPort0": me1200ErpsConfigPort0,
       "me1200ErpsConfigPort1": me1200ErpsConfigPort1,
       "me1200ErpsConfigInterconnectMajorRingGroupIndex": me1200ErpsConfigInterconnectMajorRingGroupIndex,
       "me1200ErpsConfigVirtualChannel": me1200ErpsConfigVirtualChannel,
       "me1200ErpsConfigPort0SignalFailMepIndex": me1200ErpsConfigPort0SignalFailMepIndex,
       "me1200ErpsConfigPort0ApsMepIndex": me1200ErpsConfigPort0ApsMepIndex,
       "me1200ErpsConfigPort1SignalFailMepIndex": me1200ErpsConfigPort1SignalFailMepIndex,
       "me1200ErpsConfigPort1ApsMepIndex": me1200ErpsConfigPort1ApsMepIndex,
       "me1200ErpsConfigHoldOffTime": me1200ErpsConfigHoldOffTime,
       "me1200ErpsConfigWaitToRestoreTime": me1200ErpsConfigWaitToRestoreTime,
       "me1200ErpsConfigGuardTime": me1200ErpsConfigGuardTime,
       "me1200ErpsConfigRplMode": me1200ErpsConfigRplMode,
       "me1200ErpsConfigRplPort": me1200ErpsConfigRplPort,
       "me1200ErpsConfigRevertive": me1200ErpsConfigRevertive,
       "me1200ErpsConfigVersion": me1200ErpsConfigVersion,
       "me1200ErpsConfigTopologyChange": me1200ErpsConfigTopologyChange,
       "me1200ErpsConfigProtectedVlans0Kto1K": me1200ErpsConfigProtectedVlans0Kto1K,
       "me1200ErpsConfigProtectedVlans1Kto2K": me1200ErpsConfigProtectedVlans1Kto2K,
       "me1200ErpsConfigProtectedVlans2Kto3K": me1200ErpsConfigProtectedVlans2Kto3K,
       "me1200ErpsConfigProtectedVlans3Kto4K": me1200ErpsConfigProtectedVlans3Kto4K,
       "me1200ErpsConfigAction": me1200ErpsConfigAction,
       "me1200ErpsConfigRowEditor": me1200ErpsConfigRowEditor,
       "me1200ErpsConfigRowEditorGroupIndex": me1200ErpsConfigRowEditorGroupIndex,
       "me1200ErpsConfigRowEditorRingType": me1200ErpsConfigRowEditorRingType,
       "me1200ErpsConfigRowEditorPort0": me1200ErpsConfigRowEditorPort0,
       "me1200ErpsConfigRowEditorPort1": me1200ErpsConfigRowEditorPort1,
       "me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex": me1200ErpsConfigRowEditorInterconnectMajorRingGroupIndex,
       "me1200ErpsConfigRowEditorVirtualChannel": me1200ErpsConfigRowEditorVirtualChannel,
       "me1200ErpsConfigRowEditorPort0SignalFailMepIndex": me1200ErpsConfigRowEditorPort0SignalFailMepIndex,
       "me1200ErpsConfigRowEditorPort0ApsMepIndex": me1200ErpsConfigRowEditorPort0ApsMepIndex,
       "me1200ErpsConfigRowEditorPort1SignalFailMepIndex": me1200ErpsConfigRowEditorPort1SignalFailMepIndex,
       "me1200ErpsConfigRowEditorPort1ApsMepIndex": me1200ErpsConfigRowEditorPort1ApsMepIndex,
       "me1200ErpsConfigRowEditorHoldOffTime": me1200ErpsConfigRowEditorHoldOffTime,
       "me1200ErpsConfigRowEditorWaitToRestoreTime": me1200ErpsConfigRowEditorWaitToRestoreTime,
       "me1200ErpsConfigRowEditorGuardTime": me1200ErpsConfigRowEditorGuardTime,
       "me1200ErpsConfigRowEditorRplMode": me1200ErpsConfigRowEditorRplMode,
       "me1200ErpsConfigRowEditorRplPort": me1200ErpsConfigRowEditorRplPort,
       "me1200ErpsConfigRowEditorRevertive": me1200ErpsConfigRowEditorRevertive,
       "me1200ErpsConfigRowEditorVersion": me1200ErpsConfigRowEditorVersion,
       "me1200ErpsConfigRowEditorTopologyChange": me1200ErpsConfigRowEditorTopologyChange,
       "me1200ErpsConfigRowEditorProtectedVlans0Kto1K": me1200ErpsConfigRowEditorProtectedVlans0Kto1K,
       "me1200ErpsConfigRowEditorProtectedVlans1Kto2K": me1200ErpsConfigRowEditorProtectedVlans1Kto2K,
       "me1200ErpsConfigRowEditorProtectedVlans2Kto3K": me1200ErpsConfigRowEditorProtectedVlans2Kto3K,
       "me1200ErpsConfigRowEditorProtectedVlans3Kto4K": me1200ErpsConfigRowEditorProtectedVlans3Kto4K,
       "me1200ErpsConfigRowEditorAction": me1200ErpsConfigRowEditorAction,
       "me1200ErpsStatus": me1200ErpsStatus,
       "me1200ErpsStatusTable": me1200ErpsStatusTable,
       "me1200ErpsStatusEntry": me1200ErpsStatusEntry,
       "me1200ErpsStatusGroupIndex": me1200ErpsStatusGroupIndex,
       "me1200ErpsStatusActive": me1200ErpsStatusActive,
       "me1200ErpsStatusProtectionState": me1200ErpsStatusProtectionState,
       "me1200ErpsStatusRplBlocked": me1200ErpsStatusRplBlocked,
       "me1200ErpsStatusWtrRemaining": me1200ErpsStatusWtrRemaining,
       "me1200ErpsStatusAdminCmd": me1200ErpsStatusAdminCmd,
       "me1200ErpsStatusFopAlarm": me1200ErpsStatusFopAlarm,
       "me1200ErpsStatusTxActive": me1200ErpsStatusTxActive,
       "me1200ErpsStatusTxRequestOrState": me1200ErpsStatusTxRequestOrState,
       "me1200ErpsStatusTxRplBlocked": me1200ErpsStatusTxRplBlocked,
       "me1200ErpsStatusTxDoNotFlush": me1200ErpsStatusTxDoNotFlush,
       "me1200ErpsStatusBlockedPortReference": me1200ErpsStatusBlockedPortReference,
       "me1200ErpsStatusPort0Blocked": me1200ErpsStatusPort0Blocked,
       "me1200ErpsStatusPort0State": me1200ErpsStatusPort0State,
       "me1200ErpsStatusPort0RxActive": me1200ErpsStatusPort0RxActive,
       "me1200ErpsStatusPort0RxRequestOrState": me1200ErpsStatusPort0RxRequestOrState,
       "me1200ErpsStatusPort0RxRplBlocked": me1200ErpsStatusPort0RxRplBlocked,
       "me1200ErpsStatusPort0RxDoNotFlush": me1200ErpsStatusPort0RxDoNotFlush,
       "me1200ErpsStatusPort0RxBlockedPortReference": me1200ErpsStatusPort0RxBlockedPortReference,
       "me1200ErpsStatusPort0RxNodeId": me1200ErpsStatusPort0RxNodeId,
       "me1200ErpsStatusPort1Blocked": me1200ErpsStatusPort1Blocked,
       "me1200ErpsStatusPort1State": me1200ErpsStatusPort1State,
       "me1200ErpsStatusPort1RxActive": me1200ErpsStatusPort1RxActive,
       "me1200ErpsStatusPort1RxRequestOrState": me1200ErpsStatusPort1RxRequestOrState,
       "me1200ErpsStatusPort1RxRplBlocked": me1200ErpsStatusPort1RxRplBlocked,
       "me1200ErpsStatusPort1RxDoNotFlush": me1200ErpsStatusPort1RxDoNotFlush,
       "me1200ErpsStatusPort1RxBlockedPortReference": me1200ErpsStatusPort1RxBlockedPortReference,
       "me1200ErpsStatusPort1RxNodeId": me1200ErpsStatusPort1RxNodeId,
       "me1200ErpsStatistics": me1200ErpsStatistics,
       "me1200ErpsStatisticsTable": me1200ErpsStatisticsTable,
       "me1200ErpsStatisticsEntry": me1200ErpsStatisticsEntry,
       "me1200ErpsStatisticsGroupIndex": me1200ErpsStatisticsGroupIndex,
       "me1200ErpsStatisticsRapsTx": me1200ErpsStatisticsRapsTx,
       "me1200ErpsStatisticsRapsRx": me1200ErpsStatisticsRapsRx,
       "me1200ErpsStatisticsRapsRxDrop": me1200ErpsStatisticsRapsRxDrop,
       "me1200ErpsStatisticsLocalSF": me1200ErpsStatisticsLocalSF,
       "me1200ErpsStatisticsLocalSFCleared": me1200ErpsStatisticsLocalSFCleared,
       "me1200ErpsStatisticsRemoteSF": me1200ErpsStatisticsRemoteSF,
       "me1200ErpsStatisticsNR": me1200ErpsStatisticsNR,
       "me1200ErpsStatisticsRemoteMS": me1200ErpsStatisticsRemoteMS,
       "me1200ErpsStatisticsLocalMS": me1200ErpsStatisticsLocalMS,
       "me1200ErpsStatisticsRemoteFS": me1200ErpsStatisticsRemoteFS,
       "me1200ErpsStatisticsLocalFS": me1200ErpsStatisticsLocalFS,
       "me1200ErpsStatisticsAdminClear": me1200ErpsStatisticsAdminClear,
       "me1200ErpsControl": me1200ErpsControl,
       "me1200ErpsControlTable": me1200ErpsControlTable,
       "me1200ErpsControlEntry": me1200ErpsControlEntry,
       "me1200ErpsControlGroupIndex": me1200ErpsControlGroupIndex,
       "me1200ErpsControlCommand": me1200ErpsControlCommand,
       "me1200ErpsControlPort": me1200ErpsControlPort,
       "me1200ErpsMIBConformance": me1200ErpsMIBConformance,
       "me1200ErpsMIBCompliances": me1200ErpsMIBCompliances,
       "me1200ErpsMibCompliance": me1200ErpsMibCompliance,
       "me1200ErpsMIBGroups": me1200ErpsMIBGroups,
       "me1200ErpsCapabilitiesInfoGroup": me1200ErpsCapabilitiesInfoGroup,
       "me1200ErpsConfigTableInfoGroup": me1200ErpsConfigTableInfoGroup,
       "me1200ErpsConfigRowEditorInfoGroup": me1200ErpsConfigRowEditorInfoGroup,
       "me1200ErpsStatusTableInfoGroup": me1200ErpsStatusTableInfoGroup,
       "me1200ErpsStatisticsTableInfoGroup": me1200ErpsStatisticsTableInfoGroup,
       "me1200ErpsControlTableInfoGroup": me1200ErpsControlTableInfoGroup}
)
