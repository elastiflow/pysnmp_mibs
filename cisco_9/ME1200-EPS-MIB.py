# SNMP MIB module (ME1200-EPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-EPS-MIB.mib
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
 ME1200RowEditorState) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200RowEditorState")

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

me1200EpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45)
)
if mibBuilder.loadTexts:
    me1200EpsMib.setRevisions(
        ("2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-02-04 00:00",
         "2014-01-29 00:00",
         "2013-10-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200EpsDomain(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("port", 0),
          ("evc", 1))
    )



class ME1200EpsArchitecture(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 0),
          ("oneForOne", 1))
    )



class ME1200EpsDirectional(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 0),
          ("biDirectional", 1))
    )



class ME1200EpsCommand(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1),
          ("lockOut", 2),
          ("forcedSwitch", 3),
          ("manualSwitchProtection", 4),
          ("manualSwitchWorking", 5),
          ("exercise", 6),
          ("localFreeze", 7),
          ("localLockOut", 8))
    )



class ME1200EpsProtectionState(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("noRequestWorking", 1),
          ("noRequestProtecting", 2),
          ("lockOut", 3),
          ("forcedSwitch", 4),
          ("signalFailWorking", 5),
          ("signalFailProtecting", 6),
          ("manualSwitchWorking", 7),
          ("manualSwitchProtecting", 8),
          ("waitToRestore", 9),
          ("exerciseWorking", 10),
          ("exerciseProtecting", 11),
          ("reverseRequestWorking", 12),
          ("reverseRequestProtecting", 13),
          ("doNotRevert", 14))
    )



class ME1200EpsDefectState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("sd", 1),
          ("sf", 2))
    )



class ME1200EpsRequest(TextualConvention, Integer32):
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("nr", 0),
          ("dnr", 1),
          ("rr", 2),
          ("exer", 3),
          ("wtr", 4),
          ("msW", 5),
          ("msP", 6),
          ("sd", 7),
          ("sfW", 8),
          ("fs", 9),
          ("sfP", 10),
          ("lo", 11))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200EpsMibObjects_ObjectIdentity = ObjectIdentity
me1200EpsMibObjects = _Me1200EpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1)
)
_Me1200EpsCapabilities_ObjectIdentity = ObjectIdentity
me1200EpsCapabilities = _Me1200EpsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1)
)
_Me1200EpsCapabilitiesInstanceMax_Type = Unsigned32
_Me1200EpsCapabilitiesInstanceMax_Object = MibScalar
me1200EpsCapabilitiesInstanceMax = _Me1200EpsCapabilitiesInstanceMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1, 1),
    _Me1200EpsCapabilitiesInstanceMax_Type()
)
me1200EpsCapabilitiesInstanceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesInstanceMax.setStatus("current")
_Me1200EpsCapabilitiesWtrMax_Type = Unsigned32
_Me1200EpsCapabilitiesWtrMax_Object = MibScalar
me1200EpsCapabilitiesWtrMax = _Me1200EpsCapabilitiesWtrMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1, 2),
    _Me1200EpsCapabilitiesWtrMax_Type()
)
me1200EpsCapabilitiesWtrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesWtrMax.setStatus("current")
_Me1200EpsCapabilitiesHoldOffOff_Type = Unsigned32
_Me1200EpsCapabilitiesHoldOffOff_Object = MibScalar
me1200EpsCapabilitiesHoldOffOff = _Me1200EpsCapabilitiesHoldOffOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1, 3),
    _Me1200EpsCapabilitiesHoldOffOff_Type()
)
me1200EpsCapabilitiesHoldOffOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesHoldOffOff.setStatus("current")
_Me1200EpsCapabilitiesHoldOffMax_Type = Unsigned32
_Me1200EpsCapabilitiesHoldOffMax_Object = MibScalar
me1200EpsCapabilitiesHoldOffMax = _Me1200EpsCapabilitiesHoldOffMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1, 4),
    _Me1200EpsCapabilitiesHoldOffMax_Type()
)
me1200EpsCapabilitiesHoldOffMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesHoldOffMax.setStatus("current")
_Me1200EpsCapabilitiesMepMax_Type = Unsigned32
_Me1200EpsCapabilitiesMepMax_Object = MibScalar
me1200EpsCapabilitiesMepMax = _Me1200EpsCapabilitiesMepMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1, 5),
    _Me1200EpsCapabilitiesMepMax_Type()
)
me1200EpsCapabilitiesMepMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesMepMax.setStatus("current")
_Me1200EpsCapabilitiesMepInvalid_Type = Unsigned32
_Me1200EpsCapabilitiesMepInvalid_Object = MibScalar
me1200EpsCapabilitiesMepInvalid = _Me1200EpsCapabilitiesMepInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 1, 6),
    _Me1200EpsCapabilitiesMepInvalid_Type()
)
me1200EpsCapabilitiesMepInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesMepInvalid.setStatus("current")
_Me1200EpsConfig_ObjectIdentity = ObjectIdentity
me1200EpsConfig = _Me1200EpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2)
)
_Me1200InstanceTable_Object = MibTable
me1200InstanceTable = _Me1200InstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200InstanceTable.setStatus("current")
_Me1200InstanceEntry_Object = MibTableRow
me1200InstanceEntry = _Me1200InstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1)
)
me1200InstanceEntry.setIndexNames(
    (0, "ME1200-EPS-MIB", "me1200InstanceId"),
)
if mibBuilder.loadTexts:
    me1200InstanceEntry.setStatus("current")


