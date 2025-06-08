# SNMP MIB module (ME1200-SYNCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-SYNCE-MIB.mib
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

(ME1200InterfaceIndex,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200Unsigned8")

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

me1200SynceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42)
)
if mibBuilder.loadTexts:
    me1200SynceMib.setRevisions(
        ("2016-05-09 00:00",
         "2014-06-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200synceAnegMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("preferedSlave", 1),
          ("preferedMaster", 2),
          ("forcedSlave", 3))
    )



class ME1200synceEecOption(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eecOption1", 0),
          ("eecOption2", 1))
    )



class ME1200synceFrequency(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("freq1544kHz", 1),
          ("freq2048kHz", 2),
          ("freq10MHz", 3),
          ("freqMax", 4))
    )



class ME1200syncePtsfState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unusable", 1),
          ("lossSync", 2),
          ("lossAnnounce", 3))
    )



class ME1200synceQualityLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("qlNone", 0),
          ("qlPrc", 1),
          ("qlSsua", 2),
          ("qlSsub", 3),
          ("qlEec2", 4),
          ("qlEec1", 5),
          ("qlDnu", 6),
          ("qlInv", 7),
          ("qlFail", 8),
          ("qlLink", 9))
    )



class ME1200synceSelectionMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("manualToSelected", 1),
          ("autoNonrevertive", 2),
          ("autoRevertive", 3),
          ("forcedHoldover", 4),
          ("forcedFreeRun", 5))
    )



class ME1200synceSelectorState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("holdover", 1),
          ("freerun", 2),
          ("ptp", 3),
          ("refFailed", 4),
          ("acquiring", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200SynceMibObjects_ObjectIdentity = ObjectIdentity
me1200SynceMibObjects = _Me1200SynceMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1)
)
_Me1200SynceCapabilities_ObjectIdentity = ObjectIdentity
me1200SynceCapabilities = _Me1200SynceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 1)
)
_Me1200SynceCapabilitiesGlobal_ObjectIdentity = ObjectIdentity
me1200SynceCapabilitiesGlobal = _Me1200SynceCapabilitiesGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 1, 1)
)
_Me1200SynceCapabilitiesGlobalSourceCount_Type = Unsigned32
_Me1200SynceCapabilitiesGlobalSourceCount_Object = MibScalar
me1200SynceCapabilitiesGlobalSourceCount = _Me1200SynceCapabilitiesGlobalSourceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 1, 1, 1),
    _Me1200SynceCapabilitiesGlobalSourceCount_Type()
)
me1200SynceCapabilitiesGlobalSourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceCapabilitiesGlobalSourceCount.setStatus("current")
_Me1200SynceConfig_ObjectIdentity = ObjectIdentity
me1200SynceConfig = _Me1200SynceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2)
)
_Me1200SynceConfigGlobal_ObjectIdentity = ObjectIdentity
me1200SynceConfigGlobal = _Me1200SynceConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1)
)
_Me1200SynceConfigGlobalClockSelectionMode_ObjectIdentity = ObjectIdentity
me1200SynceConfigGlobalClockSelectionMode = _Me1200SynceConfigGlobalClockSelectionMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1)
)
_Me1200SynceConfigGlobalClockSelectionModeSelectionMode_Type = ME1200synceSelectionMode
_Me1200SynceConfigGlobalClockSelectionModeSelectionMode_Object = MibScalar
me1200SynceConfigGlobalClockSelectionModeSelectionMode = _Me1200SynceConfigGlobalClockSelectionModeSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1, 1),
    _Me1200SynceConfigGlobalClockSelectionModeSelectionMode_Type()
)
me1200SynceConfigGlobalClockSelectionModeSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeSelectionMode.setStatus("current")
_Me1200SynceConfigGlobalClockSelectionModeSource_Type = Unsigned32
_Me1200SynceConfigGlobalClockSelectionModeSource_Object = MibScalar
me1200SynceConfigGlobalClockSelectionModeSource = _Me1200SynceConfigGlobalClockSelectionModeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1, 2),
    _Me1200SynceConfigGlobalClockSelectionModeSource_Type()
)
me1200SynceConfigGlobalClockSelectionModeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeSource.setStatus("current")
_Me1200SynceConfigGlobalClockSelectionModeWtrTime_Type = Unsigned32
_Me1200SynceConfigGlobalClockSelectionModeWtrTime_Object = MibScalar
me1200SynceConfigGlobalClockSelectionModeWtrTime = _Me1200SynceConfigGlobalClockSelectionModeWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1, 3),
    _Me1200SynceConfigGlobalClockSelectionModeWtrTime_Type()
)
me1200SynceConfigGlobalClockSelectionModeWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeWtrTime.setStatus("current")
_Me1200SynceConfigGlobalClockSelectionModeSsmHoldover_Type = ME1200synceQualityLevel
_Me1200SynceConfigGlobalClockSelectionModeSsmHoldover_Object = MibScalar
me1200SynceConfigGlobalClockSelectionModeSsmHoldover = _Me1200SynceConfigGlobalClockSelectionModeSsmHoldover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1, 4),
    _Me1200SynceConfigGlobalClockSelectionModeSsmHoldover_Type()
)
me1200SynceConfigGlobalClockSelectionModeSsmHoldover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeSsmHoldover.setStatus("current")
_Me1200SynceConfigGlobalClockSelectionModeSsmFreerun_Type = ME1200synceQualityLevel
_Me1200SynceConfigGlobalClockSelectionModeSsmFreerun_Object = MibScalar
me1200SynceConfigGlobalClockSelectionModeSsmFreerun = _Me1200SynceConfigGlobalClockSelectionModeSsmFreerun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1, 5),
    _Me1200SynceConfigGlobalClockSelectionModeSsmFreerun_Type()
)
me1200SynceConfigGlobalClockSelectionModeSsmFreerun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeSsmFreerun.setStatus("current")
_Me1200SynceConfigGlobalClockSelectionModeEecOption_Type = ME1200synceEecOption
_Me1200SynceConfigGlobalClockSelectionModeEecOption_Object = MibScalar
me1200SynceConfigGlobalClockSelectionModeEecOption = _Me1200SynceConfigGlobalClockSelectionModeEecOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 1, 6),
    _Me1200SynceConfigGlobalClockSelectionModeEecOption_Type()
)
me1200SynceConfigGlobalClockSelectionModeEecOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeEecOption.setStatus("current")
_Me1200SynceConfigGlobalStationClocks_ObjectIdentity = ObjectIdentity
me1200SynceConfigGlobalStationClocks = _Me1200SynceConfigGlobalStationClocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 2)
)
_Me1200SynceConfigGlobalStationClocksStationClkOut_Type = ME1200synceFrequency
_Me1200SynceConfigGlobalStationClocksStationClkOut_Object = MibScalar
me1200SynceConfigGlobalStationClocksStationClkOut = _Me1200SynceConfigGlobalStationClocksStationClkOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 2, 1),
    _Me1200SynceConfigGlobalStationClocksStationClkOut_Type()
)
me1200SynceConfigGlobalStationClocksStationClkOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalStationClocksStationClkOut.setStatus("current")
_Me1200SynceConfigGlobalStationClocksStationClkIn_Type = ME1200synceFrequency
_Me1200SynceConfigGlobalStationClocksStationClkIn_Object = MibScalar
me1200SynceConfigGlobalStationClocksStationClkIn = _Me1200SynceConfigGlobalStationClocksStationClkIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 1, 2, 2),
    _Me1200SynceConfigGlobalStationClocksStationClkIn_Type()
)
me1200SynceConfigGlobalStationClocksStationClkIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalStationClocksStationClkIn.setStatus("current")
_Me1200SynceConfigSources_ObjectIdentity = ObjectIdentity
me1200SynceConfigSources = _Me1200SynceConfigSources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2)
)
_Me1200SynceConfigSourcesClockSourceNominationTable_Object = MibTable
me1200SynceConfigSourcesClockSourceNominationTable = _Me1200SynceConfigSourcesClockSourceNominationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationTable.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationEntry_Object = MibTableRow
me1200SynceConfigSourcesClockSourceNominationEntry = _Me1200SynceConfigSourcesClockSourceNominationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1)
)
me1200SynceConfigSourcesClockSourceNominationEntry.setIndexNames(
    (0, "ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationSourceId"),
)
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationEntry.setStatus("current")


