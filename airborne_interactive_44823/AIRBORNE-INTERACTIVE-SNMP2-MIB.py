# SNMP MIB module (AIRBORNE-INTERACTIVE-SNMP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/airborne_interactive_44823/AIRBORNE-INTERACTIVE-SNMP2-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:16:09 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

airborne = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44823)
)
if mibBuilder.loadTexts:
    airborne.setRevisions(
        ("2015-03-19 10:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Controlstatus_ObjectIdentity = ObjectIdentity
controlstatus = _Controlstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44823, 1)
)


class _NavigatorControlStatus_Type(Integer32):
    """Custom type navigatorControlStatus based on Integer32"""
    defaultValue = 1

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
        *(("unavailable", 1),
          ("available", 2),
          ("restart", 3),
          ("faulty", 4))
    )


_NavigatorControlStatus_Type.__name__ = "Integer32"
_NavigatorControlStatus_Object = MibScalar
navigatorControlStatus = _NavigatorControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 1),
    _NavigatorControlStatus_Type()
)
navigatorControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    navigatorControlStatus.setStatus("current")
if mibBuilder.loadTexts:
    navigatorControlStatus.setUnits("enum: 1=unavailable ; 2=available ; 3=restart ; 4=faulty")
_NavigatorActiveMapUsers_Type = Integer32
_NavigatorActiveMapUsers_Object = MibScalar
navigatorActiveMapUsers = _NavigatorActiveMapUsers_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 2),
    _NavigatorActiveMapUsers_Type()
)
navigatorActiveMapUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    navigatorActiveMapUsers.setStatus("current")
_NavigatorGlobalErrorNumber_Type = Integer32
_NavigatorGlobalErrorNumber_Object = MibScalar
navigatorGlobalErrorNumber = _NavigatorGlobalErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 3),
    _NavigatorGlobalErrorNumber_Type()
)
navigatorGlobalErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    navigatorGlobalErrorNumber.setStatus("current")


class _NavigatorInstallationState_Type(Integer32):
    """Custom type navigatorInstallationState based on Integer32"""
    defaultValue = 1

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
        *(("undefined", 1),
          ("inProgress", 2),
          ("partialFailed", 3),
          ("failed", 4),
          ("success", 5))
    )


_NavigatorInstallationState_Type.__name__ = "Integer32"
_NavigatorInstallationState_Object = MibScalar
navigatorInstallationState = _NavigatorInstallationState_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 4),
    _NavigatorInstallationState_Type()
)
navigatorInstallationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    navigatorInstallationState.setStatus("current")
if mibBuilder.loadTexts:
    navigatorInstallationState.setUnits("enum: 1=undefined ; 2=In Progress ; 3=Partially Failed ; 4=failed ; 5=successful")
_NavigatorInstallationPackagesReadyStatus_Type = OctetString
_NavigatorInstallationPackagesReadyStatus_Object = MibScalar
navigatorInstallationPackagesReadyStatus = _NavigatorInstallationPackagesReadyStatus_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 5),
    _NavigatorInstallationPackagesReadyStatus_Type()
)
navigatorInstallationPackagesReadyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    navigatorInstallationPackagesReadyStatus.setStatus("current")
if mibBuilder.loadTexts:
    navigatorInstallationPackagesReadyStatus.setUnits("string: String that triggers packages ready for install")


class _NavigatorTestMode_Type(Integer32):
    """Custom type navigatorTestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NavigatorTestMode_Type.__name__ = "Integer32"
_NavigatorTestMode_Object = MibScalar
navigatorTestMode = _NavigatorTestMode_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 6),
    _NavigatorTestMode_Type()
)
navigatorTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    navigatorTestMode.setStatus("current")
if mibBuilder.loadTexts:
    navigatorTestMode.setUnits("enum: 1=disabled ; 2=enabled")


class _NavigatorFlightPhase_Type(Integer32):
    """Custom type navigatorFlightPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NavigatorFlightPhase_Type.__name__ = "Integer32"
_NavigatorFlightPhase_Object = MibScalar
navigatorFlightPhase = _NavigatorFlightPhase_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 7),
    _NavigatorFlightPhase_Type()
)
navigatorFlightPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    navigatorFlightPhase.setStatus("current")
if mibBuilder.loadTexts:
    navigatorFlightPhase.setUnits("enum: 1=off ; 2=on")