class _Me1200InstanceId_Type(Integer32):
    """Custom type me1200InstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200InstanceId_Type.__name__ = "Integer32"
_Me1200InstanceId_Object = MibTableColumn
me1200InstanceId = _Me1200InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1, 1),
    _Me1200InstanceId_Type()
)
me1200InstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200InstanceId.setStatus("current")
_Me1200InstanceDomain_Type = ME1200EpsDomain
_Me1200InstanceDomain_Object = MibTableColumn
me1200InstanceDomain = _Me1200InstanceDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1, 2),
    _Me1200InstanceDomain_Type()
)
me1200InstanceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceDomain.setStatus("current")
_Me1200InstanceArchitecture_Type = ME1200EpsArchitecture
_Me1200InstanceArchitecture_Object = MibTableColumn
me1200InstanceArchitecture = _Me1200InstanceArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1, 3),
    _Me1200InstanceArchitecture_Type()
)
me1200InstanceArchitecture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceArchitecture.setStatus("current")
_Me1200InstanceWorkingFlow_Type = ME1200InterfaceIndex
_Me1200InstanceWorkingFlow_Object = MibTableColumn
me1200InstanceWorkingFlow = _Me1200InstanceWorkingFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1, 4),
    _Me1200InstanceWorkingFlow_Type()
)
me1200InstanceWorkingFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceWorkingFlow.setStatus("current")
_Me1200InstanceProtectingFlow_Type = ME1200InterfaceIndex
_Me1200InstanceProtectingFlow_Object = MibTableColumn
me1200InstanceProtectingFlow = _Me1200InstanceProtectingFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1, 5),
    _Me1200InstanceProtectingFlow_Type()
)
me1200InstanceProtectingFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceProtectingFlow.setStatus("current")
_Me1200InstanceAction_Type = ME1200RowEditorState
_Me1200InstanceAction_Object = MibTableColumn
me1200InstanceAction = _Me1200InstanceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 1, 1, 100),
    _Me1200InstanceAction_Type()
)
me1200InstanceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceAction.setStatus("current")
_Me1200InstanceRowEditor_ObjectIdentity = ObjectIdentity
me1200InstanceRowEditor = _Me1200InstanceRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2)
)


class _Me1200InstanceRowEditorId_Type(Integer32):
    """Custom type me1200InstanceRowEditorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200InstanceRowEditorId_Type.__name__ = "Integer32"
