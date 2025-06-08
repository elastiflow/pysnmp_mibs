# SNMP MIB module (PEAKDXXH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKDXXH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(FaultType,
 RedundancyModeType,
 YesNoType,
 nsConverters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "FaultType",
    "RedundancyModeType",
    "YesNoType",
    "nsConverters")

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

peakDXXHConverterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2)
)
if mibBuilder.loadTexts:
    peakDXXHConverterModule.setRevisions(
        ("2015-09-15 09:00",
         "2014-09-09 12:00",
         "2013-11-21 12:00",
         "2013-09-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ExternalReferenceType(TextualConvention, Integer32):
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
        *(("notPresent", 1),
          ("locked", 2),
          ("unlocked", 3))
    )



class ModuleStateType(TextualConvention, Integer32):
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
        *(("missing", 1),
          ("warmup", 2),
          ("present", 3))
    )



class PSUPowerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPowered", 1),
          ("powered", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DxxhCModuleTable_Object = MibTable
dxxhCModuleTable = _DxxhCModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    dxxhCModuleTable.setStatus("current")
_DxxhCModuleTableEntry_Object = MibTableRow
dxxhCModuleTableEntry = _DxxhCModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1)
)
dxxhCModuleTableEntry.setIndexNames(
    (0, "PEAKDXXH-MIB", "dxxhCModuleIndex"),
)
if mibBuilder.loadTexts:
    dxxhCModuleTableEntry.setStatus("current")


class _DxxhCModuleIndex_Type(Integer32):
    """Custom type dxxhCModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DxxhCModuleIndex_Type.__name__ = "Integer32"
_DxxhCModuleIndex_Object = MibTableColumn
dxxhCModuleIndex = _DxxhCModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 1),
    _DxxhCModuleIndex_Type()
)
dxxhCModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxxhCModuleIndex.setStatus("current")
_DxxhCModuleName_Type = OctetString
_DxxhCModuleName_Object = MibTableColumn
dxxhCModuleName = _DxxhCModuleName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 2),
    _DxxhCModuleName_Type()
)
dxxhCModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCModuleName.setStatus("current")
_DxxhCModuleState_Type = ModuleStateType
_DxxhCModuleState_Object = MibTableColumn
dxxhCModuleState = _DxxhCModuleState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 3),
    _DxxhCModuleState_Type()
)
dxxhCModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCModuleState.setStatus("current")
_DxxhCModuleAttenuation_Type = OctetString
_DxxhCModuleAttenuation_Object = MibTableColumn
dxxhCModuleAttenuation = _DxxhCModuleAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 4),
    _DxxhCModuleAttenuation_Type()
)
dxxhCModuleAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxxhCModuleAttenuation.setStatus("current")
_DxxhCModuleExternalReference_Type = ExternalReferenceType
_DxxhCModuleExternalReference_Object = MibTableColumn
dxxhCModuleExternalReference = _DxxhCModuleExternalReference_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 5),
    _DxxhCModuleExternalReference_Type()
)
dxxhCModuleExternalReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCModuleExternalReference.setStatus("current")
_DxxhCModuleSummaryAlarm_Type = FaultType
_DxxhCModuleSummaryAlarm_Object = MibTableColumn
dxxhCModuleSummaryAlarm = _DxxhCModuleSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 19),
    _DxxhCModuleSummaryAlarm_Type()
)
dxxhCModuleSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCModuleSummaryAlarm.setStatus("current")
_DxxhCModuleOKSince_Type = OctetString
_DxxhCModuleOKSince_Object = MibTableColumn
dxxhCModuleOKSince = _DxxhCModuleOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 1, 1, 20),
    _DxxhCModuleOKSince_Type()
)
dxxhCModuleOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCModuleOKSince.setStatus("current")
_DxxhCPSUTable_Object = MibTable
dxxhCPSUTable = _DxxhCPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 2)
)
if mibBuilder.loadTexts:
    dxxhCPSUTable.setStatus("current")
_DxxhCPSUTableEntry_Object = MibTableRow
dxxhCPSUTableEntry = _DxxhCPSUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 2, 1)
)
dxxhCPSUTableEntry.setIndexNames(
    (0, "PEAKDXXH-MIB", "dxxhCPSUIndex"),
)
if mibBuilder.loadTexts:
    dxxhCPSUTableEntry.setStatus("current")


class _DxxhCPSUIndex_Type(Integer32):
    """Custom type dxxhCPSUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DxxhCPSUIndex_Type.__name__ = "Integer32"