class _NavigatorMapAvailability_Type(Integer32):
    """Custom type navigatorMapAvailability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("available", 1))
    )


_NavigatorMapAvailability_Type.__name__ = "Integer32"
_NavigatorMapAvailability_Object = MibScalar
navigatorMapAvailability = _NavigatorMapAvailability_Object(
    (1, 3, 6, 1, 4, 1, 44823, 1, 8),
    _NavigatorMapAvailability_Type()
)
navigatorMapAvailability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    navigatorMapAvailability.setStatus("current")
if mibBuilder.loadTexts:
    navigatorMapAvailability.setUnits("string: Map Availability")
_LoadedContentSoftware_ObjectIdentity = ObjectIdentity
loadedContentSoftware = _LoadedContentSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44823, 2)
)
_LoadedContentNames_ObjectIdentity = ObjectIdentity
loadedContentNames = _LoadedContentNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44823, 2, 1)
)
_LoadedcontentnameNavCust_Type = OctetString
_LoadedcontentnameNavCust_Object = MibScalar
loadedcontentnameNavCust = _LoadedcontentnameNavCust_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 1, 1),
    _LoadedcontentnameNavCust_Type()
)
loadedcontentnameNavCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentnameNavCust.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentnameNavCust.setUnits("string: Content Name")
_LoadedcontentnameNavImgs_Type = OctetString
_LoadedcontentnameNavImgs_Object = MibScalar
loadedcontentnameNavImgs = _LoadedcontentnameNavImgs_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 1, 2),
    _LoadedcontentnameNavImgs_Type()
)
loadedcontentnameNavImgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentnameNavImgs.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentnameNavImgs.setUnits("string: Content Name")
_LoadedcontentnameNavFont_Type = OctetString
_LoadedcontentnameNavFont_Object = MibScalar
loadedcontentnameNavFont = _LoadedcontentnameNavFont_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 1, 3),
    _LoadedcontentnameNavFont_Type()
)
loadedcontentnameNavFont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentnameNavFont.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentnameNavFont.setUnits("string: Content Name")
_LoadedcontentnameNavData_Type = OctetString
_LoadedcontentnameNavData_Object = MibScalar
loadedcontentnameNavData = _LoadedcontentnameNavData_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 1, 4),
    _LoadedcontentnameNavData_Type()
)
loadedcontentnameNavData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentnameNavData.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentnameNavData.setUnits("string: Content Name")
_LoadedContentVersions_ObjectIdentity = ObjectIdentity
loadedContentVersions = _LoadedContentVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44823, 2, 2)
)
_LoadedcontentversionNavCust_Type = OctetString
_LoadedcontentversionNavCust_Object = MibScalar
loadedcontentversionNavCust = _LoadedcontentversionNavCust_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 2, 1),
    _LoadedcontentversionNavCust_Type()
)
loadedcontentversionNavCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentversionNavCust.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentversionNavCust.setUnits("string: Content Version")
_LoadedcontentversionNavImgs_Type = OctetString
_LoadedcontentversionNavImgs_Object = MibScalar
loadedcontentversionNavImgs = _LoadedcontentversionNavImgs_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 2, 2),
    _LoadedcontentversionNavImgs_Type()
)
loadedcontentversionNavImgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentversionNavImgs.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentversionNavImgs.setUnits("string: Content Version")
_LoadedcontentversionNavFont_Type = OctetString
_LoadedcontentversionNavFont_Object = MibScalar
loadedcontentversionNavFont = _LoadedcontentversionNavFont_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 2, 3),
    _LoadedcontentversionNavFont_Type()
)
loadedcontentversionNavFont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentversionNavFont.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentversionNavFont.setUnits("string: Content Version")
_LoadedcontentversionNavData_Type = OctetString
_LoadedcontentversionNavData_Object = MibScalar
loadedcontentversionNavData = _LoadedcontentversionNavData_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 2, 4),
    _LoadedcontentversionNavData_Type()
)
loadedcontentversionNavData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentversionNavData.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentversionNavData.setUnits("string: Content Version")
_LoadedContentState_ObjectIdentity = ObjectIdentity
loadedContentState = _LoadedContentState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44823, 2, 3)
)


class _LoadedcontentstateNavCust_Type(Integer32):
    """Custom type loadedcontentstateNavCust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("installed", 1))
    )


_LoadedcontentstateNavCust_Type.__name__ = "Integer32"
_LoadedcontentstateNavCust_Object = MibScalar
loadedcontentstateNavCust = _LoadedcontentstateNavCust_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 3, 1),
    _LoadedcontentstateNavCust_Type()
)
loadedcontentstateNavCust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentstateNavCust.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentstateNavCust.setUnits("enum: 0=Missing ; 1=Installed")


class _LoadedcontentstateNavImgs_Type(Integer32):
    """Custom type loadedcontentstateNavImgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("installed", 1))
    )


_LoadedcontentstateNavImgs_Type.__name__ = "Integer32"
_LoadedcontentstateNavImgs_Object = MibScalar
loadedcontentstateNavImgs = _LoadedcontentstateNavImgs_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 3, 2),
    _LoadedcontentstateNavImgs_Type()
)
loadedcontentstateNavImgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentstateNavImgs.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentstateNavImgs.setUnits("enum: 0=Missing ; 1=Installed")


class _LoadedcontentstateNavFont_Type(Integer32):
    """Custom type loadedcontentstateNavFont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("installed", 1))
    )


