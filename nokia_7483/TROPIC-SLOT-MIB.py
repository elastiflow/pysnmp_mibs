# SNMP MIB module (TROPIC-SLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-SLOT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(tnSlotMIB,
 tnSlotModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSlotMIB",
    "tnSlotModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(TropicAdminStateType,
 TropicOperationalCapabilityType,
 TropicOperationalStateType,
 TropicResetType,
 TropicSlotIndexType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TropicAdminStateType",
    "TropicOperationalCapabilityType",
    "TropicOperationalStateType",
    "TropicResetType",
    "TropicSlotIndexType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnSlotMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotMibModule.setRevisions(
        ("2008-03-06 12:00",
         "2008-07-25 12:00",
         "2008-09-26 12:00",
         "2008-10-16 12:00",
         "2009-06-25 12:00",
         "2010-12-09 12:00",
         "2013-05-21 12:00",
         "2013-12-06 12:00",
         "2014-02-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSlotConf_ObjectIdentity = ObjectIdentity
tnSlotConf = _TnSlotConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1)
)
_TnSlotGroups_ObjectIdentity = ObjectIdentity
tnSlotGroups = _TnSlotGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 1)
)
_TnSlotCompliances_ObjectIdentity = ObjectIdentity
tnSlotCompliances = _TnSlotCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 2)
)
_TnSlotObjs_ObjectIdentity = ObjectIdentity
tnSlotObjs = _TnSlotObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2)
)
_TnSlotBasics_ObjectIdentity = ObjectIdentity
tnSlotBasics = _TnSlotBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2)
)
_TnSlotTable_Object = MibTable
tnSlotTable = _TnSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotTable.setStatus("current")
_TnSlotEntry_Object = MibTableRow
tnSlotEntry = _TnSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1)
)
tnSlotEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSlotEntry.setStatus("current")
_TnSlotIndex_Type = TropicSlotIndexType
_TnSlotIndex_Object = MibTableColumn
tnSlotIndex = _TnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 1),
    _TnSlotIndex_Type()
)
tnSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSlotIndex.setStatus("current")
_TnSlotProgrammedType_Type = ObjectIdentifier
_TnSlotProgrammedType_Object = MibTableColumn
tnSlotProgrammedType = _TnSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 2),
    _TnSlotProgrammedType_Type()
)
tnSlotProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotProgrammedType.setStatus("current")
_TnSlotPresentType_Type = ObjectIdentifier
_TnSlotPresentType_Object = MibTableColumn
tnSlotPresentType = _TnSlotPresentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 3),
    _TnSlotPresentType_Type()
)
tnSlotPresentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotPresentType.setStatus("current")


class _TnSlotAdminState_Type(TropicAdminStateType):
    """Custom type tnSlotAdminState based on TropicAdminStateType"""
    defaultValue = 2


_TnSlotAdminState_Type.__name__ = "TropicAdminStateType"
_TnSlotAdminState_Object = MibTableColumn
tnSlotAdminState = _TnSlotAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 4),
    _TnSlotAdminState_Type()
)
tnSlotAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotAdminState.setStatus("current")


class _TnSlotOperationalState_Type(TropicOperationalStateType):
    """Custom type tnSlotOperationalState based on TropicOperationalStateType"""
    defaultValue = 2


_TnSlotOperationalState_Type.__name__ = "TropicOperationalStateType"
_TnSlotOperationalState_Object = MibTableColumn
tnSlotOperationalState = _TnSlotOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 5),
    _TnSlotOperationalState_Type()
)
tnSlotOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotOperationalState.setStatus("current")


class _TnSlotOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnSlotOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnSlotOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnSlotOperationalCapability_Object = MibTableColumn
tnSlotOperationalCapability = _TnSlotOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 6),
    _TnSlotOperationalCapability_Type()
)
tnSlotOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotOperationalCapability.setStatus("current")


class _TnSlotStateQualifier_Type(TropicStateQualifierType):
    """Custom type tnSlotStateQualifier based on TropicStateQualifierType"""
    defaultBinValue = "0000001"


_TnSlotStateQualifier_Type.__name__ = "TropicStateQualifierType"
_TnSlotStateQualifier_Object = MibTableColumn
tnSlotStateQualifier = _TnSlotStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 7),
    _TnSlotStateQualifier_Type()
)
tnSlotStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotStateQualifier.setStatus("current")
_TnSlotResetTable_Object = MibTable
tnSlotResetTable = _TnSlotResetTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlotResetTable.setStatus("current")
_TnSlotResetEntry_Object = MibTableRow
tnSlotResetEntry = _TnSlotResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1)
)
tnSlotResetEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSlotResetEntry.setStatus("current")


class _TnSlotReset_Type(TropicResetType):
    """Custom type tnSlotReset based on TropicResetType"""
    defaultValue = 1


_TnSlotReset_Type.__name__ = "TropicResetType"
_TnSlotReset_Object = MibTableColumn
tnSlotReset = _TnSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1, 1),
    _TnSlotReset_Type()
)
tnSlotReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSlotReset.setStatus("current")