_Me1200InstanceRowEditorId_Object = MibScalar
me1200InstanceRowEditorId = _Me1200InstanceRowEditorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2, 1),
    _Me1200InstanceRowEditorId_Type()
)
me1200InstanceRowEditorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceRowEditorId.setStatus("current")
_Me1200InstanceRowEditorDomain_Type = ME1200EpsDomain
_Me1200InstanceRowEditorDomain_Object = MibScalar
me1200InstanceRowEditorDomain = _Me1200InstanceRowEditorDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2, 2),
    _Me1200InstanceRowEditorDomain_Type()
)
me1200InstanceRowEditorDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceRowEditorDomain.setStatus("current")
_Me1200InstanceRowEditorArchitecture_Type = ME1200EpsArchitecture
_Me1200InstanceRowEditorArchitecture_Object = MibScalar
me1200InstanceRowEditorArchitecture = _Me1200InstanceRowEditorArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2, 3),
    _Me1200InstanceRowEditorArchitecture_Type()
)
me1200InstanceRowEditorArchitecture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceRowEditorArchitecture.setStatus("current")
_Me1200InstanceRowEditorWorkingFlow_Type = ME1200InterfaceIndex
_Me1200InstanceRowEditorWorkingFlow_Object = MibScalar
me1200InstanceRowEditorWorkingFlow = _Me1200InstanceRowEditorWorkingFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2, 4),
    _Me1200InstanceRowEditorWorkingFlow_Type()
)
me1200InstanceRowEditorWorkingFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceRowEditorWorkingFlow.setStatus("current")
_Me1200InstanceRowEditorProtectingFlow_Type = ME1200InterfaceIndex
_Me1200InstanceRowEditorProtectingFlow_Object = MibScalar
me1200InstanceRowEditorProtectingFlow = _Me1200InstanceRowEditorProtectingFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2, 5),
    _Me1200InstanceRowEditorProtectingFlow_Type()
)
me1200InstanceRowEditorProtectingFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceRowEditorProtectingFlow.setStatus("current")
_Me1200InstanceRowEditorAction_Type = ME1200RowEditorState
_Me1200InstanceRowEditorAction_Object = MibScalar
me1200InstanceRowEditorAction = _Me1200InstanceRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 2, 100),
    _Me1200InstanceRowEditorAction_Type()
)
me1200InstanceRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200InstanceRowEditorAction.setStatus("current")
_Me1200ConfigTable_Object = MibTable
me1200ConfigTable = _Me1200ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200ConfigTable.setStatus("current")
_Me1200ConfigEntry_Object = MibTableRow
me1200ConfigEntry = _Me1200ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1)
)
me1200ConfigEntry.setIndexNames(
    (0, "ME1200-EPS-MIB", "me1200ConfigId"),
)
if mibBuilder.loadTexts:
    me1200ConfigEntry.setStatus("current")


class _Me1200ConfigId_Type(Integer32):
    """Custom type me1200ConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200ConfigId_Type.__name__ = "Integer32"
_Me1200ConfigId_Object = MibTableColumn
me1200ConfigId = _Me1200ConfigId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1, 1),
    _Me1200ConfigId_Type()
)
me1200ConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200ConfigId.setStatus("current")
_Me1200ConfigDirectional_Type = ME1200EpsDirectional
_Me1200ConfigDirectional_Object = MibTableColumn
me1200ConfigDirectional = _Me1200ConfigDirectional_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1, 2),
    _Me1200ConfigDirectional_Type()
)
me1200ConfigDirectional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigDirectional.setStatus("current")
_Me1200ConfigApsEnable_Type = TruthValue
_Me1200ConfigApsEnable_Object = MibTableColumn
me1200ConfigApsEnable = _Me1200ConfigApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1, 3),
    _Me1200ConfigApsEnable_Type()
)
me1200ConfigApsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigApsEnable.setStatus("current")
_Me1200ConfigRevertive_Type = TruthValue
_Me1200ConfigRevertive_Object = MibTableColumn
me1200ConfigRevertive = _Me1200ConfigRevertive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1, 4),
    _Me1200ConfigRevertive_Type()
)
me1200ConfigRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigRevertive.setStatus("current")
_Me1200ConfigRestoreTimer_Type = Unsigned32
_Me1200ConfigRestoreTimer_Object = MibTableColumn
me1200ConfigRestoreTimer = _Me1200ConfigRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1, 5),
    _Me1200ConfigRestoreTimer_Type()
)
me1200ConfigRestoreTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigRestoreTimer.setStatus("current")
_Me1200ConfigHoldOffTimer_Type = Unsigned32
_Me1200ConfigHoldOffTimer_Object = MibTableColumn
me1200ConfigHoldOffTimer = _Me1200ConfigHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 3, 1, 6),
    _Me1200ConfigHoldOffTimer_Type()
)
me1200ConfigHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200ConfigHoldOffTimer.setStatus("current")
_Me1200MepTable_Object = MibTable
me1200MepTable = _Me1200MepTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200MepTable.setStatus("current")
_Me1200MepEntry_Object = MibTableRow
me1200MepEntry = _Me1200MepEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 4, 1)
)
me1200MepEntry.setIndexNames(
    (0, "ME1200-EPS-MIB", "me1200MepId"),
)
if mibBuilder.loadTexts:
    me1200MepEntry.setStatus("current")


class _Me1200MepId_Type(Integer32):
    """Custom type me1200MepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200MepId_Type.__name__ = "Integer32"