_LoadedcontentstateNavFont_Type.__name__ = "Integer32"
_LoadedcontentstateNavFont_Object = MibScalar
loadedcontentstateNavFont = _LoadedcontentstateNavFont_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 3, 3),
    _LoadedcontentstateNavFont_Type()
)
loadedcontentstateNavFont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentstateNavFont.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentstateNavFont.setUnits("enum: 0=Missing ; 1=Installed")


class _LoadedcontentstateNavData_Type(Integer32):
    """Custom type loadedcontentstateNavData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("missing", 0),
          ("installed", 1))
    )


_LoadedcontentstateNavData_Type.__name__ = "Integer32"
_LoadedcontentstateNavData_Object = MibScalar
loadedcontentstateNavData = _LoadedcontentstateNavData_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 3, 4),
    _LoadedcontentstateNavData_Type()
)
loadedcontentstateNavData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedcontentstateNavData.setStatus("current")
if mibBuilder.loadTexts:
    loadedcontentstateNavData.setUnits("enum: 0=Missing ; 1=Installed")
_LoadedSoftware_Type = OctetString
_LoadedSoftware_Object = MibScalar
loadedSoftware = _LoadedSoftware_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 4),
    _LoadedSoftware_Type()
)
loadedSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedSoftware.setStatus("current")
if mibBuilder.loadTexts:
    loadedSoftware.setUnits("string: Software Version")
_LoadedConfig_Type = OctetString
_LoadedConfig_Object = MibScalar
loadedConfig = _LoadedConfig_Object(
    (1, 3, 6, 1, 4, 1, 44823, 2, 5),
    _LoadedConfig_Type()
)
loadedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadedConfig.setStatus("current")
if mibBuilder.loadTexts:
    loadedConfig.setUnits("string: Software Version")
_NavigatorMiscStatus_ObjectIdentity = ObjectIdentity
navigatorMiscStatus = _NavigatorMiscStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44823, 3)
)
_MiscstatusDate_Type = OctetString
_MiscstatusDate_Object = MibScalar
miscstatusDate = _MiscstatusDate_Object(
    (1, 3, 6, 1, 4, 1, 44823, 3, 1),
    _MiscstatusDate_Type()
)
miscstatusDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscstatusDate.setStatus("current")
if mibBuilder.loadTexts:
    miscstatusDate.setUnits("string: System - Date")
_MiscstatusOSVersion_Type = OctetString
_MiscstatusOSVersion_Object = MibScalar
miscstatusOSVersion = _MiscstatusOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 44823, 3, 2),
    _MiscstatusOSVersion_Type()
)
miscstatusOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscstatusOSVersion.setStatus("current")
if mibBuilder.loadTexts:
    miscstatusOSVersion.setUnits("string: System - OS Version")
_MiscstatusPFISSpace_Type = Integer32
_MiscstatusPFISSpace_Object = MibScalar
miscstatusPFISSpace = _MiscstatusPFISSpace_Object(
    (1, 3, 6, 1, 4, 1, 44823, 3, 3),
    _MiscstatusPFISSpace_Type()
)
miscstatusPFISSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscstatusPFISSpace.setStatus("current")
if mibBuilder.loadTexts:
    miscstatusPFISSpace.setUnits("integer: PFIS partition space in Megabytes")
_MiscstatusContentSpace_Type = Integer32
_MiscstatusContentSpace_Object = MibScalar
miscstatusContentSpace = _MiscstatusContentSpace_Object(
    (1, 3, 6, 1, 4, 1, 44823, 3, 4),
    _MiscstatusContentSpace_Type()
)
miscstatusContentSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscstatusContentSpace.setStatus("current")
if mibBuilder.loadTexts:
    miscstatusContentSpace.setUnits("integer: Content partition space in Megabytes")


class _MiscstatusContentCorruptionState_Type(Integer32):
    """Custom type miscstatusContentCorruptionState based on Integer32"""
    defaultValue = 0

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
        *(("notcorrupt", 0),
          ("errorsleft", 1),
          ("filesystemissue", 2),
          ("notmounted", 3))
    )


_MiscstatusContentCorruptionState_Type.__name__ = "Integer32"
_MiscstatusContentCorruptionState_Object = MibScalar
miscstatusContentCorruptionState = _MiscstatusContentCorruptionState_Object(
    (1, 3, 6, 1, 4, 1, 44823, 3, 5),
    _MiscstatusContentCorruptionState_Type()
)
miscstatusContentCorruptionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscstatusContentCorruptionState.setStatus("current")
if mibBuilder.loadTexts:
    miscstatusContentCorruptionState.setUnits("enum: 0=notcorrupt ; 1=errorsleft ; 2=filesystemissue ; 3=notmounted")

# Managed Objects groups

controlstatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44823, 1, 9)
)
controlstatusGroup.setObjects(
      *(("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorControlStatus"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorActiveMapUsers"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorGlobalErrorNumber"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorInstallationState"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorInstallationPackagesReadyStatus"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorTestMode"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorFlightPhase"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "navigatorMapAvailability"))
)
if mibBuilder.loadTexts:
    controlstatusGroup.setStatus("current")

loadedContentNamesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44823, 2, 1, 5)
)
loadedContentNamesGroup.setObjects(
      *(("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentnameNavCust"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentnameNavImgs"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentnameNavFont"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentnameNavData"))
)
if mibBuilder.loadTexts:
    loadedContentNamesGroup.setStatus("current")

loadedContentVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44823, 2, 2, 5)
)
loadedContentVersionGroup.setObjects(
      *(("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentversionNavCust"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentversionNavImgs"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentversionNavFont"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentversionNavData"))
)
if mibBuilder.loadTexts:
    loadedContentVersionGroup.setStatus("current")

loadedContentStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44823, 2, 3, 5)
)
loadedContentStateGroup.setObjects(
      *(("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentstateNavCust"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentstateNavImgs"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentstateNavFont"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedcontentstateNavData"))
)
if mibBuilder.loadTexts:
    loadedContentStateGroup.setStatus("current")

loadedVersionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44823, 2, 6)
)
loadedVersionsGroup.setObjects(
      *(("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedSoftware"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "loadedConfig"))
)
if mibBuilder.loadTexts:
    loadedVersionsGroup.setStatus("current")

navigatorMiscStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 44823, 3, 6)
)
navigatorMiscStatusGroup.setObjects(
      *(("AIRBORNE-INTERACTIVE-SNMP2-MIB", "miscstatusDate"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "miscstatusOSVersion"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "miscstatusPFISSpace"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "miscstatusContentSpace"),
        ("AIRBORNE-INTERACTIVE-SNMP2-MIB", "miscstatusContentCorruptionState"))
)
if mibBuilder.loadTexts:
    navigatorMiscStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRBORNE-INTERACTIVE-SNMP2-MIB",
    **{"airborne": airborne,
       "controlstatus": controlstatus,
       "navigatorControlStatus": navigatorControlStatus,
       "navigatorActiveMapUsers": navigatorActiveMapUsers,
       "navigatorGlobalErrorNumber": navigatorGlobalErrorNumber,
       "navigatorInstallationState": navigatorInstallationState,
       "navigatorInstallationPackagesReadyStatus": navigatorInstallationPackagesReadyStatus,
       "navigatorTestMode": navigatorTestMode,
       "navigatorFlightPhase": navigatorFlightPhase,
       "navigatorMapAvailability": navigatorMapAvailability,
       "controlstatusGroup": controlstatusGroup,
       "loadedContentSoftware": loadedContentSoftware,
       "loadedContentNames": loadedContentNames,
       "loadedcontentnameNavCust": loadedcontentnameNavCust,
       "loadedcontentnameNavImgs": loadedcontentnameNavImgs,
       "loadedcontentnameNavFont": loadedcontentnameNavFont,
       "loadedcontentnameNavData": loadedcontentnameNavData,
       "loadedContentNamesGroup": loadedContentNamesGroup,
       "loadedContentVersions": loadedContentVersions,
       "loadedcontentversionNavCust": loadedcontentversionNavCust,
       "loadedcontentversionNavImgs": loadedcontentversionNavImgs,
       "loadedcontentversionNavFont": loadedcontentversionNavFont,
       "loadedcontentversionNavData": loadedcontentversionNavData,
       "loadedContentVersionGroup": loadedContentVersionGroup,
       "loadedContentState": loadedContentState,
       "loadedcontentstateNavCust": loadedcontentstateNavCust,
       "loadedcontentstateNavImgs": loadedcontentstateNavImgs,
       "loadedcontentstateNavFont": loadedcontentstateNavFont,
       "loadedcontentstateNavData": loadedcontentstateNavData,
       "loadedContentStateGroup": loadedContentStateGroup,
       "loadedSoftware": loadedSoftware,
       "loadedConfig": loadedConfig,
       "loadedVersionsGroup": loadedVersionsGroup,
       "navigatorMiscStatus": navigatorMiscStatus,
       "miscstatusDate": miscstatusDate,
       "miscstatusOSVersion": miscstatusOSVersion,
       "miscstatusPFISSpace": miscstatusPFISSpace,
       "miscstatusContentSpace": miscstatusContentSpace,
       "miscstatusContentCorruptionState": miscstatusContentCorruptionState,
       "navigatorMiscStatusGroup": navigatorMiscStatusGroup}
)