class _Me1200SynceConfigSourcesClockSourceNominationSourceId_Type(Integer32):
    """Custom type me1200SynceConfigSourcesClockSourceNominationSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200SynceConfigSourcesClockSourceNominationSourceId_Type.__name__ = "Integer32"
_Me1200SynceConfigSourcesClockSourceNominationSourceId_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationSourceId = _Me1200SynceConfigSourcesClockSourceNominationSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 1),
    _Me1200SynceConfigSourcesClockSourceNominationSourceId_Type()
)
me1200SynceConfigSourcesClockSourceNominationSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationSourceId.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationNominated_Type = TruthValue
_Me1200SynceConfigSourcesClockSourceNominationNominated_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationNominated = _Me1200SynceConfigSourcesClockSourceNominationNominated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 2),
    _Me1200SynceConfigSourcesClockSourceNominationNominated_Type()
)
me1200SynceConfigSourcesClockSourceNominationNominated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationNominated.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationNetworkPort_Type = ME1200InterfaceIndex
_Me1200SynceConfigSourcesClockSourceNominationNetworkPort_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationNetworkPort = _Me1200SynceConfigSourcesClockSourceNominationNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 3),
    _Me1200SynceConfigSourcesClockSourceNominationNetworkPort_Type()
)
me1200SynceConfigSourcesClockSourceNominationNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationNetworkPort.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationClkInPort_Type = ME1200Unsigned8
_Me1200SynceConfigSourcesClockSourceNominationClkInPort_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationClkInPort = _Me1200SynceConfigSourcesClockSourceNominationClkInPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 4),
    _Me1200SynceConfigSourcesClockSourceNominationClkInPort_Type()
)
me1200SynceConfigSourcesClockSourceNominationClkInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationClkInPort.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationPriority_Type = Unsigned32
_Me1200SynceConfigSourcesClockSourceNominationPriority_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationPriority = _Me1200SynceConfigSourcesClockSourceNominationPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 5),
    _Me1200SynceConfigSourcesClockSourceNominationPriority_Type()
)
me1200SynceConfigSourcesClockSourceNominationPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationPriority.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationAnegMode_Type = ME1200synceAnegMode
_Me1200SynceConfigSourcesClockSourceNominationAnegMode_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationAnegMode = _Me1200SynceConfigSourcesClockSourceNominationAnegMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 6),
    _Me1200SynceConfigSourcesClockSourceNominationAnegMode_Type()
)
me1200SynceConfigSourcesClockSourceNominationAnegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationAnegMode.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationSsmOverwrite_Type = ME1200synceQualityLevel
_Me1200SynceConfigSourcesClockSourceNominationSsmOverwrite_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationSsmOverwrite = _Me1200SynceConfigSourcesClockSourceNominationSsmOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 7),
    _Me1200SynceConfigSourcesClockSourceNominationSsmOverwrite_Type()
)
me1200SynceConfigSourcesClockSourceNominationSsmOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationSsmOverwrite.setStatus("current")
_Me1200SynceConfigSourcesClockSourceNominationHoldoffTime_Type = Unsigned32
_Me1200SynceConfigSourcesClockSourceNominationHoldoffTime_Object = MibTableColumn
me1200SynceConfigSourcesClockSourceNominationHoldoffTime = _Me1200SynceConfigSourcesClockSourceNominationHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 2, 1, 1, 8),
    _Me1200SynceConfigSourcesClockSourceNominationHoldoffTime_Type()
)
me1200SynceConfigSourcesClockSourceNominationHoldoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationHoldoffTime.setStatus("current")
_Me1200SynceConfigPorts_ObjectIdentity = ObjectIdentity
me1200SynceConfigPorts = _Me1200SynceConfigPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 3)
)
_Me1200SynceConfigPortsPortConfigTable_Object = MibTable
me1200SynceConfigPortsPortConfigTable = _Me1200SynceConfigPortsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    me1200SynceConfigPortsPortConfigTable.setStatus("current")
_Me1200SynceConfigPortsPortConfigEntry_Object = MibTableRow
me1200SynceConfigPortsPortConfigEntry = _Me1200SynceConfigPortsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 3, 1, 1)
)
me1200SynceConfigPortsPortConfigEntry.setIndexNames(
    (0, "ME1200-SYNCE-MIB", "me1200SynceConfigPortsPortConfigPortId"),
)
if mibBuilder.loadTexts:
    me1200SynceConfigPortsPortConfigEntry.setStatus("current")
_Me1200SynceConfigPortsPortConfigPortId_Type = ME1200InterfaceIndex
_Me1200SynceConfigPortsPortConfigPortId_Object = MibTableColumn
me1200SynceConfigPortsPortConfigPortId = _Me1200SynceConfigPortsPortConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 3, 1, 1, 1),
    _Me1200SynceConfigPortsPortConfigPortId_Type()
)
me1200SynceConfigPortsPortConfigPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SynceConfigPortsPortConfigPortId.setStatus("current")
_Me1200SynceConfigPortsPortConfigSsmEnabled_Type = TruthValue
_Me1200SynceConfigPortsPortConfigSsmEnabled_Object = MibTableColumn
me1200SynceConfigPortsPortConfigSsmEnabled = _Me1200SynceConfigPortsPortConfigSsmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 2, 3, 1, 1, 2),
    _Me1200SynceConfigPortsPortConfigSsmEnabled_Type()
)
me1200SynceConfigPortsPortConfigSsmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceConfigPortsPortConfigSsmEnabled.setStatus("current")
_Me1200SynceStatus_ObjectIdentity = ObjectIdentity
me1200SynceStatus = _Me1200SynceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3)
)
_Me1200SynceStatusGlobal_ObjectIdentity = ObjectIdentity
me1200SynceStatusGlobal = _Me1200SynceStatusGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1)
)
_Me1200SynceStatusGlobalClockSelectionMode_ObjectIdentity = ObjectIdentity
me1200SynceStatusGlobalClockSelectionMode = _Me1200SynceStatusGlobalClockSelectionMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1, 1)
)
_Me1200SynceStatusGlobalClockSelectionModeClockInput_Type = Unsigned32
_Me1200SynceStatusGlobalClockSelectionModeClockInput_Object = MibScalar
me1200SynceStatusGlobalClockSelectionModeClockInput = _Me1200SynceStatusGlobalClockSelectionModeClockInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1, 1, 1),
    _Me1200SynceStatusGlobalClockSelectionModeClockInput_Type()
)
me1200SynceStatusGlobalClockSelectionModeClockInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusGlobalClockSelectionModeClockInput.setStatus("current")
_Me1200SynceStatusGlobalClockSelectionModeSelectorState_Type = ME1200synceSelectorState
_Me1200SynceStatusGlobalClockSelectionModeSelectorState_Object = MibScalar
me1200SynceStatusGlobalClockSelectionModeSelectorState = _Me1200SynceStatusGlobalClockSelectionModeSelectorState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1, 1, 2),
    _Me1200SynceStatusGlobalClockSelectionModeSelectorState_Type()
)
me1200SynceStatusGlobalClockSelectionModeSelectorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusGlobalClockSelectionModeSelectorState.setStatus("current")
_Me1200SynceStatusGlobalClockSelectionModeLosx_Type = TruthValue
_Me1200SynceStatusGlobalClockSelectionModeLosx_Object = MibScalar
me1200SynceStatusGlobalClockSelectionModeLosx = _Me1200SynceStatusGlobalClockSelectionModeLosx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1, 1, 3),
    _Me1200SynceStatusGlobalClockSelectionModeLosx_Type()
)
me1200SynceStatusGlobalClockSelectionModeLosx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusGlobalClockSelectionModeLosx.setStatus("current")
_Me1200SynceStatusGlobalClockSelectionModeLol_Type = TruthValue
_Me1200SynceStatusGlobalClockSelectionModeLol_Object = MibScalar
me1200SynceStatusGlobalClockSelectionModeLol = _Me1200SynceStatusGlobalClockSelectionModeLol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1, 1, 4),
    _Me1200SynceStatusGlobalClockSelectionModeLol_Type()
)
me1200SynceStatusGlobalClockSelectionModeLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusGlobalClockSelectionModeLol.setStatus("current")
_Me1200SynceStatusGlobalClockSelectionModeDhold_Type = TruthValue
_Me1200SynceStatusGlobalClockSelectionModeDhold_Object = MibScalar
me1200SynceStatusGlobalClockSelectionModeDhold = _Me1200SynceStatusGlobalClockSelectionModeDhold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 1, 1, 5),
    _Me1200SynceStatusGlobalClockSelectionModeDhold_Type()
)
me1200SynceStatusGlobalClockSelectionModeDhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusGlobalClockSelectionModeDhold.setStatus("current")
_Me1200SynceStatusSources_ObjectIdentity = ObjectIdentity
me1200SynceStatusSources = _Me1200SynceStatusSources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2)
)
_Me1200SynceStatusSourcesClockSourceNominationTable_Object = MibTable
me1200SynceStatusSourcesClockSourceNominationTable = _Me1200SynceStatusSourcesClockSourceNominationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationTable.setStatus("current")
_Me1200SynceStatusSourcesClockSourceNominationEntry_Object = MibTableRow
me1200SynceStatusSourcesClockSourceNominationEntry = _Me1200SynceStatusSourcesClockSourceNominationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1, 1)
)
me1200SynceStatusSourcesClockSourceNominationEntry.setIndexNames(
    (0, "ME1200-SYNCE-MIB", "me1200SynceStatusSourcesClockSourceNominationSourceId"),
)
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationEntry.setStatus("current")


class _Me1200SynceStatusSourcesClockSourceNominationSourceId_Type(Integer32):
    """Custom type me1200SynceStatusSourcesClockSourceNominationSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200SynceStatusSourcesClockSourceNominationSourceId_Type.__name__ = "Integer32"