_Me1200MepId_Object = MibTableColumn
me1200MepId = _Me1200MepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 4, 1, 1),
    _Me1200MepId_Type()
)
me1200MepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MepId.setStatus("current")
_Me1200MepWorkingMep_Type = Unsigned32
_Me1200MepWorkingMep_Object = MibTableColumn
me1200MepWorkingMep = _Me1200MepWorkingMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 4, 1, 2),
    _Me1200MepWorkingMep_Type()
)
me1200MepWorkingMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MepWorkingMep.setStatus("current")
_Me1200MepProtectingMep_Type = Unsigned32
_Me1200MepProtectingMep_Object = MibTableColumn
me1200MepProtectingMep = _Me1200MepProtectingMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 4, 1, 3),
    _Me1200MepProtectingMep_Type()
)
me1200MepProtectingMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MepProtectingMep.setStatus("current")
_Me1200MepApsMep_Type = Unsigned32
_Me1200MepApsMep_Object = MibTableColumn
me1200MepApsMep = _Me1200MepApsMep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 4, 1, 4),
    _Me1200MepApsMep_Type()
)
me1200MepApsMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MepApsMep.setStatus("current")
_Me1200CommandTable_Object = MibTable
me1200CommandTable = _Me1200CommandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200CommandTable.setStatus("current")
_Me1200CommandEntry_Object = MibTableRow
me1200CommandEntry = _Me1200CommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 5, 1)
)
me1200CommandEntry.setIndexNames(
    (0, "ME1200-EPS-MIB", "me1200CommandId"),
)
if mibBuilder.loadTexts:
    me1200CommandEntry.setStatus("current")


class _Me1200CommandId_Type(Integer32):
    """Custom type me1200CommandId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200CommandId_Type.__name__ = "Integer32"
_Me1200CommandId_Object = MibTableColumn
me1200CommandId = _Me1200CommandId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 5, 1, 1),
    _Me1200CommandId_Type()
)
me1200CommandId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200CommandId.setStatus("current")
_Me1200CommandCommand_Type = ME1200EpsCommand
_Me1200CommandCommand_Object = MibTableColumn
me1200CommandCommand = _Me1200CommandCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 2, 5, 1, 2),
    _Me1200CommandCommand_Type()
)
me1200CommandCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200CommandCommand.setStatus("current")
_Me1200EpsStatus_ObjectIdentity = ObjectIdentity
me1200EpsStatus = _Me1200EpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3)
)
_Me1200StatusTable_Object = MibTable
me1200StatusTable = _Me1200StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200StatusTable.setStatus("current")
_Me1200StatusEntry_Object = MibTableRow
me1200StatusEntry = _Me1200StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1)
)
me1200StatusEntry.setIndexNames(
    (0, "ME1200-EPS-MIB", "me1200StatusId"),
)
if mibBuilder.loadTexts:
    me1200StatusEntry.setStatus("current")


class _Me1200StatusId_Type(Integer32):
    """Custom type me1200StatusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200StatusId_Type.__name__ = "Integer32"