_DxxhCPSUIndex_Object = MibTableColumn
dxxhCPSUIndex = _DxxhCPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 2, 1, 1),
    _DxxhCPSUIndex_Type()
)
dxxhCPSUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxxhCPSUIndex.setStatus("current")
_DxxhCPSUPoweredState_Type = PSUPowerType
_DxxhCPSUPoweredState_Object = MibTableColumn
dxxhCPSUPoweredState = _DxxhCPSUPoweredState_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 2, 1, 2),
    _DxxhCPSUPoweredState_Type()
)
dxxhCPSUPoweredState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCPSUPoweredState.setStatus("current")
_DxxhCPSUSummaryAlarm_Type = FaultType
_DxxhCPSUSummaryAlarm_Object = MibTableColumn
dxxhCPSUSummaryAlarm = _DxxhCPSUSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 2, 1, 19),
    _DxxhCPSUSummaryAlarm_Type()
)
dxxhCPSUSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCPSUSummaryAlarm.setStatus("current")
_DxxhCPSUOKSince_Type = OctetString
_DxxhCPSUOKSince_Object = MibTableColumn
dxxhCPSUOKSince = _DxxhCPSUOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 2, 1, 20),
    _DxxhCPSUOKSince_Type()
)
dxxhCPSUOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhCPSUOKSince.setStatus("current")
_DxxhRedundancy_ObjectIdentity = ObjectIdentity
dxxhRedundancy = _DxxhRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 3)
)
_DxxhRedundancyMode_Type = RedundancyModeType
_DxxhRedundancyMode_Object = MibScalar
dxxhRedundancyMode = _DxxhRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 3, 1),
    _DxxhRedundancyMode_Type()
)
dxxhRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxxhRedundancyMode.setStatus("current")
_DxxhRedundancyCopySettings_Type = YesNoType
_DxxhRedundancyCopySettings_Object = MibScalar
dxxhRedundancyCopySettings = _DxxhRedundancyCopySettings_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 3, 2),
    _DxxhRedundancyCopySettings_Type()
)
dxxhRedundancyCopySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxxhRedundancyCopySettings.setStatus("current")


class _DxxhRedundancyActualModuleOnline_Type(OctetString):
    """Custom type dxxhRedundancyActualModuleOnline based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DxxhRedundancyActualModuleOnline_Type.__name__ = "OctetString"
_DxxhRedundancyActualModuleOnline_Object = MibScalar
dxxhRedundancyActualModuleOnline = _DxxhRedundancyActualModuleOnline_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 3, 3),
    _DxxhRedundancyActualModuleOnline_Type()
)
dxxhRedundancyActualModuleOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxxhRedundancyActualModuleOnline.setStatus("current")


class _DxxhRedundancyWantedModuleOnline_Type(OctetString):
    """Custom type dxxhRedundancyWantedModuleOnline based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DxxhRedundancyWantedModuleOnline_Type.__name__ = "OctetString"
_DxxhRedundancyWantedModuleOnline_Object = MibScalar
dxxhRedundancyWantedModuleOnline = _DxxhRedundancyWantedModuleOnline_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 3, 4),
    _DxxhRedundancyWantedModuleOnline_Type()
)
dxxhRedundancyWantedModuleOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxxhRedundancyWantedModuleOnline.setStatus("current")
_DxxhConvGroups_ObjectIdentity = ObjectIdentity
dxxhConvGroups = _DxxhConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 110)
)
_DxxhConvConformance_ObjectIdentity = ObjectIdentity
dxxhConvConformance = _DxxhConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 111)
)