_Me1200SynceStatusSourcesClockSourceNominationSourceId_Object = MibTableColumn
me1200SynceStatusSourcesClockSourceNominationSourceId = _Me1200SynceStatusSourcesClockSourceNominationSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1, 1, 1),
    _Me1200SynceStatusSourcesClockSourceNominationSourceId_Type()
)
me1200SynceStatusSourcesClockSourceNominationSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationSourceId.setStatus("current")
_Me1200SynceStatusSourcesClockSourceNominationLocs_Type = TruthValue
_Me1200SynceStatusSourcesClockSourceNominationLocs_Object = MibTableColumn
me1200SynceStatusSourcesClockSourceNominationLocs = _Me1200SynceStatusSourcesClockSourceNominationLocs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1, 1, 2),
    _Me1200SynceStatusSourcesClockSourceNominationLocs_Type()
)
me1200SynceStatusSourcesClockSourceNominationLocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationLocs.setStatus("current")
_Me1200SynceStatusSourcesClockSourceNominationFos_Type = TruthValue
_Me1200SynceStatusSourcesClockSourceNominationFos_Object = MibTableColumn
me1200SynceStatusSourcesClockSourceNominationFos = _Me1200SynceStatusSourcesClockSourceNominationFos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1, 1, 3),
    _Me1200SynceStatusSourcesClockSourceNominationFos_Type()
)
me1200SynceStatusSourcesClockSourceNominationFos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationFos.setStatus("current")
_Me1200SynceStatusSourcesClockSourceNominationSsm_Type = TruthValue
_Me1200SynceStatusSourcesClockSourceNominationSsm_Object = MibTableColumn
me1200SynceStatusSourcesClockSourceNominationSsm = _Me1200SynceStatusSourcesClockSourceNominationSsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1, 1, 4),
    _Me1200SynceStatusSourcesClockSourceNominationSsm_Type()
)
me1200SynceStatusSourcesClockSourceNominationSsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationSsm.setStatus("current")
_Me1200SynceStatusSourcesClockSourceNominationWtr_Type = TruthValue
_Me1200SynceStatusSourcesClockSourceNominationWtr_Object = MibTableColumn
me1200SynceStatusSourcesClockSourceNominationWtr = _Me1200SynceStatusSourcesClockSourceNominationWtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 2, 1, 1, 5),
    _Me1200SynceStatusSourcesClockSourceNominationWtr_Type()
)
me1200SynceStatusSourcesClockSourceNominationWtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationWtr.setStatus("current")
_Me1200SynceStatusPorts_ObjectIdentity = ObjectIdentity
me1200SynceStatusPorts = _Me1200SynceStatusPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3)
)
_Me1200SynceStatusPortsPortStatusTable_Object = MibTable
me1200SynceStatusPortsPortStatusTable = _Me1200SynceStatusPortsPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusTable.setStatus("current")
_Me1200SynceStatusPortsPortStatusEntry_Object = MibTableRow
me1200SynceStatusPortsPortStatusEntry = _Me1200SynceStatusPortsPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3, 1, 1)
)
me1200SynceStatusPortsPortStatusEntry.setIndexNames(
    (0, "ME1200-SYNCE-MIB", "me1200SynceStatusPortsPortStatusPortId"),
)
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusEntry.setStatus("current")
_Me1200SynceStatusPortsPortStatusPortId_Type = ME1200InterfaceIndex
_Me1200SynceStatusPortsPortStatusPortId_Object = MibTableColumn
me1200SynceStatusPortsPortStatusPortId = _Me1200SynceStatusPortsPortStatusPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3, 1, 1, 1),
    _Me1200SynceStatusPortsPortStatusPortId_Type()
)
me1200SynceStatusPortsPortStatusPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusPortId.setStatus("current")
_Me1200SynceStatusPortsPortStatusSsmRx_Type = ME1200synceQualityLevel
_Me1200SynceStatusPortsPortStatusSsmRx_Object = MibTableColumn
me1200SynceStatusPortsPortStatusSsmRx = _Me1200SynceStatusPortsPortStatusSsmRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3, 1, 1, 2),
    _Me1200SynceStatusPortsPortStatusSsmRx_Type()
)
me1200SynceStatusPortsPortStatusSsmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusSsmRx.setStatus("current")
_Me1200SynceStatusPortsPortStatusSsmTx_Type = ME1200synceQualityLevel
_Me1200SynceStatusPortsPortStatusSsmTx_Object = MibTableColumn
me1200SynceStatusPortsPortStatusSsmTx = _Me1200SynceStatusPortsPortStatusSsmTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3, 1, 1, 3),
    _Me1200SynceStatusPortsPortStatusSsmTx_Type()
)
me1200SynceStatusPortsPortStatusSsmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusSsmTx.setStatus("current")
_Me1200SynceStatusPortsPortStatusMaster_Type = TruthValue
_Me1200SynceStatusPortsPortStatusMaster_Object = MibTableColumn
me1200SynceStatusPortsPortStatusMaster = _Me1200SynceStatusPortsPortStatusMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 3, 1, 1, 4),
    _Me1200SynceStatusPortsPortStatusMaster_Type()
)
me1200SynceStatusPortsPortStatusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusMaster.setStatus("current")
_Me1200SynceStatusPtp_ObjectIdentity = ObjectIdentity
me1200SynceStatusPtp = _Me1200SynceStatusPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 4)
)
_Me1200SynceStatusPtpPortStatusTable_Object = MibTable
me1200SynceStatusPtpPortStatusTable = _Me1200SynceStatusPtpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    me1200SynceStatusPtpPortStatusTable.setStatus("current")
_Me1200SynceStatusPtpPortStatusEntry_Object = MibTableRow
me1200SynceStatusPtpPortStatusEntry = _Me1200SynceStatusPtpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 4, 1, 1)
)
me1200SynceStatusPtpPortStatusEntry.setIndexNames(
    (0, "ME1200-SYNCE-MIB", "me1200SynceStatusPtpPortStatusSourceId"),
)
if mibBuilder.loadTexts:
    me1200SynceStatusPtpPortStatusEntry.setStatus("current")