_Me1200StatusId_Object = MibTableColumn
me1200StatusId = _Me1200StatusId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 1),
    _Me1200StatusId_Type()
)
me1200StatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200StatusId.setStatus("current")
_Me1200StatusProtectionState_Type = ME1200EpsProtectionState
_Me1200StatusProtectionState_Object = MibTableColumn
me1200StatusProtectionState = _Me1200StatusProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 2),
    _Me1200StatusProtectionState_Type()
)
me1200StatusProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusProtectionState.setStatus("current")
_Me1200StatusWorkingState_Type = ME1200EpsDefectState
_Me1200StatusWorkingState_Object = MibTableColumn
me1200StatusWorkingState = _Me1200StatusWorkingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 3),
    _Me1200StatusWorkingState_Type()
)
me1200StatusWorkingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusWorkingState.setStatus("current")
_Me1200StatusProtectingState_Type = ME1200EpsDefectState
_Me1200StatusProtectingState_Object = MibTableColumn
me1200StatusProtectingState = _Me1200StatusProtectingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 4),
    _Me1200StatusProtectingState_Type()
)
me1200StatusProtectingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusProtectingState.setStatus("current")
_Me1200StatusTransmittedApsRequest_Type = ME1200EpsRequest
_Me1200StatusTransmittedApsRequest_Object = MibTableColumn
me1200StatusTransmittedApsRequest = _Me1200StatusTransmittedApsRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 5),
    _Me1200StatusTransmittedApsRequest_Type()
)
me1200StatusTransmittedApsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTransmittedApsRequest.setStatus("current")
_Me1200StatusTransmittedApsReSignal_Type = Unsigned32
_Me1200StatusTransmittedApsReSignal_Object = MibTableColumn
me1200StatusTransmittedApsReSignal = _Me1200StatusTransmittedApsReSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 6),
    _Me1200StatusTransmittedApsReSignal_Type()
)
me1200StatusTransmittedApsReSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTransmittedApsReSignal.setStatus("current")
_Me1200StatusTransmittedApsBrSignal_Type = Unsigned32
_Me1200StatusTransmittedApsBrSignal_Object = MibTableColumn
me1200StatusTransmittedApsBrSignal = _Me1200StatusTransmittedApsBrSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 7),
    _Me1200StatusTransmittedApsBrSignal_Type()
)
me1200StatusTransmittedApsBrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusTransmittedApsBrSignal.setStatus("current")
_Me1200StatusReceivedApsRequest_Type = ME1200EpsRequest
_Me1200StatusReceivedApsRequest_Object = MibTableColumn
me1200StatusReceivedApsRequest = _Me1200StatusReceivedApsRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 8),
    _Me1200StatusReceivedApsRequest_Type()
)
me1200StatusReceivedApsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusReceivedApsRequest.setStatus("current")
_Me1200StatusReceivedApsReSignal_Type = Unsigned32
_Me1200StatusReceivedApsReSignal_Object = MibTableColumn
me1200StatusReceivedApsReSignal = _Me1200StatusReceivedApsReSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 9),
    _Me1200StatusReceivedApsReSignal_Type()
)
me1200StatusReceivedApsReSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusReceivedApsReSignal.setStatus("current")
_Me1200StatusReceivedApsBrSignal_Type = Unsigned32
_Me1200StatusReceivedApsBrSignal_Object = MibTableColumn
me1200StatusReceivedApsBrSignal = _Me1200StatusReceivedApsBrSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 10),
    _Me1200StatusReceivedApsBrSignal_Type()
)
me1200StatusReceivedApsBrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusReceivedApsBrSignal.setStatus("current")
_Me1200StatusDfopPm_Type = TruthValue
_Me1200StatusDfopPm_Object = MibTableColumn
me1200StatusDfopPm = _Me1200StatusDfopPm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 11),
    _Me1200StatusDfopPm_Type()
)
me1200StatusDfopPm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDfopPm.setStatus("current")
_Me1200StatusDfopCm_Type = TruthValue
_Me1200StatusDfopCm_Object = MibTableColumn
me1200StatusDfopCm = _Me1200StatusDfopCm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 12),
    _Me1200StatusDfopCm_Type()
)
me1200StatusDfopCm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDfopCm.setStatus("current")
_Me1200StatusDfopNr_Type = TruthValue
_Me1200StatusDfopNr_Object = MibTableColumn
me1200StatusDfopNr = _Me1200StatusDfopNr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 13),
    _Me1200StatusDfopNr_Type()
)
me1200StatusDfopNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDfopNr.setStatus("current")
_Me1200StatusDfopNoAps_Type = TruthValue
_Me1200StatusDfopNoAps_Object = MibTableColumn
me1200StatusDfopNoAps = _Me1200StatusDfopNoAps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 3, 1, 1, 14),
    _Me1200StatusDfopNoAps_Type()
)
me1200StatusDfopNoAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200StatusDfopNoAps.setStatus("current")
_Me1200EpsControl_ObjectIdentity = ObjectIdentity
me1200EpsControl = _Me1200EpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 1, 4)
)
_Me1200EpsMibConformance_ObjectIdentity = ObjectIdentity
me1200EpsMibConformance = _Me1200EpsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3)
)
_Me1200EpsMibCompliances_ObjectIdentity = ObjectIdentity
me1200EpsMibCompliances = _Me1200EpsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 1)
)
_Me1200EpsMibGroups_ObjectIdentity = ObjectIdentity
me1200EpsMibGroups = _Me1200EpsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2)
)