class _TnSlotResetReason_Type(Integer32):
    """Custom type tnSlotResetReason based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("powerReset", 1),
          ("userReset", 2),
          ("ccActivitySwitch", 3),
          ("softwareTrap", 4),
          ("watchdog", 5),
          ("alarmPanelStartupError", 6),
          ("softwareStartupError", 7),
          ("cardCommsError", 8),
          ("softwareAssert", 9),
          ("subcomponentSoftwareBadCrc", 10),
          ("databaseError", 11),
          ("seepError", 12),
          ("subcomponentReset", 13),
          ("warmReset", 14),
          ("coldReset", 15),
          ("userBootReset", 16),
          ("ntpNotResponding", 17),
          ("cardTookNewShelfSerialNumber", 18),
          ("subcomponentStartupError", 19),
          ("inBootJumperSet", 20),
          ("inBootSeep", 21),
          ("inBootBank0Corrupt", 22),
          ("inBootBank1Corrupt", 23),
          ("inBootAppLoadCorrupt", 24),
          ("inBootCrashCountExceeded", 25),
          ("subcomponentWatchdog", 26),
          ("criticalDatabaseStartupError", 27),
          ("redundancyError", 28),
          ("controlNetworkError", 29),
          ("shelfSerialNumberChanged", 30),
          ("swlDiskTransferFailure", 31),
          ("bitSyncCommsFailure", 32),
          ("diskReformatted", 33),
          ("diskMissing", 34),
          ("diskIoError", 35),
          ("cpuStarvation", 36),
          ("uiStarvation", 37),
          ("sonetSdhModeMismatch", 38),
          ("universalCardTypeMismatch", 39),
          ("boardMgrPowerCycle", 40),
          ("boardMgrProcessorReset", 41),
          ("ecProcessExit", 42),
          ("eventNvramAccessFailure", 43),
          ("userCCActivitySwitch", 44))
    )


_TnSlotResetReason_Type.__name__ = "Integer32"
_TnSlotResetReason_Object = MibTableColumn
tnSlotResetReason = _TnSlotResetReason_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1, 2),
    _TnSlotResetReason_Type()
)
tnSlotResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotResetReason.setStatus("current")


class _TnSlotResetTime_Type(Unsigned32):
    """Custom type tnSlotResetTime based on Unsigned32"""
    defaultValue = 0


_TnSlotResetTime_Type.__name__ = "Unsigned32"
_TnSlotResetTime_Object = MibTableColumn
tnSlotResetTime = _TnSlotResetTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 2, 1, 3),
    _TnSlotResetTime_Type()
)
tnSlotResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSlotResetTime.setStatus("current")

# Managed Objects groups

tnSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 1, 1)
)
tnSlotGroup.setObjects(
      *(("TROPIC-SLOT-MIB", "tnSlotProgrammedType"),
        ("TROPIC-SLOT-MIB", "tnSlotPresentType"),
        ("TROPIC-SLOT-MIB", "tnSlotAdminState"),
        ("TROPIC-SLOT-MIB", "tnSlotOperationalState"),
        ("TROPIC-SLOT-MIB", "tnSlotOperationalCapability"),
        ("TROPIC-SLOT-MIB", "tnSlotStateQualifier"))
)
if mibBuilder.loadTexts:
    tnSlotGroup.setStatus("current")

tnSlotResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 1, 2)
)
tnSlotResetGroup.setObjects(
      *(("TROPIC-SLOT-MIB", "tnSlotReset"),
        ("TROPIC-SLOT-MIB", "tnSlotResetReason"),
        ("TROPIC-SLOT-MIB", "tnSlotResetTime"))
)
if mibBuilder.loadTexts:
    tnSlotResetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSlotCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 1, 2, 1)
)
tnSlotCompliance.setObjects(
      *(("TROPIC-SLOT-MIB", "tnSlotGroup"),
        ("TROPIC-SLOT-MIB", "tnSlotResetGroup"))
)
if mibBuilder.loadTexts:
    tnSlotCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SLOT-MIB",
    **{"tnSlotMibModule": tnSlotMibModule,
       "tnSlotConf": tnSlotConf,
       "tnSlotGroups": tnSlotGroups,
       "tnSlotGroup": tnSlotGroup,
       "tnSlotResetGroup": tnSlotResetGroup,
       "tnSlotCompliances": tnSlotCompliances,
       "tnSlotCompliance": tnSlotCompliance,
       "tnSlotObjs": tnSlotObjs,
       "tnSlotBasics": tnSlotBasics,
       "tnSlotTable": tnSlotTable,
       "tnSlotEntry": tnSlotEntry,
       "tnSlotIndex": tnSlotIndex,
       "tnSlotProgrammedType": tnSlotProgrammedType,
       "tnSlotPresentType": tnSlotPresentType,
       "tnSlotAdminState": tnSlotAdminState,
       "tnSlotOperationalState": tnSlotOperationalState,
       "tnSlotOperationalCapability": tnSlotOperationalCapability,
       "tnSlotStateQualifier": tnSlotStateQualifier,
       "tnSlotResetTable": tnSlotResetTable,
       "tnSlotResetEntry": tnSlotResetEntry,
       "tnSlotReset": tnSlotReset,
       "tnSlotResetReason": tnSlotResetReason,
       "tnSlotResetTime": tnSlotResetTime}
)