class _Me1200SynceStatusPtpPortStatusSourceId_Type(Integer32):
    """Custom type me1200SynceStatusPtpPortStatusSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200SynceStatusPtpPortStatusSourceId_Type.__name__ = "Integer32"
_Me1200SynceStatusPtpPortStatusSourceId_Object = MibTableColumn
me1200SynceStatusPtpPortStatusSourceId = _Me1200SynceStatusPtpPortStatusSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 4, 1, 1, 1),
    _Me1200SynceStatusPtpPortStatusSourceId_Type()
)
me1200SynceStatusPtpPortStatusSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SynceStatusPtpPortStatusSourceId.setStatus("current")
_Me1200SynceStatusPtpPortStatusSsmRx_Type = ME1200synceQualityLevel
_Me1200SynceStatusPtpPortStatusSsmRx_Object = MibTableColumn
me1200SynceStatusPtpPortStatusSsmRx = _Me1200SynceStatusPtpPortStatusSsmRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 4, 1, 1, 2),
    _Me1200SynceStatusPtpPortStatusSsmRx_Type()
)
me1200SynceStatusPtpPortStatusSsmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusPtpPortStatusSsmRx.setStatus("current")
_Me1200SynceStatusPtpPortStatusPtsf_Type = ME1200syncePtsfState
_Me1200SynceStatusPtpPortStatusPtsf_Object = MibTableColumn
me1200SynceStatusPtpPortStatusPtsf = _Me1200SynceStatusPtpPortStatusPtsf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 3, 4, 1, 1, 3),
    _Me1200SynceStatusPtpPortStatusPtsf_Type()
)
me1200SynceStatusPtpPortStatusPtsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SynceStatusPtpPortStatusPtsf.setStatus("current")
_Me1200SynceControl_ObjectIdentity = ObjectIdentity
me1200SynceControl = _Me1200SynceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 4)
)
_Me1200SynceControlSources_ObjectIdentity = ObjectIdentity
me1200SynceControlSources = _Me1200SynceControlSources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 4, 1)
)
_Me1200SynceControlSourcesClockSourceTable_Object = MibTable
me1200SynceControlSourcesClockSourceTable = _Me1200SynceControlSourcesClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    me1200SynceControlSourcesClockSourceTable.setStatus("current")
_Me1200SynceControlSourcesClockSourceEntry_Object = MibTableRow
me1200SynceControlSourcesClockSourceEntry = _Me1200SynceControlSourcesClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 4, 1, 1, 1)
)
me1200SynceControlSourcesClockSourceEntry.setIndexNames(
    (0, "ME1200-SYNCE-MIB", "me1200SynceControlSourcesClockSourceSourceId"),
)
if mibBuilder.loadTexts:
    me1200SynceControlSourcesClockSourceEntry.setStatus("current")


class _Me1200SynceControlSourcesClockSourceSourceId_Type(Integer32):
    """Custom type me1200SynceControlSourcesClockSourceSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Me1200SynceControlSourcesClockSourceSourceId_Type.__name__ = "Integer32"