# Managed Objects groups

me1200EpsCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 1)
)
me1200EpsCapabilitiesInfoGroup.setObjects(
      *(("ME1200-EPS-MIB", "me1200EpsCapabilitiesInstanceMax"),
        ("ME1200-EPS-MIB", "me1200EpsCapabilitiesWtrMax"),
        ("ME1200-EPS-MIB", "me1200EpsCapabilitiesHoldOffOff"),
        ("ME1200-EPS-MIB", "me1200EpsCapabilitiesHoldOffMax"),
        ("ME1200-EPS-MIB", "me1200EpsCapabilitiesMepMax"),
        ("ME1200-EPS-MIB", "me1200EpsCapabilitiesMepInvalid"))
)
if mibBuilder.loadTexts:
    me1200EpsCapabilitiesInfoGroup.setStatus("current")

me1200InstanceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 2)
)
me1200InstanceTableInfoGroup.setObjects(
      *(("ME1200-EPS-MIB", "me1200InstanceDomain"),
        ("ME1200-EPS-MIB", "me1200InstanceArchitecture"),
        ("ME1200-EPS-MIB", "me1200InstanceWorkingFlow"),
        ("ME1200-EPS-MIB", "me1200InstanceProtectingFlow"),
        ("ME1200-EPS-MIB", "me1200InstanceAction"))
)
if mibBuilder.loadTexts:
    me1200InstanceTableInfoGroup.setStatus("current")

me1200InstanceRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 3)
)
me1200InstanceRowEditorInfoGroup.setObjects(
      *(("ME1200-EPS-MIB", "me1200InstanceRowEditorId"),
        ("ME1200-EPS-MIB", "me1200InstanceRowEditorDomain"),
        ("ME1200-EPS-MIB", "me1200InstanceRowEditorArchitecture"),
        ("ME1200-EPS-MIB", "me1200InstanceRowEditorWorkingFlow"),
        ("ME1200-EPS-MIB", "me1200InstanceRowEditorProtectingFlow"),
        ("ME1200-EPS-MIB", "me1200InstanceRowEditorAction"))
)
if mibBuilder.loadTexts:
    me1200InstanceRowEditorInfoGroup.setStatus("current")

me1200ConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 4)
)
me1200ConfigTableInfoGroup.setObjects(
      *(("ME1200-EPS-MIB", "me1200ConfigDirectional"),
        ("ME1200-EPS-MIB", "me1200ConfigApsEnable"),
        ("ME1200-EPS-MIB", "me1200ConfigRevertive"),
        ("ME1200-EPS-MIB", "me1200ConfigRestoreTimer"),
        ("ME1200-EPS-MIB", "me1200ConfigHoldOffTimer"))
)
if mibBuilder.loadTexts:
    me1200ConfigTableInfoGroup.setStatus("current")

me1200MepTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 5)
)
me1200MepTableInfoGroup.setObjects(
      *(("ME1200-EPS-MIB", "me1200MepWorkingMep"),
        ("ME1200-EPS-MIB", "me1200MepProtectingMep"),
        ("ME1200-EPS-MIB", "me1200MepApsMep"))
)
if mibBuilder.loadTexts:
    me1200MepTableInfoGroup.setStatus("current")