# Managed Objects groups

dxxhCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 110, 1)
)
dxxhCNFReqGrp.setObjects(
      *(("PEAKDXXH-MIB", "dxxhCModuleAttenuation"),
        ("PEAKDXXH-MIB", "dxxhCModuleState"),
        ("PEAKDXXH-MIB", "dxxhCModuleName"),
        ("PEAKDXXH-MIB", "dxxhCModuleSummaryAlarm"),
        ("PEAKDXXH-MIB", "dxxhCModuleExternalReference"),
        ("PEAKDXXH-MIB", "dxxhCModuleOKSince"),
        ("PEAKDXXH-MIB", "dxxhCPSUPoweredState"),
        ("PEAKDXXH-MIB", "dxxhCPSUSummaryAlarm"),
        ("PEAKDXXH-MIB", "dxxhCPSUOKSince"))
)
if mibBuilder.loadTexts:
    dxxhCNFReqGrp.setStatus("current")

dxxhCNFRedundancyGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 110, 5)
)
dxxhCNFRedundancyGrp.setObjects(
      *(("PEAKDXXH-MIB", "dxxhRedundancyMode"),
        ("PEAKDXXH-MIB", "dxxhRedundancyCopySettings"),
        ("PEAKDXXH-MIB", "dxxhRedundancyActualModuleOnline"),
        ("PEAKDXXH-MIB", "dxxhRedundancyWantedModuleOnline"))
)
if mibBuilder.loadTexts:
    dxxhCNFRedundancyGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dxxhCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 2, 111, 1)
)
dxxhCNFCompliance.setObjects(
      *(("PEAKDXXH-MIB", "dxxhCNFReqGrp"),
        ("PEAKDXXH-MIB", "dxxhCNFRedundancyGrp"))
)
if mibBuilder.loadTexts:
    dxxhCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKDXXH-MIB",
    **{"ExternalReferenceType": ExternalReferenceType,
       "ModuleStateType": ModuleStateType,
       "PSUPowerType": PSUPowerType,
       "peakDXXHConverterModule": peakDXXHConverterModule,
       "dxxhCModuleTable": dxxhCModuleTable,
       "dxxhCModuleTableEntry": dxxhCModuleTableEntry,
       "dxxhCModuleIndex": dxxhCModuleIndex,
       "dxxhCModuleName": dxxhCModuleName,
       "dxxhCModuleState": dxxhCModuleState,
       "dxxhCModuleAttenuation": dxxhCModuleAttenuation,
       "dxxhCModuleExternalReference": dxxhCModuleExternalReference,
       "dxxhCModuleSummaryAlarm": dxxhCModuleSummaryAlarm,
       "dxxhCModuleOKSince": dxxhCModuleOKSince,
       "dxxhCPSUTable": dxxhCPSUTable,
       "dxxhCPSUTableEntry": dxxhCPSUTableEntry,
       "dxxhCPSUIndex": dxxhCPSUIndex,
       "dxxhCPSUPoweredState": dxxhCPSUPoweredState,
       "dxxhCPSUSummaryAlarm": dxxhCPSUSummaryAlarm,
       "dxxhCPSUOKSince": dxxhCPSUOKSince,
       "dxxhRedundancy": dxxhRedundancy,
       "dxxhRedundancyMode": dxxhRedundancyMode,
       "dxxhRedundancyCopySettings": dxxhRedundancyCopySettings,
       "dxxhRedundancyActualModuleOnline": dxxhRedundancyActualModuleOnline,
       "dxxhRedundancyWantedModuleOnline": dxxhRedundancyWantedModuleOnline,
       "dxxhConvGroups": dxxhConvGroups,
       "dxxhCNFReqGrp": dxxhCNFReqGrp,
       "dxxhCNFRedundancyGrp": dxxhCNFRedundancyGrp,
       "dxxhConvConformance": dxxhConvConformance,
       "dxxhCNFCompliance": dxxhCNFCompliance}
)