_Me1200SynceControlSourcesClockSourceSourceId_Object = MibTableColumn
me1200SynceControlSourcesClockSourceSourceId = _Me1200SynceControlSourcesClockSourceSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 4, 1, 1, 1, 1),
    _Me1200SynceControlSourcesClockSourceSourceId_Type()
)
me1200SynceControlSourcesClockSourceSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SynceControlSourcesClockSourceSourceId.setStatus("current")
_Me1200SynceControlSourcesClockSourceClearWtr_Type = ME1200Unsigned8
_Me1200SynceControlSourcesClockSourceClearWtr_Object = MibTableColumn
me1200SynceControlSourcesClockSourceClearWtr = _Me1200SynceControlSourcesClockSourceClearWtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 4, 1, 1, 1, 2),
    _Me1200SynceControlSourcesClockSourceClearWtr_Type()
)
me1200SynceControlSourcesClockSourceClearWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SynceControlSourcesClockSourceClearWtr.setStatus("current")
_Me1200SynceNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200SynceNotificationPrefix = _Me1200SynceNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 5)
)
_Me1200SynceNotification_ObjectIdentity = ObjectIdentity
me1200SynceNotification = _Me1200SynceNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 5, 0)
)
_Me1200SynceMibConformance_ObjectIdentity = ObjectIdentity
me1200SynceMibConformance = _Me1200SynceMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2)
)
_Me1200SynceMibCompliances_ObjectIdentity = ObjectIdentity
me1200SynceMibCompliances = _Me1200SynceMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 1)
)
_Me1200SynceMibGroups_ObjectIdentity = ObjectIdentity
me1200SynceMibGroups = _Me1200SynceMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2)
)