me1200CommandTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 6)
)
me1200CommandTableInfoGroup.setObjects(
    ("ME1200-EPS-MIB", "me1200CommandCommand")
)
if mibBuilder.loadTexts:
    me1200CommandTableInfoGroup.setStatus("current")

me1200StatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 2, 7)
)
me1200StatusTableInfoGroup.setObjects(
      *(("ME1200-EPS-MIB", "me1200StatusProtectionState"),
        ("ME1200-EPS-MIB", "me1200StatusWorkingState"),
        ("ME1200-EPS-MIB", "me1200StatusProtectingState"),
        ("ME1200-EPS-MIB", "me1200StatusTransmittedApsRequest"),
        ("ME1200-EPS-MIB", "me1200StatusTransmittedApsReSignal"),
        ("ME1200-EPS-MIB", "me1200StatusTransmittedApsBrSignal"),
        ("ME1200-EPS-MIB", "me1200StatusReceivedApsRequest"),
        ("ME1200-EPS-MIB", "me1200StatusReceivedApsReSignal"),
        ("ME1200-EPS-MIB", "me1200StatusReceivedApsBrSignal"),
        ("ME1200-EPS-MIB", "me1200StatusDfopPm"),
        ("ME1200-EPS-MIB", "me1200StatusDfopCm"),
        ("ME1200-EPS-MIB", "me1200StatusDfopNr"),
        ("ME1200-EPS-MIB", "me1200StatusDfopNoAps"))
)
if mibBuilder.loadTexts:
    me1200StatusTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200EpsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 45, 3, 1, 1)
)
me1200EpsMibCompliance.setObjects(
      *(("ME1200-EPS-MIB", "me1200EpsCapabilitiesInfoGroup"),
        ("ME1200-EPS-MIB", "me1200InstanceTableInfoGroup"),
        ("ME1200-EPS-MIB", "me1200InstanceRowEditorInfoGroup"),
        ("ME1200-EPS-MIB", "me1200ConfigTableInfoGroup"),
        ("ME1200-EPS-MIB", "me1200MepTableInfoGroup"),
        ("ME1200-EPS-MIB", "me1200CommandTableInfoGroup"),
        ("ME1200-EPS-MIB", "me1200StatusTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200EpsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-EPS-MIB",
    **{"ME1200EpsDomain": ME1200EpsDomain,
       "ME1200EpsArchitecture": ME1200EpsArchitecture,
       "ME1200EpsDirectional": ME1200EpsDirectional,
       "ME1200EpsCommand": ME1200EpsCommand,
       "ME1200EpsProtectionState": ME1200EpsProtectionState,
       "ME1200EpsDefectState": ME1200EpsDefectState,
       "ME1200EpsRequest": ME1200EpsRequest,
       "me1200EpsMib": me1200EpsMib,
       "me1200EpsMibObjects": me1200EpsMibObjects,
       "me1200EpsCapabilities": me1200EpsCapabilities,
       "me1200EpsCapabilitiesInstanceMax": me1200EpsCapabilitiesInstanceMax,
       "me1200EpsCapabilitiesWtrMax": me1200EpsCapabilitiesWtrMax,
       "me1200EpsCapabilitiesHoldOffOff": me1200EpsCapabilitiesHoldOffOff,
       "me1200EpsCapabilitiesHoldOffMax": me1200EpsCapabilitiesHoldOffMax,
       "me1200EpsCapabilitiesMepMax": me1200EpsCapabilitiesMepMax,
       "me1200EpsCapabilitiesMepInvalid": me1200EpsCapabilitiesMepInvalid,
       "me1200EpsConfig": me1200EpsConfig,
       "me1200InstanceTable": me1200InstanceTable,
       "me1200InstanceEntry": me1200InstanceEntry,
       "me1200InstanceId": me1200InstanceId,
       "me1200InstanceDomain": me1200InstanceDomain,
       "me1200InstanceArchitecture": me1200InstanceArchitecture,
       "me1200InstanceWorkingFlow": me1200InstanceWorkingFlow,
       "me1200InstanceProtectingFlow": me1200InstanceProtectingFlow,
       "me1200InstanceAction": me1200InstanceAction,
       "me1200InstanceRowEditor": me1200InstanceRowEditor,
       "me1200InstanceRowEditorId": me1200InstanceRowEditorId,
       "me1200InstanceRowEditorDomain": me1200InstanceRowEditorDomain,
       "me1200InstanceRowEditorArchitecture": me1200InstanceRowEditorArchitecture,
       "me1200InstanceRowEditorWorkingFlow": me1200InstanceRowEditorWorkingFlow,
       "me1200InstanceRowEditorProtectingFlow": me1200InstanceRowEditorProtectingFlow,
       "me1200InstanceRowEditorAction": me1200InstanceRowEditorAction,
       "me1200ConfigTable": me1200ConfigTable,
       "me1200ConfigEntry": me1200ConfigEntry,
       "me1200ConfigId": me1200ConfigId,
       "me1200ConfigDirectional": me1200ConfigDirectional,
       "me1200ConfigApsEnable": me1200ConfigApsEnable,
       "me1200ConfigRevertive": me1200ConfigRevertive,
       "me1200ConfigRestoreTimer": me1200ConfigRestoreTimer,
       "me1200ConfigHoldOffTimer": me1200ConfigHoldOffTimer,
       "me1200MepTable": me1200MepTable,
       "me1200MepEntry": me1200MepEntry,
       "me1200MepId": me1200MepId,
       "me1200MepWorkingMep": me1200MepWorkingMep,
       "me1200MepProtectingMep": me1200MepProtectingMep,
       "me1200MepApsMep": me1200MepApsMep,
       "me1200CommandTable": me1200CommandTable,
       "me1200CommandEntry": me1200CommandEntry,
       "me1200CommandId": me1200CommandId,
       "me1200CommandCommand": me1200CommandCommand,
       "me1200EpsStatus": me1200EpsStatus,
       "me1200StatusTable": me1200StatusTable,
       "me1200StatusEntry": me1200StatusEntry,
       "me1200StatusId": me1200StatusId,
       "me1200StatusProtectionState": me1200StatusProtectionState,
       "me1200StatusWorkingState": me1200StatusWorkingState,
       "me1200StatusProtectingState": me1200StatusProtectingState,
       "me1200StatusTransmittedApsRequest": me1200StatusTransmittedApsRequest,
       "me1200StatusTransmittedApsReSignal": me1200StatusTransmittedApsReSignal,
       "me1200StatusTransmittedApsBrSignal": me1200StatusTransmittedApsBrSignal,
       "me1200StatusReceivedApsRequest": me1200StatusReceivedApsRequest,
       "me1200StatusReceivedApsReSignal": me1200StatusReceivedApsReSignal,
       "me1200StatusReceivedApsBrSignal": me1200StatusReceivedApsBrSignal,
       "me1200StatusDfopPm": me1200StatusDfopPm,
       "me1200StatusDfopCm": me1200StatusDfopCm,
       "me1200StatusDfopNr": me1200StatusDfopNr,
       "me1200StatusDfopNoAps": me1200StatusDfopNoAps,
       "me1200EpsControl": me1200EpsControl,
       "me1200EpsMibConformance": me1200EpsMibConformance,
       "me1200EpsMibCompliances": me1200EpsMibCompliances,
       "me1200EpsMibCompliance": me1200EpsMibCompliance,
       "me1200EpsMibGroups": me1200EpsMibGroups,
       "me1200EpsCapabilitiesInfoGroup": me1200EpsCapabilitiesInfoGroup,
       "me1200InstanceTableInfoGroup": me1200InstanceTableInfoGroup,
       "me1200InstanceRowEditorInfoGroup": me1200InstanceRowEditorInfoGroup,
       "me1200ConfigTableInfoGroup": me1200ConfigTableInfoGroup,
       "me1200MepTableInfoGroup": me1200MepTableInfoGroup,
       "me1200CommandTableInfoGroup": me1200CommandTableInfoGroup,
       "me1200StatusTableInfoGroup": me1200StatusTableInfoGroup}
)