# Managed Objects groups

me1200SynceCapabilitiesGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 1)
)
me1200SynceCapabilitiesGlobalInfoGroup.setObjects(
    ("ME1200-SYNCE-MIB", "me1200SynceCapabilitiesGlobalSourceCount")
)
if mibBuilder.loadTexts:
    me1200SynceCapabilitiesGlobalInfoGroup.setStatus("current")

me1200SynceConfigGlobalClockSelectionModeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 2)
)
me1200SynceConfigGlobalClockSelectionModeInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeSelectionMode"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeSource"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeWtrTime"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeSsmHoldover"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeSsmFreerun"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeEecOption"))
)
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalClockSelectionModeInfoGroup.setStatus("current")

me1200SynceConfigGlobalStationClocksInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 3)
)
me1200SynceConfigGlobalStationClocksInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalStationClocksStationClkOut"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalStationClocksStationClkIn"))
)
if mibBuilder.loadTexts:
    me1200SynceConfigGlobalStationClocksInfoGroup.setStatus("current")

me1200SynceConfigSourcesClockSourceNominationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 4)
)
me1200SynceConfigSourcesClockSourceNominationInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationNominated"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationNetworkPort"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationClkInPort"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationPriority"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationAnegMode"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationSsmOverwrite"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationHoldoffTime"))
)
if mibBuilder.loadTexts:
    me1200SynceConfigSourcesClockSourceNominationInfoGroup.setStatus("current")

me1200SynceConfigPortsPortConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 5)
)
me1200SynceConfigPortsPortConfigInfoGroup.setObjects(
    ("ME1200-SYNCE-MIB", "me1200SynceConfigPortsPortConfigSsmEnabled")
)
if mibBuilder.loadTexts:
    me1200SynceConfigPortsPortConfigInfoGroup.setStatus("current")

me1200SynceStatusGlobalClockSelectionModeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 6)
)
me1200SynceStatusGlobalClockSelectionModeInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeClockInput"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeSelectorState"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeLosx"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeLol"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeDhold"))
)
if mibBuilder.loadTexts:
    me1200SynceStatusGlobalClockSelectionModeInfoGroup.setStatus("current")

me1200SynceStatusSourcesClockSourceNominationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 7)
)
me1200SynceStatusSourcesClockSourceNominationInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceStatusSourcesClockSourceNominationLocs"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusSourcesClockSourceNominationFos"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusSourcesClockSourceNominationSsm"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusSourcesClockSourceNominationWtr"))
)
if mibBuilder.loadTexts:
    me1200SynceStatusSourcesClockSourceNominationInfoGroup.setStatus("current")

me1200SynceStatusPortsPortStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 8)
)
me1200SynceStatusPortsPortStatusInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceStatusPortsPortStatusSsmRx"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusPortsPortStatusSsmTx"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusPortsPortStatusMaster"))
)
if mibBuilder.loadTexts:
    me1200SynceStatusPortsPortStatusInfoGroup.setStatus("current")

me1200SynceStatusPtpPortStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 9)
)
me1200SynceStatusPtpPortStatusInfoGroup.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceStatusPtpPortStatusSsmRx"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusPtpPortStatusPtsf"))
)
if mibBuilder.loadTexts:
    me1200SynceStatusPtpPortStatusInfoGroup.setStatus("current")

me1200SynceControlSourcesClockSourceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 10)
)
me1200SynceControlSourcesClockSourceInfoGroup.setObjects(
    ("ME1200-SYNCE-MIB", "me1200SynceControlSourcesClockSourceClearWtr")
)
if mibBuilder.loadTexts:
    me1200SynceControlSourcesClockSourceInfoGroup.setStatus("current")


# Notification objects

me1200SynceNotificationClockSelectorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 1, 5, 0, 1)
)
me1200SynceNotificationClockSelectorStateChange.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeClockInput"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeSelectorState"))
)
if mibBuilder.loadTexts:
    me1200SynceNotificationClockSelectorStateChange.setStatus(
        "current"
    )


# Notifications groups

me1200SynceNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 2, 11)
)
me1200SynceNotificationInfoGroup.setObjects(
    ("ME1200-SYNCE-MIB", "me1200SynceNotificationClockSelectorStateChange")
)
if mibBuilder.loadTexts:
    me1200SynceNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200SynceMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 42, 2, 1, 1)
)
me1200SynceMibCompliance.setObjects(
      *(("ME1200-SYNCE-MIB", "me1200SynceCapabilitiesGlobalInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalClockSelectionModeInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigGlobalStationClocksInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigSourcesClockSourceNominationInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceConfigPortsPortConfigInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusGlobalClockSelectionModeInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusSourcesClockSourceNominationInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusPortsPortStatusInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceStatusPtpPortStatusInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceControlSourcesClockSourceInfoGroup"),
        ("ME1200-SYNCE-MIB", "me1200SynceNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200SynceMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-SYNCE-MIB",
    **{"ME1200synceAnegMode": ME1200synceAnegMode,
       "ME1200synceEecOption": ME1200synceEecOption,
       "ME1200synceFrequency": ME1200synceFrequency,
       "ME1200syncePtsfState": ME1200syncePtsfState,
       "ME1200synceQualityLevel": ME1200synceQualityLevel,
       "ME1200synceSelectionMode": ME1200synceSelectionMode,
       "ME1200synceSelectorState": ME1200synceSelectorState,
       "me1200SynceMib": me1200SynceMib,
       "me1200SynceMibObjects": me1200SynceMibObjects,
       "me1200SynceCapabilities": me1200SynceCapabilities,
       "me1200SynceCapabilitiesGlobal": me1200SynceCapabilitiesGlobal,
       "me1200SynceCapabilitiesGlobalSourceCount": me1200SynceCapabilitiesGlobalSourceCount,
       "me1200SynceConfig": me1200SynceConfig,
       "me1200SynceConfigGlobal": me1200SynceConfigGlobal,
       "me1200SynceConfigGlobalClockSelectionMode": me1200SynceConfigGlobalClockSelectionMode,
       "me1200SynceConfigGlobalClockSelectionModeSelectionMode": me1200SynceConfigGlobalClockSelectionModeSelectionMode,
       "me1200SynceConfigGlobalClockSelectionModeSource": me1200SynceConfigGlobalClockSelectionModeSource,
       "me1200SynceConfigGlobalClockSelectionModeWtrTime": me1200SynceConfigGlobalClockSelectionModeWtrTime,
       "me1200SynceConfigGlobalClockSelectionModeSsmHoldover": me1200SynceConfigGlobalClockSelectionModeSsmHoldover,
       "me1200SynceConfigGlobalClockSelectionModeSsmFreerun": me1200SynceConfigGlobalClockSelectionModeSsmFreerun,
       "me1200SynceConfigGlobalClockSelectionModeEecOption": me1200SynceConfigGlobalClockSelectionModeEecOption,
       "me1200SynceConfigGlobalStationClocks": me1200SynceConfigGlobalStationClocks,
       "me1200SynceConfigGlobalStationClocksStationClkOut": me1200SynceConfigGlobalStationClocksStationClkOut,
       "me1200SynceConfigGlobalStationClocksStationClkIn": me1200SynceConfigGlobalStationClocksStationClkIn,
       "me1200SynceConfigSources": me1200SynceConfigSources,
       "me1200SynceConfigSourcesClockSourceNominationTable": me1200SynceConfigSourcesClockSourceNominationTable,
       "me1200SynceConfigSourcesClockSourceNominationEntry": me1200SynceConfigSourcesClockSourceNominationEntry,
       "me1200SynceConfigSourcesClockSourceNominationSourceId": me1200SynceConfigSourcesClockSourceNominationSourceId,
       "me1200SynceConfigSourcesClockSourceNominationNominated": me1200SynceConfigSourcesClockSourceNominationNominated,
       "me1200SynceConfigSourcesClockSourceNominationNetworkPort": me1200SynceConfigSourcesClockSourceNominationNetworkPort,
       "me1200SynceConfigSourcesClockSourceNominationClkInPort": me1200SynceConfigSourcesClockSourceNominationClkInPort,
       "me1200SynceConfigSourcesClockSourceNominationPriority": me1200SynceConfigSourcesClockSourceNominationPriority,
       "me1200SynceConfigSourcesClockSourceNominationAnegMode": me1200SynceConfigSourcesClockSourceNominationAnegMode,
       "me1200SynceConfigSourcesClockSourceNominationSsmOverwrite": me1200SynceConfigSourcesClockSourceNominationSsmOverwrite,
       "me1200SynceConfigSourcesClockSourceNominationHoldoffTime": me1200SynceConfigSourcesClockSourceNominationHoldoffTime,
       "me1200SynceConfigPorts": me1200SynceConfigPorts,
       "me1200SynceConfigPortsPortConfigTable": me1200SynceConfigPortsPortConfigTable,
       "me1200SynceConfigPortsPortConfigEntry": me1200SynceConfigPortsPortConfigEntry,
       "me1200SynceConfigPortsPortConfigPortId": me1200SynceConfigPortsPortConfigPortId,
       "me1200SynceConfigPortsPortConfigSsmEnabled": me1200SynceConfigPortsPortConfigSsmEnabled,
       "me1200SynceStatus": me1200SynceStatus,
       "me1200SynceStatusGlobal": me1200SynceStatusGlobal,
       "me1200SynceStatusGlobalClockSelectionMode": me1200SynceStatusGlobalClockSelectionMode,
       "me1200SynceStatusGlobalClockSelectionModeClockInput": me1200SynceStatusGlobalClockSelectionModeClockInput,
       "me1200SynceStatusGlobalClockSelectionModeSelectorState": me1200SynceStatusGlobalClockSelectionModeSelectorState,
       "me1200SynceStatusGlobalClockSelectionModeLosx": me1200SynceStatusGlobalClockSelectionModeLosx,
       "me1200SynceStatusGlobalClockSelectionModeLol": me1200SynceStatusGlobalClockSelectionModeLol,
       "me1200SynceStatusGlobalClockSelectionModeDhold": me1200SynceStatusGlobalClockSelectionModeDhold,
       "me1200SynceStatusSources": me1200SynceStatusSources,
       "me1200SynceStatusSourcesClockSourceNominationTable": me1200SynceStatusSourcesClockSourceNominationTable,
       "me1200SynceStatusSourcesClockSourceNominationEntry": me1200SynceStatusSourcesClockSourceNominationEntry,
       "me1200SynceStatusSourcesClockSourceNominationSourceId": me1200SynceStatusSourcesClockSourceNominationSourceId,
       "me1200SynceStatusSourcesClockSourceNominationLocs": me1200SynceStatusSourcesClockSourceNominationLocs,
       "me1200SynceStatusSourcesClockSourceNominationFos": me1200SynceStatusSourcesClockSourceNominationFos,
       "me1200SynceStatusSourcesClockSourceNominationSsm": me1200SynceStatusSourcesClockSourceNominationSsm,
       "me1200SynceStatusSourcesClockSourceNominationWtr": me1200SynceStatusSourcesClockSourceNominationWtr,
       "me1200SynceStatusPorts": me1200SynceStatusPorts,
       "me1200SynceStatusPortsPortStatusTable": me1200SynceStatusPortsPortStatusTable,
       "me1200SynceStatusPortsPortStatusEntry": me1200SynceStatusPortsPortStatusEntry,
       "me1200SynceStatusPortsPortStatusPortId": me1200SynceStatusPortsPortStatusPortId,
       "me1200SynceStatusPortsPortStatusSsmRx": me1200SynceStatusPortsPortStatusSsmRx,
       "me1200SynceStatusPortsPortStatusSsmTx": me1200SynceStatusPortsPortStatusSsmTx,
       "me1200SynceStatusPortsPortStatusMaster": me1200SynceStatusPortsPortStatusMaster,
       "me1200SynceStatusPtp": me1200SynceStatusPtp,
       "me1200SynceStatusPtpPortStatusTable": me1200SynceStatusPtpPortStatusTable,
       "me1200SynceStatusPtpPortStatusEntry": me1200SynceStatusPtpPortStatusEntry,
       "me1200SynceStatusPtpPortStatusSourceId": me1200SynceStatusPtpPortStatusSourceId,
       "me1200SynceStatusPtpPortStatusSsmRx": me1200SynceStatusPtpPortStatusSsmRx,
       "me1200SynceStatusPtpPortStatusPtsf": me1200SynceStatusPtpPortStatusPtsf,
       "me1200SynceControl": me1200SynceControl,
       "me1200SynceControlSources": me1200SynceControlSources,
       "me1200SynceControlSourcesClockSourceTable": me1200SynceControlSourcesClockSourceTable,
       "me1200SynceControlSourcesClockSourceEntry": me1200SynceControlSourcesClockSourceEntry,
       "me1200SynceControlSourcesClockSourceSourceId": me1200SynceControlSourcesClockSourceSourceId,
       "me1200SynceControlSourcesClockSourceClearWtr": me1200SynceControlSourcesClockSourceClearWtr,
       "me1200SynceNotificationPrefix": me1200SynceNotificationPrefix,
       "me1200SynceNotification": me1200SynceNotification,
       "me1200SynceNotificationClockSelectorStateChange": me1200SynceNotificationClockSelectorStateChange,
       "me1200SynceMibConformance": me1200SynceMibConformance,
       "me1200SynceMibCompliances": me1200SynceMibCompliances,
       "me1200SynceMibCompliance": me1200SynceMibCompliance,
       "me1200SynceMibGroups": me1200SynceMibGroups,
       "me1200SynceCapabilitiesGlobalInfoGroup": me1200SynceCapabilitiesGlobalInfoGroup,
       "me1200SynceConfigGlobalClockSelectionModeInfoGroup": me1200SynceConfigGlobalClockSelectionModeInfoGroup,
       "me1200SynceConfigGlobalStationClocksInfoGroup": me1200SynceConfigGlobalStationClocksInfoGroup,
       "me1200SynceConfigSourcesClockSourceNominationInfoGroup": me1200SynceConfigSourcesClockSourceNominationInfoGroup,
       "me1200SynceConfigPortsPortConfigInfoGroup": me1200SynceConfigPortsPortConfigInfoGroup,
       "me1200SynceStatusGlobalClockSelectionModeInfoGroup": me1200SynceStatusGlobalClockSelectionModeInfoGroup,
       "me1200SynceStatusSourcesClockSourceNominationInfoGroup": me1200SynceStatusSourcesClockSourceNominationInfoGroup,
       "me1200SynceStatusPortsPortStatusInfoGroup": me1200SynceStatusPortsPortStatusInfoGroup,
       "me1200SynceStatusPtpPortStatusInfoGroup": me1200SynceStatusPtpPortStatusInfoGroup,
       "me1200SynceControlSourcesClockSourceInfoGroup": me1200SynceControlSourcesClockSourceInfoGroup,
       "me1200SynceNotificationInfoGroup": me1200SynceNotificationInfoGroup}
)
