# SNMP MIB module (EKINOPS-PMC2002-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PMC2002-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:46 2025
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

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

modulepmc2002 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52)
)
if mibBuilder.loadTexts:
    modulepmc2002.setRevisions(
        ("2011-01-04 00:00",
         "2011-10-14 00:00",
         "2012-07-03 00:00",
         "2013-04-03 00:00",
         "2014-03-26 00:00",
         "2014-11-18 00:00",
         "2015-02-20 00:00",
         "2016-05-24 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmc2002OtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Pmc2002OtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Pmc2002AdjustValue(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Pmc2002OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pmc2002DccMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dccNo", 0),
          ("dcctermLine1", 1),
          ("dcctermLine2", 2),
          ("dcctermLines12", 3),
          ("dccmaster", 4),
          ("dccslaveLine12", 7))
    )



class Pmc2002Mode(TextualConvention, Integer32):
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
        *(("modedual", 0),
          ("modeprotect", 1),
          ("moderegen", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pmc2002alarms_ObjectIdentity = ObjectIdentity
pmc2002alarms = _Pmc2002alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2)
)
_Pmc2002AlmOther_ObjectIdentity = ObjectIdentity
pmc2002AlmOther = _Pmc2002AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1)
)
_Pmc2002AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmc2002AlmOtherNurg = _Pmc2002AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1)
)
_Pmc2002AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmc2002AlmsynthAlm2 = _Pmc2002AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1, 2)
)
_Pmc2002AlmConfTableSave_Type = EkiOnOff
_Pmc2002AlmConfTableSave_Object = MibScalar
pmc2002AlmConfTableSave = _Pmc2002AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1, 2, 1),
    _Pmc2002AlmConfTableSave_Type()
)
pmc2002AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmConfTableSave.setStatus("current")
_Pmc2002AlmInvUpload_Type = EkiOnOff
_Pmc2002AlmInvUpload_Object = MibScalar
pmc2002AlmInvUpload = _Pmc2002AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1, 2, 2),
    _Pmc2002AlmInvUpload_Type()
)
pmc2002AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmInvUpload.setStatus("current")
_Pmc2002AlmConfTableLoad_Type = EkiOnOff
_Pmc2002AlmConfTableLoad_Object = MibScalar
pmc2002AlmConfTableLoad = _Pmc2002AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1, 2, 3),
    _Pmc2002AlmConfTableLoad_Type()
)
pmc2002AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmConfTableLoad.setStatus("current")
_Pmc2002AlmCorrelatOff_Type = EkiOnOff
_Pmc2002AlmCorrelatOff_Object = MibScalar
pmc2002AlmCorrelatOff = _Pmc2002AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1, 2, 4),
    _Pmc2002AlmCorrelatOff_Type()
)
pmc2002AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmCorrelatOff.setStatus("current")
_Pmc2002AlmMaintenanceOn_Type = EkiOnOff
_Pmc2002AlmMaintenanceOn_Object = MibScalar
pmc2002AlmMaintenanceOn = _Pmc2002AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 1, 2, 5),
    _Pmc2002AlmMaintenanceOn_Type()
)
pmc2002AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmMaintenanceOn.setStatus("current")
_Pmc2002AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmc2002AlmOtherUrg = _Pmc2002AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2)
)
_Pmc2002AlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pmc2002AlmmodInitFailLevel2 = _Pmc2002AlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 194)
)
_Pmc2002AlmLedFail_Type = EkiOnOff
_Pmc2002AlmLedFail_Object = MibScalar
pmc2002AlmLedFail = _Pmc2002AlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 194, 1),
    _Pmc2002AlmLedFail_Type()
)
pmc2002AlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLedFail.setStatus("current")
_Pmc2002AlmNextColdBootForced_Type = EkiOnOff
_Pmc2002AlmNextColdBootForced_Object = MibScalar
pmc2002AlmNextColdBootForced = _Pmc2002AlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 194, 2),
    _Pmc2002AlmNextColdBootForced_Type()
)
pmc2002AlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmNextColdBootForced.setStatus("current")
_Pmc2002AlmBootUndone_Type = EkiOnOff
_Pmc2002AlmBootUndone_Object = MibScalar
pmc2002AlmBootUndone = _Pmc2002AlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 194, 3),
    _Pmc2002AlmBootUndone_Type()
)
pmc2002AlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmBootUndone.setStatus("current")
_Pmc2002AlmResetHwInitFail_Type = EkiOnOff
_Pmc2002AlmResetHwInitFail_Object = MibScalar
pmc2002AlmResetHwInitFail = _Pmc2002AlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 194, 4),
    _Pmc2002AlmResetHwInitFail_Type()
)
pmc2002AlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmResetHwInitFail.setStatus("current")
_Pmc2002AlmSwInitFail_Type = EkiOnOff
_Pmc2002AlmSwInitFail_Object = MibScalar
pmc2002AlmSwInitFail = _Pmc2002AlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 194, 5),
    _Pmc2002AlmSwInitFail_Type()
)
pmc2002AlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmSwInitFail.setStatus("current")
_Pmc2002AlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pmc2002AlmmodInitFailLevel3 = _Pmc2002AlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195)
)
_Pmc2002AlmGwIdentFail_Type = EkiOnOff
_Pmc2002AlmGwIdentFail_Object = MibScalar
pmc2002AlmGwIdentFail = _Pmc2002AlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 1),
    _Pmc2002AlmGwIdentFail_Type()
)
pmc2002AlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmGwIdentFail.setStatus("current")
_Pmc2002AlmObmTypeReadFail_Type = EkiOnOff
_Pmc2002AlmObmTypeReadFail_Object = MibScalar
pmc2002AlmObmTypeReadFail = _Pmc2002AlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 2),
    _Pmc2002AlmObmTypeReadFail_Type()
)
pmc2002AlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmObmTypeReadFail.setStatus("current")
_Pmc2002AlmInitModuleFail_Type = EkiOnOff
_Pmc2002AlmInitModuleFail_Object = MibScalar
pmc2002AlmInitModuleFail = _Pmc2002AlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 3),
    _Pmc2002AlmInitModuleFail_Type()
)
pmc2002AlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmInitModuleFail.setStatus("current")
_Pmc2002AlmXfp1InitFail_Type = EkiOnOff
_Pmc2002AlmXfp1InitFail_Object = MibScalar
pmc2002AlmXfp1InitFail = _Pmc2002AlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 5),
    _Pmc2002AlmXfp1InitFail_Type()
)
pmc2002AlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmXfp1InitFail.setStatus("current")
_Pmc2002AlmXfp2InitFail_Type = EkiOnOff
_Pmc2002AlmXfp2InitFail_Object = MibScalar
pmc2002AlmXfp2InitFail = _Pmc2002AlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 6),
    _Pmc2002AlmXfp2InitFail_Type()
)
pmc2002AlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmXfp2InitFail.setStatus("current")
_Pmc2002AlmLine1InitFail_Type = EkiOnOff
_Pmc2002AlmLine1InitFail_Object = MibScalar
pmc2002AlmLine1InitFail = _Pmc2002AlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 7),
    _Pmc2002AlmLine1InitFail_Type()
)
pmc2002AlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLine1InitFail.setStatus("current")
_Pmc2002AlmClient1InitFail_Type = EkiOnOff
_Pmc2002AlmClient1InitFail_Object = MibScalar
pmc2002AlmClient1InitFail = _Pmc2002AlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 2, 195, 9),
    _Pmc2002AlmClient1InitFail_Type()
)
pmc2002AlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClient1InitFail.setStatus("current")
_Pmc2002AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmc2002AlmOtherCrit = _Pmc2002AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3)
)
_Pmc2002AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmc2002AlmsynthAlm0 = _Pmc2002AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3, 0)
)
_Pmc2002AlmLineFailSynth_Type = EkiOnOff
_Pmc2002AlmLineFailSynth_Object = MibScalar
pmc2002AlmLineFailSynth = _Pmc2002AlmLineFailSynth_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3, 0, 1),
    _Pmc2002AlmLineFailSynth_Type()
)
pmc2002AlmLineFailSynth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineFailSynth.setStatus("current")
_Pmc2002AlmLineLosSynth_Type = EkiOnOff
_Pmc2002AlmLineLosSynth_Object = MibScalar
pmc2002AlmLineLosSynth = _Pmc2002AlmLineLosSynth_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3, 0, 2),
    _Pmc2002AlmLineLosSynth_Type()
)
pmc2002AlmLineLosSynth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineLosSynth.setStatus("current")
_Pmc2002AlmModGlobFail_Type = EkiOnOff
_Pmc2002AlmModGlobFail_Object = MibScalar
pmc2002AlmModGlobFail = _Pmc2002AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3, 0, 9),
    _Pmc2002AlmModGlobFail_Type()
)
pmc2002AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmModGlobFail.setStatus("current")
_Pmc2002AlmDefFuseA_Type = EkiOnOff
_Pmc2002AlmDefFuseA_Object = MibScalar
pmc2002AlmDefFuseA = _Pmc2002AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3, 0, 15),
    _Pmc2002AlmDefFuseA_Type()
)
pmc2002AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmDefFuseA.setStatus("current")
_Pmc2002AlmDefFuseB_Type = EkiOnOff
_Pmc2002AlmDefFuseB_Object = MibScalar
pmc2002AlmDefFuseB = _Pmc2002AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 1, 3, 0, 16),
    _Pmc2002AlmDefFuseB_Type()
)
pmc2002AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmDefFuseB.setStatus("current")
_Pmc2002AlmClient_ObjectIdentity = ObjectIdentity
pmc2002AlmClient = _Pmc2002AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2)
)
_Pmc2002AlmClientNurg_ObjectIdentity = ObjectIdentity
pmc2002AlmClientNurg = _Pmc2002AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1)
)
_Pmc2002AlmclientXfpWarningsTable_Object = MibTable
pmc2002AlmclientXfpWarningsTable = _Pmc2002AlmclientXfpWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpWarningsTable.setStatus("current")
_Pmc2002AlmclientXfpWarningsEntry_Object = MibTableRow
pmc2002AlmclientXfpWarningsEntry = _Pmc2002AlmclientXfpWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1)
)
pmc2002AlmclientXfpWarningsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmclientXfpWarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpWarningsEntry.setStatus("current")


class _Pmc2002AlmclientXfpWarningsIndex_Type(Integer32):
    """Custom type pmc2002AlmclientXfpWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmclientXfpWarningsIndex_Type.__name__ = "Integer32"
_Pmc2002AlmclientXfpWarningsIndex_Object = MibTableColumn
pmc2002AlmclientXfpWarningsIndex = _Pmc2002AlmclientXfpWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 1),
    _Pmc2002AlmclientXfpWarningsIndex_Type()
)
pmc2002AlmclientXfpWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpWarningsIndex.setStatus("current")
_Pmc2002AlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pmc2002AlmClientTxPowerLowWarningPortn = _Pmc2002AlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 2),
    _Pmc2002AlmClientTxPowerLowWarningPortn_Type()
)
pmc2002AlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxPowerLowWarningPortn.setStatus("current")
_Pmc2002AlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pmc2002AlmClientTxPowerHighWarningPortn = _Pmc2002AlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 3),
    _Pmc2002AlmClientTxPowerHighWarningPortn_Type()
)
pmc2002AlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxPowerHighWarningPortn.setStatus("current")
_Pmc2002AlmClientTxBiasLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientTxBiasLowWarningPortn_Object = MibTableColumn
pmc2002AlmClientTxBiasLowWarningPortn = _Pmc2002AlmClientTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 4),
    _Pmc2002AlmClientTxBiasLowWarningPortn_Type()
)
pmc2002AlmClientTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxBiasLowWarningPortn.setStatus("current")
_Pmc2002AlmClientTxBiasHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientTxBiasHighWarningPortn_Object = MibTableColumn
pmc2002AlmClientTxBiasHighWarningPortn = _Pmc2002AlmClientTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 5),
    _Pmc2002AlmClientTxBiasHighWarningPortn_Type()
)
pmc2002AlmClientTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxBiasHighWarningPortn.setStatus("current")
_Pmc2002AlmClientTempLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientTempLowWarningPortn_Object = MibTableColumn
pmc2002AlmClientTempLowWarningPortn = _Pmc2002AlmClientTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 8),
    _Pmc2002AlmClientTempLowWarningPortn_Type()
)
pmc2002AlmClientTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTempLowWarningPortn.setStatus("current")
_Pmc2002AlmClientTempHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientTempHighWarningPortn_Object = MibTableColumn
pmc2002AlmClientTempHighWarningPortn = _Pmc2002AlmClientTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 9),
    _Pmc2002AlmClientTempHighWarningPortn_Type()
)
pmc2002AlmClientTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTempHighWarningPortn.setStatus("current")
_Pmc2002AlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pmc2002AlmClientRxPowerLowWarningPortn = _Pmc2002AlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 16),
    _Pmc2002AlmClientRxPowerLowWarningPortn_Type()
)
pmc2002AlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientRxPowerLowWarningPortn.setStatus("current")
_Pmc2002AlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pmc2002AlmClientRxPowerHighWarningPortn = _Pmc2002AlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 1, 48, 1, 17),
    _Pmc2002AlmClientRxPowerHighWarningPortn_Type()
)
pmc2002AlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientRxPowerHighWarningPortn.setStatus("current")
_Pmc2002AlmClientUrg_ObjectIdentity = ObjectIdentity
pmc2002AlmClientUrg = _Pmc2002AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2)
)
_Pmc2002AlmclientXfpAlarm1Table_Object = MibTable
pmc2002AlmclientXfpAlarm1Table = _Pmc2002AlmclientXfpAlarm1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpAlarm1Table.setStatus("current")
_Pmc2002AlmclientXfpAlarm1Entry_Object = MibTableRow
pmc2002AlmclientXfpAlarm1Entry = _Pmc2002AlmclientXfpAlarm1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1)
)
pmc2002AlmclientXfpAlarm1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmclientXfpAlarm1Index"),
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpAlarm1Entry.setStatus("current")


class _Pmc2002AlmclientXfpAlarm1Index_Type(Integer32):
    """Custom type pmc2002AlmclientXfpAlarm1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmclientXfpAlarm1Index_Type.__name__ = "Integer32"
_Pmc2002AlmclientXfpAlarm1Index_Object = MibTableColumn
pmc2002AlmclientXfpAlarm1Index = _Pmc2002AlmclientXfpAlarm1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 1),
    _Pmc2002AlmclientXfpAlarm1Index_Type()
)
pmc2002AlmclientXfpAlarm1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpAlarm1Index.setStatus("current")
_Pmc2002AlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientTxPowerLowAlarmPortn = _Pmc2002AlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 2),
    _Pmc2002AlmClientTxPowerLowAlarmPortn_Type()
)
pmc2002AlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pmc2002AlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientTxPowerHighAlarmPortn = _Pmc2002AlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 3),
    _Pmc2002AlmClientTxPowerHighAlarmPortn_Type()
)
pmc2002AlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pmc2002AlmClientTxBiasLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientTxBiasLowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientTxBiasLowAlarmPortn = _Pmc2002AlmClientTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 4),
    _Pmc2002AlmClientTxBiasLowAlarmPortn_Type()
)
pmc2002AlmClientTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxBiasLowAlarmPortn.setStatus("current")
_Pmc2002AlmClientTxBiasHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientTxBiasHighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientTxBiasHighAlarmPortn = _Pmc2002AlmClientTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 5),
    _Pmc2002AlmClientTxBiasHighAlarmPortn_Type()
)
pmc2002AlmClientTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxBiasHighAlarmPortn.setStatus("current")
_Pmc2002AlmClientTempLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientTempLowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientTempLowAlarmPortn = _Pmc2002AlmClientTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 8),
    _Pmc2002AlmClientTempLowAlarmPortn_Type()
)
pmc2002AlmClientTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTempLowAlarmPortn.setStatus("current")
_Pmc2002AlmClientTempHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientTempHighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientTempHighAlarmPortn = _Pmc2002AlmClientTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 9),
    _Pmc2002AlmClientTempHighAlarmPortn_Type()
)
pmc2002AlmClientTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTempHighAlarmPortn.setStatus("current")
_Pmc2002AlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientRxPowerLowAlarmPortn = _Pmc2002AlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 16),
    _Pmc2002AlmClientRxPowerLowAlarmPortn_Type()
)
pmc2002AlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pmc2002AlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientRxPowerHighAlarmPortn = _Pmc2002AlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 32, 1, 17),
    _Pmc2002AlmClientRxPowerHighAlarmPortn_Type()
)
pmc2002AlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pmc2002AlmclientXfpSupplyAlarmTable_Object = MibTable
pmc2002AlmclientXfpSupplyAlarmTable = _Pmc2002AlmclientXfpSupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64)
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpSupplyAlarmTable.setStatus("current")
_Pmc2002AlmclientXfpSupplyAlarmEntry_Object = MibTableRow
pmc2002AlmclientXfpSupplyAlarmEntry = _Pmc2002AlmclientXfpSupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1)
)
pmc2002AlmclientXfpSupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmclientXfpSupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpSupplyAlarmEntry.setStatus("current")


class _Pmc2002AlmclientXfpSupplyAlarmIndex_Type(Integer32):
    """Custom type pmc2002AlmclientXfpSupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmclientXfpSupplyAlarmIndex_Type.__name__ = "Integer32"
_Pmc2002AlmclientXfpSupplyAlarmIndex_Object = MibTableColumn
pmc2002AlmclientXfpSupplyAlarmIndex = _Pmc2002AlmclientXfpSupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 1),
    _Pmc2002AlmclientXfpSupplyAlarmIndex_Type()
)
pmc2002AlmclientXfpSupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpSupplyAlarmIndex.setStatus("current")
_Pmc2002AlmClientVee5LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVee5LowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVee5LowAlarmPortn = _Pmc2002AlmClientVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 2),
    _Pmc2002AlmClientVee5LowAlarmPortn_Type()
)
pmc2002AlmClientVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVee5LowAlarmPortn.setStatus("current")
_Pmc2002AlmClientVee5HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVee5HighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVee5HighAlarmPortn = _Pmc2002AlmClientVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 3),
    _Pmc2002AlmClientVee5HighAlarmPortn_Type()
)
pmc2002AlmClientVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVee5HighAlarmPortn.setStatus("current")
_Pmc2002AlmClientVcc2LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc2LowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVcc2LowAlarmPortn = _Pmc2002AlmClientVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 4),
    _Pmc2002AlmClientVcc2LowAlarmPortn_Type()
)
pmc2002AlmClientVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc2LowAlarmPortn.setStatus("current")
_Pmc2002AlmClientVcc2HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc2HighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVcc2HighAlarmPortn = _Pmc2002AlmClientVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 5),
    _Pmc2002AlmClientVcc2HighAlarmPortn_Type()
)
pmc2002AlmClientVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc2HighAlarmPortn.setStatus("current")
_Pmc2002AlmClientVcc3LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc3LowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVcc3LowAlarmPortn = _Pmc2002AlmClientVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 6),
    _Pmc2002AlmClientVcc3LowAlarmPortn_Type()
)
pmc2002AlmClientVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc3LowAlarmPortn.setStatus("current")
_Pmc2002AlmClientVcc3HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc3HighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVcc3HighAlarmPortn = _Pmc2002AlmClientVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 7),
    _Pmc2002AlmClientVcc3HighAlarmPortn_Type()
)
pmc2002AlmClientVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc3HighAlarmPortn.setStatus("current")
_Pmc2002AlmClientVcc5LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc5LowAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVcc5LowAlarmPortn = _Pmc2002AlmClientVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 8),
    _Pmc2002AlmClientVcc5LowAlarmPortn_Type()
)
pmc2002AlmClientVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc5LowAlarmPortn.setStatus("current")
_Pmc2002AlmClientVcc5HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc5HighAlarmPortn_Object = MibTableColumn
pmc2002AlmClientVcc5HighAlarmPortn = _Pmc2002AlmClientVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 9),
    _Pmc2002AlmClientVcc5HighAlarmPortn_Type()
)
pmc2002AlmClientVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc5HighAlarmPortn.setStatus("current")
_Pmc2002AlmClientVee5LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVee5LowWarningPortn_Object = MibTableColumn
pmc2002AlmClientVee5LowWarningPortn = _Pmc2002AlmClientVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 10),
    _Pmc2002AlmClientVee5LowWarningPortn_Type()
)
pmc2002AlmClientVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVee5LowWarningPortn.setStatus("current")
_Pmc2002AlmClientVee5HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVee5HighWarningPortn_Object = MibTableColumn
pmc2002AlmClientVee5HighWarningPortn = _Pmc2002AlmClientVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 11),
    _Pmc2002AlmClientVee5HighWarningPortn_Type()
)
pmc2002AlmClientVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVee5HighWarningPortn.setStatus("current")
_Pmc2002AlmClientVcc2LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc2LowWarningPortn_Object = MibTableColumn
pmc2002AlmClientVcc2LowWarningPortn = _Pmc2002AlmClientVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 12),
    _Pmc2002AlmClientVcc2LowWarningPortn_Type()
)
pmc2002AlmClientVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc2LowWarningPortn.setStatus("current")
_Pmc2002AlmClientVcc2HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc2HighWarningPortn_Object = MibTableColumn
pmc2002AlmClientVcc2HighWarningPortn = _Pmc2002AlmClientVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 13),
    _Pmc2002AlmClientVcc2HighWarningPortn_Type()
)
pmc2002AlmClientVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc2HighWarningPortn.setStatus("current")
_Pmc2002AlmClientVcc3LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc3LowWarningPortn_Object = MibTableColumn
pmc2002AlmClientVcc3LowWarningPortn = _Pmc2002AlmClientVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 14),
    _Pmc2002AlmClientVcc3LowWarningPortn_Type()
)
pmc2002AlmClientVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc3LowWarningPortn.setStatus("current")
_Pmc2002AlmClientVcc3HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc3HighWarningPortn_Object = MibTableColumn
pmc2002AlmClientVcc3HighWarningPortn = _Pmc2002AlmClientVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 15),
    _Pmc2002AlmClientVcc3HighWarningPortn_Type()
)
pmc2002AlmClientVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc3HighWarningPortn.setStatus("current")
_Pmc2002AlmClientVcc5LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc5LowWarningPortn_Object = MibTableColumn
pmc2002AlmClientVcc5LowWarningPortn = _Pmc2002AlmClientVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 16),
    _Pmc2002AlmClientVcc5LowWarningPortn_Type()
)
pmc2002AlmClientVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc5LowWarningPortn.setStatus("current")
_Pmc2002AlmClientVcc5HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientVcc5HighWarningPortn_Object = MibTableColumn
pmc2002AlmClientVcc5HighWarningPortn = _Pmc2002AlmClientVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 2, 64, 1, 17),
    _Pmc2002AlmClientVcc5HighWarningPortn_Type()
)
pmc2002AlmClientVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientVcc5HighWarningPortn.setStatus("current")
_Pmc2002AlmClientCrit_ObjectIdentity = ObjectIdentity
pmc2002AlmClientCrit = _Pmc2002AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3)
)
_Pmc2002AlmsynthAlmPortTable_Object = MibTable
pmc2002AlmsynthAlmPortTable = _Pmc2002AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmc2002AlmsynthAlmPortTable.setStatus("current")
_Pmc2002AlmsynthAlmPortEntry_Object = MibTableRow
pmc2002AlmsynthAlmPortEntry = _Pmc2002AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1)
)
pmc2002AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmsynthAlmPortEntry.setStatus("current")


class _Pmc2002AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmc2002AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmc2002AlmsynthAlmPortIndex_Object = MibTableColumn
pmc2002AlmsynthAlmPortIndex = _Pmc2002AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 1),
    _Pmc2002AlmsynthAlmPortIndex_Type()
)
pmc2002AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmsynthAlmPortIndex.setStatus("current")
_Pmc2002AlmClientSfpAbsentPortn_Type = EkiOnOff
_Pmc2002AlmClientSfpAbsentPortn_Object = MibTableColumn
pmc2002AlmClientSfpAbsentPortn = _Pmc2002AlmClientSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 2),
    _Pmc2002AlmClientSfpAbsentPortn_Type()
)
pmc2002AlmClientSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientSfpAbsentPortn.setStatus("current")
_Pmc2002AlmClientDdmAbsentPortn_Type = EkiOnOff
_Pmc2002AlmClientDdmAbsentPortn_Object = MibTableColumn
pmc2002AlmClientDdmAbsentPortn = _Pmc2002AlmClientDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 3),
    _Pmc2002AlmClientDdmAbsentPortn_Type()
)
pmc2002AlmClientDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientDdmAbsentPortn.setStatus("current")
_Pmc2002AlmClientHwFailPortn_Type = EkiOnOff
_Pmc2002AlmClientHwFailPortn_Object = MibTableColumn
pmc2002AlmClientHwFailPortn = _Pmc2002AlmClientHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 5),
    _Pmc2002AlmClientHwFailPortn_Type()
)
pmc2002AlmClientHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientHwFailPortn.setStatus("current")
_Pmc2002AlmClientDwLsdPortn_Type = EkiOnOff
_Pmc2002AlmClientDwLsdPortn_Object = MibTableColumn
pmc2002AlmClientDwLsdPortn = _Pmc2002AlmClientDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 6),
    _Pmc2002AlmClientDwLsdPortn_Type()
)
pmc2002AlmClientDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientDwLsdPortn.setStatus("current")
_Pmc2002AlmClientLocalOosPortn_Type = EkiOnOff
_Pmc2002AlmClientLocalOosPortn_Object = MibTableColumn
pmc2002AlmClientLocalOosPortn = _Pmc2002AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 7),
    _Pmc2002AlmClientLocalOosPortn_Type()
)
pmc2002AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientLocalOosPortn.setStatus("current")
_Pmc2002AlmClientDwCaisPortn_Type = EkiOnOff
_Pmc2002AlmClientDwCaisPortn_Object = MibTableColumn
pmc2002AlmClientDwCaisPortn = _Pmc2002AlmClientDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 9),
    _Pmc2002AlmClientDwCaisPortn_Type()
)
pmc2002AlmClientDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientDwCaisPortn.setStatus("current")
_Pmc2002AlmClientSfpDdmWarningPortn_Type = EkiOnOff
_Pmc2002AlmClientSfpDdmWarningPortn_Object = MibTableColumn
pmc2002AlmClientSfpDdmWarningPortn = _Pmc2002AlmClientSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 10),
    _Pmc2002AlmClientSfpDdmWarningPortn_Type()
)
pmc2002AlmClientSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientSfpDdmWarningPortn.setStatus("current")
_Pmc2002AlmClientSfpDdmAlmPortn_Type = EkiOnOff
_Pmc2002AlmClientSfpDdmAlmPortn_Object = MibTableColumn
pmc2002AlmClientSfpDdmAlmPortn = _Pmc2002AlmClientSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 11),
    _Pmc2002AlmClientSfpDdmAlmPortn_Type()
)
pmc2002AlmClientSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientSfpDdmAlmPortn.setStatus("current")
_Pmc2002AlmClientFailPortn_Type = EkiOnOff
_Pmc2002AlmClientFailPortn_Object = MibTableColumn
pmc2002AlmClientFailPortn = _Pmc2002AlmClientFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 13),
    _Pmc2002AlmClientFailPortn_Type()
)
pmc2002AlmClientFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientFailPortn.setStatus("current")
_Pmc2002AlmClientUpCsfPortn_Type = EkiOnOff
_Pmc2002AlmClientUpCsfPortn_Object = MibTableColumn
pmc2002AlmClientUpCsfPortn = _Pmc2002AlmClientUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 8, 1, 17),
    _Pmc2002AlmClientUpCsfPortn_Type()
)
pmc2002AlmClientUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientUpCsfPortn.setStatus("current")
_Pmc2002AlmclientAccessioAlmTable_Object = MibTable
pmc2002AlmclientAccessioAlmTable = _Pmc2002AlmclientAccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pmc2002AlmclientAccessioAlmTable.setStatus("current")
_Pmc2002AlmclientAccessioAlmEntry_Object = MibTableRow
pmc2002AlmclientAccessioAlmEntry = _Pmc2002AlmclientAccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 16, 1)
)
pmc2002AlmclientAccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmclientAccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmclientAccessioAlmEntry.setStatus("current")


class _Pmc2002AlmclientAccessioAlmIndex_Type(Integer32):
    """Custom type pmc2002AlmclientAccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmclientAccessioAlmIndex_Type.__name__ = "Integer32"
_Pmc2002AlmclientAccessioAlmIndex_Object = MibTableColumn
pmc2002AlmclientAccessioAlmIndex = _Pmc2002AlmclientAccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 16, 1, 1),
    _Pmc2002AlmclientAccessioAlmIndex_Type()
)
pmc2002AlmclientAccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmclientAccessioAlmIndex.setStatus("current")
_Pmc2002AlmClientDwLasFailPortn_Type = EkiOnOff
_Pmc2002AlmClientDwLasFailPortn_Object = MibTableColumn
pmc2002AlmClientDwLasFailPortn = _Pmc2002AlmClientDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 16, 1, 2),
    _Pmc2002AlmClientDwLasFailPortn_Type()
)
pmc2002AlmClientDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientDwLasFailPortn.setStatus("current")
_Pmc2002AlmClientUpLosPortn_Type = EkiOnOff
_Pmc2002AlmClientUpLosPortn_Object = MibTableColumn
pmc2002AlmClientUpLosPortn = _Pmc2002AlmClientUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 16, 1, 5),
    _Pmc2002AlmClientUpLosPortn_Type()
)
pmc2002AlmClientUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientUpLosPortn.setStatus("current")
_Pmc2002AlmclientXfpAlarm2Table_Object = MibTable
pmc2002AlmclientXfpAlarm2Table = _Pmc2002AlmclientXfpAlarm2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpAlarm2Table.setStatus("current")
_Pmc2002AlmclientXfpAlarm2Entry_Object = MibTableRow
pmc2002AlmclientXfpAlarm2Entry = _Pmc2002AlmclientXfpAlarm2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1)
)
pmc2002AlmclientXfpAlarm2Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmclientXfpAlarm2Index"),
)
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpAlarm2Entry.setStatus("current")


class _Pmc2002AlmclientXfpAlarm2Index_Type(Integer32):
    """Custom type pmc2002AlmclientXfpAlarm2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmclientXfpAlarm2Index_Type.__name__ = "Integer32"
_Pmc2002AlmclientXfpAlarm2Index_Object = MibTableColumn
pmc2002AlmclientXfpAlarm2Index = _Pmc2002AlmclientXfpAlarm2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 1),
    _Pmc2002AlmclientXfpAlarm2Index_Type()
)
pmc2002AlmclientXfpAlarm2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmclientXfpAlarm2Index.setStatus("current")
_Pmc2002AlmClientModNrPortn_Type = EkiOnOff
_Pmc2002AlmClientModNrPortn_Object = MibTableColumn
pmc2002AlmClientModNrPortn = _Pmc2002AlmClientModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 3),
    _Pmc2002AlmClientModNrPortn_Type()
)
pmc2002AlmClientModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientModNrPortn.setStatus("current")
_Pmc2002AlmClientRxCdrNotLockedPortn_Type = EkiOnOff
_Pmc2002AlmClientRxCdrNotLockedPortn_Object = MibTableColumn
pmc2002AlmClientRxCdrNotLockedPortn = _Pmc2002AlmClientRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 4),
    _Pmc2002AlmClientRxCdrNotLockedPortn_Type()
)
pmc2002AlmClientRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientRxCdrNotLockedPortn.setStatus("current")
_Pmc2002AlmClientRxNrPortn_Type = EkiOnOff
_Pmc2002AlmClientRxNrPortn_Object = MibTableColumn
pmc2002AlmClientRxNrPortn = _Pmc2002AlmClientRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 6),
    _Pmc2002AlmClientRxNrPortn_Type()
)
pmc2002AlmClientRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientRxNrPortn.setStatus("current")
_Pmc2002AlmClientTxCdrNotLockedPortn_Type = EkiOnOff
_Pmc2002AlmClientTxCdrNotLockedPortn_Object = MibTableColumn
pmc2002AlmClientTxCdrNotLockedPortn = _Pmc2002AlmClientTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 7),
    _Pmc2002AlmClientTxCdrNotLockedPortn_Type()
)
pmc2002AlmClientTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxCdrNotLockedPortn.setStatus("current")
_Pmc2002AlmClientTxFaultPortn_Type = EkiOnOff
_Pmc2002AlmClientTxFaultPortn_Object = MibTableColumn
pmc2002AlmClientTxFaultPortn = _Pmc2002AlmClientTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 8),
    _Pmc2002AlmClientTxFaultPortn_Type()
)
pmc2002AlmClientTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxFaultPortn.setStatus("current")
_Pmc2002AlmClientTxNrPortn_Type = EkiOnOff
_Pmc2002AlmClientTxNrPortn_Object = MibTableColumn
pmc2002AlmClientTxNrPortn = _Pmc2002AlmClientTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 9),
    _Pmc2002AlmClientTxNrPortn_Type()
)
pmc2002AlmClientTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTxNrPortn.setStatus("current")
_Pmc2002AlmClientWavelengthUnlockedPortn_Type = EkiOnOff
_Pmc2002AlmClientWavelengthUnlockedPortn_Object = MibTableColumn
pmc2002AlmClientWavelengthUnlockedPortn = _Pmc2002AlmClientWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 15),
    _Pmc2002AlmClientWavelengthUnlockedPortn_Type()
)
pmc2002AlmClientWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientWavelengthUnlockedPortn.setStatus("current")
_Pmc2002AlmClientTecFaultPortn_Type = EkiOnOff
_Pmc2002AlmClientTecFaultPortn_Object = MibTableColumn
pmc2002AlmClientTecFaultPortn = _Pmc2002AlmClientTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 16),
    _Pmc2002AlmClientTecFaultPortn_Type()
)
pmc2002AlmClientTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientTecFaultPortn.setStatus("current")
_Pmc2002AlmClientApdSupplyFaultPortn_Type = EkiOnOff
_Pmc2002AlmClientApdSupplyFaultPortn_Object = MibTableColumn
pmc2002AlmClientApdSupplyFaultPortn = _Pmc2002AlmClientApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 40, 1, 17),
    _Pmc2002AlmClientApdSupplyFaultPortn_Type()
)
pmc2002AlmClientApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientApdSupplyFaultPortn.setStatus("current")
_Pmc2002AlmclientMapperDeAlmTable_Object = MibTable
pmc2002AlmclientMapperDeAlmTable = _Pmc2002AlmclientMapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pmc2002AlmclientMapperDeAlmTable.setStatus("current")
_Pmc2002AlmclientMapperDeAlmEntry_Object = MibTableRow
pmc2002AlmclientMapperDeAlmEntry = _Pmc2002AlmclientMapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72, 1)
)
pmc2002AlmclientMapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmclientMapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmclientMapperDeAlmEntry.setStatus("current")


class _Pmc2002AlmclientMapperDeAlmIndex_Type(Integer32):
    """Custom type pmc2002AlmclientMapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmclientMapperDeAlmIndex_Type.__name__ = "Integer32"
_Pmc2002AlmclientMapperDeAlmIndex_Object = MibTableColumn
pmc2002AlmclientMapperDeAlmIndex = _Pmc2002AlmclientMapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72, 1, 1),
    _Pmc2002AlmclientMapperDeAlmIndex_Type()
)
pmc2002AlmclientMapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmclientMapperDeAlmIndex.setStatus("current")
_Pmc2002AlmClientUpAccOosPortn_Type = EkiOnOff
_Pmc2002AlmClientUpAccOosPortn_Object = MibTableColumn
pmc2002AlmClientUpAccOosPortn = _Pmc2002AlmClientUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72, 1, 2),
    _Pmc2002AlmClientUpAccOosPortn_Type()
)
pmc2002AlmClientUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientUpAccOosPortn.setStatus("current")
_Pmc2002AlmClientUpBufferOvlPortn_Type = EkiOnOff
_Pmc2002AlmClientUpBufferOvlPortn_Object = MibTableColumn
pmc2002AlmClientUpBufferOvlPortn = _Pmc2002AlmClientUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72, 1, 11),
    _Pmc2002AlmClientUpBufferOvlPortn_Type()
)
pmc2002AlmClientUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientUpBufferOvlPortn.setStatus("current")
_Pmc2002AlmClientDwCsfDetPortn_Type = EkiOnOff
_Pmc2002AlmClientDwCsfDetPortn_Object = MibTableColumn
pmc2002AlmClientDwCsfDetPortn = _Pmc2002AlmClientDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72, 1, 12),
    _Pmc2002AlmClientDwCsfDetPortn_Type()
)
pmc2002AlmClientDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientDwCsfDetPortn.setStatus("current")
_Pmc2002AlmClientDwBufferOvlPortn_Type = EkiOnOff
_Pmc2002AlmClientDwBufferOvlPortn_Object = MibTableColumn
pmc2002AlmClientDwBufferOvlPortn = _Pmc2002AlmClientDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 2, 3, 72, 1, 15),
    _Pmc2002AlmClientDwBufferOvlPortn_Type()
)
pmc2002AlmClientDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmClientDwBufferOvlPortn.setStatus("current")
_Pmc2002AlmLine_ObjectIdentity = ObjectIdentity
pmc2002AlmLine = _Pmc2002AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3)
)
_Pmc2002AlmLineNurg_ObjectIdentity = ObjectIdentity
pmc2002AlmLineNurg = _Pmc2002AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1)
)
_Pmc2002AlmlineXfp1WarningsTable_Object = MibTable
pmc2002AlmlineXfp1WarningsTable = _Pmc2002AlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1WarningsTable.setStatus("current")
_Pmc2002AlmlineXfp1WarningsEntry_Object = MibTableRow
pmc2002AlmlineXfp1WarningsEntry = _Pmc2002AlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1)
)
pmc2002AlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1WarningsEntry.setStatus("current")


class _Pmc2002AlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pmc2002AlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineXfp1WarningsIndex_Object = MibTableColumn
pmc2002AlmlineXfp1WarningsIndex = _Pmc2002AlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 1),
    _Pmc2002AlmlineXfp1WarningsIndex_Type()
)
pmc2002AlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1WarningsIndex.setStatus("current")
_Pmc2002AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pmc2002AlmLineTxPowerLowWarningPortn = _Pmc2002AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 2),
    _Pmc2002AlmLineTxPowerLowWarningPortn_Type()
)
pmc2002AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxPowerLowWarningPortn.setStatus("current")
_Pmc2002AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineTxPowerHighWarningPortn = _Pmc2002AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 3),
    _Pmc2002AlmLineTxPowerHighWarningPortn_Type()
)
pmc2002AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxPowerHighWarningPortn.setStatus("current")
_Pmc2002AlmLineTxBiasLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineTxBiasLowWarningPortn_Object = MibTableColumn
pmc2002AlmLineTxBiasLowWarningPortn = _Pmc2002AlmLineTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 4),
    _Pmc2002AlmLineTxBiasLowWarningPortn_Type()
)
pmc2002AlmLineTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxBiasLowWarningPortn.setStatus("current")
_Pmc2002AlmLineTxBiasHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineTxBiasHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineTxBiasHighWarningPortn = _Pmc2002AlmLineTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 5),
    _Pmc2002AlmLineTxBiasHighWarningPortn_Type()
)
pmc2002AlmLineTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxBiasHighWarningPortn.setStatus("current")
_Pmc2002AlmLineTempLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineTempLowWarningPortn_Object = MibTableColumn
pmc2002AlmLineTempLowWarningPortn = _Pmc2002AlmLineTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 8),
    _Pmc2002AlmLineTempLowWarningPortn_Type()
)
pmc2002AlmLineTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTempLowWarningPortn.setStatus("current")
_Pmc2002AlmLineTempHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineTempHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineTempHighWarningPortn = _Pmc2002AlmLineTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 9),
    _Pmc2002AlmLineTempHighWarningPortn_Type()
)
pmc2002AlmLineTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTempHighWarningPortn.setStatus("current")
_Pmc2002AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pmc2002AlmLineRxPowerLowWarningPortn = _Pmc2002AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 16),
    _Pmc2002AlmLineRxPowerLowWarningPortn_Type()
)
pmc2002AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineRxPowerLowWarningPortn.setStatus("current")
_Pmc2002AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineRxPowerHighWarningPortn = _Pmc2002AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 209, 1, 17),
    _Pmc2002AlmLineRxPowerHighWarningPortn_Type()
)
pmc2002AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineRxPowerHighWarningPortn.setStatus("current")
_Pmc2002AlmlineOtx1TlhWarningsTable_Object = MibTable
pmc2002AlmlineOtx1TlhWarningsTable = _Pmc2002AlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineOtx1TlhWarningsTable.setStatus("current")
_Pmc2002AlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pmc2002AlmlineOtx1TlhWarningsEntry = _Pmc2002AlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225, 1)
)
pmc2002AlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pmc2002AlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pmc2002AlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pmc2002AlmlineOtx1TlhWarningsIndex = _Pmc2002AlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225, 1, 1),
    _Pmc2002AlmlineOtx1TlhWarningsIndex_Type()
)
pmc2002AlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pmc2002AlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineModulatorAgingHighWarningPortn = _Pmc2002AlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225, 1, 6),
    _Pmc2002AlmLineModulatorAgingHighWarningPortn_Type()
)
pmc2002AlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pmc2002AlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineAgingHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineAgingHighWarningPortn = _Pmc2002AlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225, 1, 7),
    _Pmc2002AlmLineAgingHighWarningPortn_Type()
)
pmc2002AlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineAgingHighWarningPortn.setStatus("current")
_Pmc2002AlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineFreqDevHighWarningPortn = _Pmc2002AlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225, 1, 13),
    _Pmc2002AlmLineFreqDevHighWarningPortn_Type()
)
pmc2002AlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineFreqDevHighWarningPortn.setStatus("current")
_Pmc2002AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pmc2002AlmLineLaserTempHighWarningPortn = _Pmc2002AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 1, 225, 1, 15),
    _Pmc2002AlmLineLaserTempHighWarningPortn_Type()
)
pmc2002AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineLaserTempHighWarningPortn.setStatus("current")
_Pmc2002AlmLineUrg_ObjectIdentity = ObjectIdentity
pmc2002AlmLineUrg = _Pmc2002AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2)
)
_Pmc2002AlmdfrmBerTable_Object = MibTable
pmc2002AlmdfrmBerTable = _Pmc2002AlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pmc2002AlmdfrmBerTable.setStatus("current")
_Pmc2002AlmdfrmBerEntry_Object = MibTableRow
pmc2002AlmdfrmBerEntry = _Pmc2002AlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 129, 1)
)
pmc2002AlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmdfrmBerEntry.setStatus("current")


class _Pmc2002AlmdfrmBerIndex_Type(Integer32):
    """Custom type pmc2002AlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pmc2002AlmdfrmBerIndex_Object = MibTableColumn
pmc2002AlmdfrmBerIndex = _Pmc2002AlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 129, 1, 1),
    _Pmc2002AlmdfrmBerIndex_Type()
)
pmc2002AlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmdfrmBerIndex.setStatus("current")
_Pmc2002AlmLineSignalDegradePortn_Type = EkiOnOff
_Pmc2002AlmLineSignalDegradePortn_Object = MibTableColumn
pmc2002AlmLineSignalDegradePortn = _Pmc2002AlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 129, 1, 2),
    _Pmc2002AlmLineSignalDegradePortn_Type()
)
pmc2002AlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineSignalDegradePortn.setStatus("current")
_Pmc2002AlmLineSignalFailPortn_Type = EkiOnOff
_Pmc2002AlmLineSignalFailPortn_Object = MibTableColumn
pmc2002AlmLineSignalFailPortn = _Pmc2002AlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 129, 1, 3),
    _Pmc2002AlmLineSignalFailPortn_Type()
)
pmc2002AlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineSignalFailPortn.setStatus("current")
_Pmc2002AlmLineDegradePortn_Type = EkiOnOff
_Pmc2002AlmLineDegradePortn_Object = MibTableColumn
pmc2002AlmLineDegradePortn = _Pmc2002AlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 129, 1, 6),
    _Pmc2002AlmLineDegradePortn_Type()
)
pmc2002AlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDegradePortn.setStatus("current")
_Pmc2002AlmlineXfp1AlarmTable_Object = MibTable
pmc2002AlmlineXfp1AlarmTable = _Pmc2002AlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1AlarmTable.setStatus("current")
_Pmc2002AlmlineXfp1AlarmEntry_Object = MibTableRow
pmc2002AlmlineXfp1AlarmEntry = _Pmc2002AlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1)
)
pmc2002AlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1AlarmEntry.setStatus("current")


class _Pmc2002AlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pmc2002AlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineXfp1AlarmIndex_Object = MibTableColumn
pmc2002AlmlineXfp1AlarmIndex = _Pmc2002AlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 1),
    _Pmc2002AlmlineXfp1AlarmIndex_Type()
)
pmc2002AlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1AlarmIndex.setStatus("current")
_Pmc2002AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineTxPowerLowAlarmPortn = _Pmc2002AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 2),
    _Pmc2002AlmLineTxPowerLowAlarmPortn_Type()
)
pmc2002AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pmc2002AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineTxPowerHighAlarmPortn = _Pmc2002AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 3),
    _Pmc2002AlmLineTxPowerHighAlarmPortn_Type()
)
pmc2002AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pmc2002AlmLineTxBiasLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineTxBiasLowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineTxBiasLowAlarmPortn = _Pmc2002AlmLineTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 4),
    _Pmc2002AlmLineTxBiasLowAlarmPortn_Type()
)
pmc2002AlmLineTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxBiasLowAlarmPortn.setStatus("current")
_Pmc2002AlmLineTxBiasHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineTxBiasHighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineTxBiasHighAlarmPortn = _Pmc2002AlmLineTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 5),
    _Pmc2002AlmLineTxBiasHighAlarmPortn_Type()
)
pmc2002AlmLineTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxBiasHighAlarmPortn.setStatus("current")
_Pmc2002AlmLineTempLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineTempLowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineTempLowAlarmPortn = _Pmc2002AlmLineTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 8),
    _Pmc2002AlmLineTempLowAlarmPortn_Type()
)
pmc2002AlmLineTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTempLowAlarmPortn.setStatus("current")
_Pmc2002AlmLineTempHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineTempHighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineTempHighAlarmPortn = _Pmc2002AlmLineTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 9),
    _Pmc2002AlmLineTempHighAlarmPortn_Type()
)
pmc2002AlmLineTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTempHighAlarmPortn.setStatus("current")
_Pmc2002AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineRxPowerLowAlarmPortn = _Pmc2002AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 16),
    _Pmc2002AlmLineRxPowerLowAlarmPortn_Type()
)
pmc2002AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pmc2002AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineRxPowerHighAlarmPortn = _Pmc2002AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 208, 1, 17),
    _Pmc2002AlmLineRxPowerHighAlarmPortn_Type()
)
pmc2002AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pmc2002AlmlineXfp1SupplyAlarmTable_Object = MibTable
pmc2002AlmlineXfp1SupplyAlarmTable = _Pmc2002AlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pmc2002AlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pmc2002AlmlineXfp1SupplyAlarmEntry = _Pmc2002AlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1)
)
pmc2002AlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pmc2002AlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pmc2002AlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pmc2002AlmlineXfp1SupplyAlarmIndex = _Pmc2002AlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 1),
    _Pmc2002AlmlineXfp1SupplyAlarmIndex_Type()
)
pmc2002AlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pmc2002AlmLineVee5LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVee5LowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVee5LowAlarmPortn = _Pmc2002AlmLineVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 2),
    _Pmc2002AlmLineVee5LowAlarmPortn_Type()
)
pmc2002AlmLineVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVee5LowAlarmPortn.setStatus("current")
_Pmc2002AlmLineVee5HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVee5HighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVee5HighAlarmPortn = _Pmc2002AlmLineVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 3),
    _Pmc2002AlmLineVee5HighAlarmPortn_Type()
)
pmc2002AlmLineVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVee5HighAlarmPortn.setStatus("current")
_Pmc2002AlmLineVcc2LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc2LowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVcc2LowAlarmPortn = _Pmc2002AlmLineVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 4),
    _Pmc2002AlmLineVcc2LowAlarmPortn_Type()
)
pmc2002AlmLineVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc2LowAlarmPortn.setStatus("current")
_Pmc2002AlmLineVcc2HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc2HighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVcc2HighAlarmPortn = _Pmc2002AlmLineVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 5),
    _Pmc2002AlmLineVcc2HighAlarmPortn_Type()
)
pmc2002AlmLineVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc2HighAlarmPortn.setStatus("current")
_Pmc2002AlmLineVcc3LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc3LowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVcc3LowAlarmPortn = _Pmc2002AlmLineVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 6),
    _Pmc2002AlmLineVcc3LowAlarmPortn_Type()
)
pmc2002AlmLineVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc3LowAlarmPortn.setStatus("current")
_Pmc2002AlmLineVcc3HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc3HighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVcc3HighAlarmPortn = _Pmc2002AlmLineVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 7),
    _Pmc2002AlmLineVcc3HighAlarmPortn_Type()
)
pmc2002AlmLineVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc3HighAlarmPortn.setStatus("current")
_Pmc2002AlmLineVcc5LowAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc5LowAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVcc5LowAlarmPortn = _Pmc2002AlmLineVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 8),
    _Pmc2002AlmLineVcc5LowAlarmPortn_Type()
)
pmc2002AlmLineVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc5LowAlarmPortn.setStatus("current")
_Pmc2002AlmLineVcc5HighAlarmPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc5HighAlarmPortn_Object = MibTableColumn
pmc2002AlmLineVcc5HighAlarmPortn = _Pmc2002AlmLineVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 9),
    _Pmc2002AlmLineVcc5HighAlarmPortn_Type()
)
pmc2002AlmLineVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc5HighAlarmPortn.setStatus("current")
_Pmc2002AlmLineVee5LowLineWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVee5LowLineWarningPortn_Object = MibTableColumn
pmc2002AlmLineVee5LowLineWarningPortn = _Pmc2002AlmLineVee5LowLineWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 10),
    _Pmc2002AlmLineVee5LowLineWarningPortn_Type()
)
pmc2002AlmLineVee5LowLineWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVee5LowLineWarningPortn.setStatus("current")
_Pmc2002AlmLineVee5HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVee5HighWarningPortn_Object = MibTableColumn
pmc2002AlmLineVee5HighWarningPortn = _Pmc2002AlmLineVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 11),
    _Pmc2002AlmLineVee5HighWarningPortn_Type()
)
pmc2002AlmLineVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVee5HighWarningPortn.setStatus("current")
_Pmc2002AlmLineVcc2LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc2LowWarningPortn_Object = MibTableColumn
pmc2002AlmLineVcc2LowWarningPortn = _Pmc2002AlmLineVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 12),
    _Pmc2002AlmLineVcc2LowWarningPortn_Type()
)
pmc2002AlmLineVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc2LowWarningPortn.setStatus("current")
_Pmc2002AlmLineVcc2HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc2HighWarningPortn_Object = MibTableColumn
pmc2002AlmLineVcc2HighWarningPortn = _Pmc2002AlmLineVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 13),
    _Pmc2002AlmLineVcc2HighWarningPortn_Type()
)
pmc2002AlmLineVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc2HighWarningPortn.setStatus("current")
_Pmc2002AlmLineVcc3LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc3LowWarningPortn_Object = MibTableColumn
pmc2002AlmLineVcc3LowWarningPortn = _Pmc2002AlmLineVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 14),
    _Pmc2002AlmLineVcc3LowWarningPortn_Type()
)
pmc2002AlmLineVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc3LowWarningPortn.setStatus("current")
_Pmc2002AlmLineVcc3HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc3HighWarningPortn_Object = MibTableColumn
pmc2002AlmLineVcc3HighWarningPortn = _Pmc2002AlmLineVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 15),
    _Pmc2002AlmLineVcc3HighWarningPortn_Type()
)
pmc2002AlmLineVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc3HighWarningPortn.setStatus("current")
_Pmc2002AlmLineVcc5LowWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc5LowWarningPortn_Object = MibTableColumn
pmc2002AlmLineVcc5LowWarningPortn = _Pmc2002AlmLineVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 16),
    _Pmc2002AlmLineVcc5LowWarningPortn_Type()
)
pmc2002AlmLineVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc5LowWarningPortn.setStatus("current")
_Pmc2002AlmLineVcc5HighWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineVcc5HighWarningPortn_Object = MibTableColumn
pmc2002AlmLineVcc5HighWarningPortn = _Pmc2002AlmLineVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 212, 1, 17),
    _Pmc2002AlmLineVcc5HighWarningPortn_Type()
)
pmc2002AlmLineVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineVcc5HighWarningPortn.setStatus("current")
_Pmc2002AlmlineOtx1TlhAlarmsTable_Object = MibTable
pmc2002AlmlineOtx1TlhAlarmsTable = _Pmc2002AlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pmc2002AlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pmc2002AlmlineOtx1TlhAlarmsEntry = _Pmc2002AlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1)
)
pmc2002AlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pmc2002AlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pmc2002AlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pmc2002AlmlineOtx1TlhAlarmsIndex = _Pmc2002AlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1, 1),
    _Pmc2002AlmlineOtx1TlhAlarmsIndex_Type()
)
pmc2002AlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pmc2002AlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pmc2002AlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pmc2002AlmLineModulatorAgingHighAlaPortn = _Pmc2002AlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1, 6),
    _Pmc2002AlmLineModulatorAgingHighAlaPortn_Type()
)
pmc2002AlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pmc2002AlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pmc2002AlmLineAgingHighAlaPortn_Object = MibTableColumn
pmc2002AlmLineAgingHighAlaPortn = _Pmc2002AlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1, 7),
    _Pmc2002AlmLineAgingHighAlaPortn_Type()
)
pmc2002AlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineAgingHighAlaPortn.setStatus("current")
_Pmc2002AlmLineCdrNotReadyPortn_Type = EkiOnOff
_Pmc2002AlmLineCdrNotReadyPortn_Object = MibTableColumn
pmc2002AlmLineCdrNotReadyPortn = _Pmc2002AlmLineCdrNotReadyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1, 10),
    _Pmc2002AlmLineCdrNotReadyPortn_Type()
)
pmc2002AlmLineCdrNotReadyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineCdrNotReadyPortn.setStatus("current")
_Pmc2002AlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pmc2002AlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pmc2002AlmLineFreqDevHighAlaPortn = _Pmc2002AlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1, 13),
    _Pmc2002AlmLineFreqDevHighAlaPortn_Type()
)
pmc2002AlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineFreqDevHighAlaPortn.setStatus("current")
_Pmc2002AlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pmc2002AlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pmc2002AlmLineLaserTempHighAlaPortn = _Pmc2002AlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 2, 224, 1, 15),
    _Pmc2002AlmLineLaserTempHighAlaPortn_Type()
)
pmc2002AlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineLaserTempHighAlaPortn.setStatus("current")
_Pmc2002AlmLineCrit_ObjectIdentity = ObjectIdentity
pmc2002AlmLineCrit = _Pmc2002AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3)
)
_Pmc2002AlmsynthAlmLineTable_Object = MibTable
pmc2002AlmsynthAlmLineTable = _Pmc2002AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pmc2002AlmsynthAlmLineTable.setStatus("current")
_Pmc2002AlmsynthAlmLineEntry_Object = MibTableRow
pmc2002AlmsynthAlmLineEntry = _Pmc2002AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1)
)
pmc2002AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmsynthAlmLineEntry.setStatus("current")


class _Pmc2002AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pmc2002AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pmc2002AlmsynthAlmLineIndex_Object = MibTableColumn
pmc2002AlmsynthAlmLineIndex = _Pmc2002AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 1),
    _Pmc2002AlmsynthAlmLineIndex_Type()
)
pmc2002AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmsynthAlmLineIndex.setStatus("current")
_Pmc2002AlmLineXfpAbsentPortn_Type = EkiOnOff
_Pmc2002AlmLineXfpAbsentPortn_Object = MibTableColumn
pmc2002AlmLineXfpAbsentPortn = _Pmc2002AlmLineXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 2),
    _Pmc2002AlmLineXfpAbsentPortn_Type()
)
pmc2002AlmLineXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineXfpAbsentPortn.setStatus("current")
_Pmc2002AlmLineXfpInitNotComplPortn_Type = EkiOnOff
_Pmc2002AlmLineXfpInitNotComplPortn_Object = MibTableColumn
pmc2002AlmLineXfpInitNotComplPortn = _Pmc2002AlmLineXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 3),
    _Pmc2002AlmLineXfpInitNotComplPortn_Type()
)
pmc2002AlmLineXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineXfpInitNotComplPortn.setStatus("current")
_Pmc2002AlmLineHwFailPortn_Type = EkiOnOff
_Pmc2002AlmLineHwFailPortn_Object = MibTableColumn
pmc2002AlmLineHwFailPortn = _Pmc2002AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 5),
    _Pmc2002AlmLineHwFailPortn_Type()
)
pmc2002AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineHwFailPortn.setStatus("current")
_Pmc2002AlmLineXfpTxOffPortn_Type = EkiOnOff
_Pmc2002AlmLineXfpTxOffPortn_Object = MibTableColumn
pmc2002AlmLineXfpTxOffPortn = _Pmc2002AlmLineXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 6),
    _Pmc2002AlmLineXfpTxOffPortn_Type()
)
pmc2002AlmLineXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineXfpTxOffPortn.setStatus("current")
_Pmc2002AlmLineLocalOosPortn_Type = EkiOnOff
_Pmc2002AlmLineLocalOosPortn_Object = MibTableColumn
pmc2002AlmLineLocalOosPortn = _Pmc2002AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 7),
    _Pmc2002AlmLineLocalOosPortn_Type()
)
pmc2002AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineLocalOosPortn.setStatus("current")
_Pmc2002AlmLineUpRdiInsPortn_Type = EkiOnOff
_Pmc2002AlmLineUpRdiInsPortn_Object = MibTableColumn
pmc2002AlmLineUpRdiInsPortn = _Pmc2002AlmLineUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 9),
    _Pmc2002AlmLineUpRdiInsPortn_Type()
)
pmc2002AlmLineUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineUpRdiInsPortn.setStatus("current")
_Pmc2002AlmLineDdmWarningPortn_Type = EkiOnOff
_Pmc2002AlmLineDdmWarningPortn_Object = MibTableColumn
pmc2002AlmLineDdmWarningPortn = _Pmc2002AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 10),
    _Pmc2002AlmLineDdmWarningPortn_Type()
)
pmc2002AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDdmWarningPortn.setStatus("current")
_Pmc2002AlmLineDdmAlmPortn_Type = EkiOnOff
_Pmc2002AlmLineDdmAlmPortn_Object = MibTableColumn
pmc2002AlmLineDdmAlmPortn = _Pmc2002AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 11),
    _Pmc2002AlmLineDdmAlmPortn_Type()
)
pmc2002AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDdmAlmPortn.setStatus("current")
_Pmc2002AlmLineFailPortn_Type = EkiOnOff
_Pmc2002AlmLineFailPortn_Object = MibTableColumn
pmc2002AlmLineFailPortn = _Pmc2002AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 7, 1, 13),
    _Pmc2002AlmLineFailPortn_Type()
)
pmc2002AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineFailPortn.setStatus("current")
_Pmc2002AlmdfrmAlmTable_Object = MibTable
pmc2002AlmdfrmAlmTable = _Pmc2002AlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pmc2002AlmdfrmAlmTable.setStatus("current")
_Pmc2002AlmdfrmAlmEntry_Object = MibTableRow
pmc2002AlmdfrmAlmEntry = _Pmc2002AlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1)
)
pmc2002AlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmdfrmAlmEntry.setStatus("current")


class _Pmc2002AlmdfrmAlmIndex_Type(Integer32):
    """Custom type pmc2002AlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pmc2002AlmdfrmAlmIndex_Object = MibTableColumn
pmc2002AlmdfrmAlmIndex = _Pmc2002AlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1, 1),
    _Pmc2002AlmdfrmAlmIndex_Type()
)
pmc2002AlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmdfrmAlmIndex.setStatus("current")
_Pmc2002AlmLineDwAisDetPortn_Type = EkiOnOff
_Pmc2002AlmLineDwAisDetPortn_Object = MibTableColumn
pmc2002AlmLineDwAisDetPortn = _Pmc2002AlmLineDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1, 2),
    _Pmc2002AlmLineDwAisDetPortn_Type()
)
pmc2002AlmLineDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDwAisDetPortn.setStatus("current")
_Pmc2002AlmLineDwRdiDetPortn_Type = EkiOnOff
_Pmc2002AlmLineDwRdiDetPortn_Object = MibTableColumn
pmc2002AlmLineDwRdiDetPortn = _Pmc2002AlmLineDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1, 3),
    _Pmc2002AlmLineDwRdiDetPortn_Type()
)
pmc2002AlmLineDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDwRdiDetPortn.setStatus("current")
_Pmc2002AlmLineDwOofPortn_Type = EkiOnOff
_Pmc2002AlmLineDwOofPortn_Object = MibTableColumn
pmc2002AlmLineDwOofPortn = _Pmc2002AlmLineDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1, 4),
    _Pmc2002AlmLineDwOofPortn_Type()
)
pmc2002AlmLineDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDwOofPortn.setStatus("current")
_Pmc2002AlmLineDwLofPortn_Type = EkiOnOff
_Pmc2002AlmLineDwLofPortn_Object = MibTableColumn
pmc2002AlmLineDwLofPortn = _Pmc2002AlmLineDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1, 5),
    _Pmc2002AlmLineDwLofPortn_Type()
)
pmc2002AlmLineDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDwLofPortn.setStatus("current")
_Pmc2002AlmLineFecFailPortn_Type = EkiOnOff
_Pmc2002AlmLineFecFailPortn_Object = MibTableColumn
pmc2002AlmLineFecFailPortn = _Pmc2002AlmLineFecFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 128, 1, 6),
    _Pmc2002AlmLineFecFailPortn_Type()
)
pmc2002AlmLineFecFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineFecFailPortn.setStatus("current")
_Pmc2002AlmlineSyncAlarmsTable_Object = MibTable
pmc2002AlmlineSyncAlarmsTable = _Pmc2002AlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineSyncAlarmsTable.setStatus("current")
_Pmc2002AlmlineSyncAlarmsEntry_Object = MibTableRow
pmc2002AlmlineSyncAlarmsEntry = _Pmc2002AlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 133, 1)
)
pmc2002AlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineSyncAlarmsEntry.setStatus("current")


class _Pmc2002AlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pmc2002AlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineSyncAlarmsIndex_Object = MibTableColumn
pmc2002AlmlineSyncAlarmsIndex = _Pmc2002AlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 133, 1, 1),
    _Pmc2002AlmlineSyncAlarmsIndex_Type()
)
pmc2002AlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineSyncAlarmsIndex.setStatus("current")
_Pmc2002AlmLineDwLockerrPortn_Type = EkiOnOff
_Pmc2002AlmLineDwLockerrPortn_Object = MibTableColumn
pmc2002AlmLineDwLockerrPortn = _Pmc2002AlmLineDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 133, 1, 13),
    _Pmc2002AlmLineDwLockerrPortn_Type()
)
pmc2002AlmLineDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDwLockerrPortn.setStatus("current")
_Pmc2002AlmLineUpLockerrPortn_Type = EkiOnOff
_Pmc2002AlmLineUpLockerrPortn_Object = MibTableColumn
pmc2002AlmLineUpLockerrPortn = _Pmc2002AlmLineUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 133, 1, 14),
    _Pmc2002AlmLineUpLockerrPortn_Type()
)
pmc2002AlmLineUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineUpLockerrPortn.setStatus("current")
_Pmc2002AlmLineDwLosPortn_Type = EkiOnOff
_Pmc2002AlmLineDwLosPortn_Object = MibTableColumn
pmc2002AlmLineDwLosPortn = _Pmc2002AlmLineDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 133, 1, 17),
    _Pmc2002AlmLineDwLosPortn_Type()
)
pmc2002AlmLineDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineDwLosPortn.setStatus("current")
_Pmc2002AlmlineXfp1AlarmsTable_Object = MibTable
pmc2002AlmlineXfp1AlarmsTable = _Pmc2002AlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1AlarmsTable.setStatus("current")
_Pmc2002AlmlineXfp1AlarmsEntry_Object = MibTableRow
pmc2002AlmlineXfp1AlarmsEntry = _Pmc2002AlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1)
)
pmc2002AlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002AlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1AlarmsEntry.setStatus("current")


class _Pmc2002AlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pmc2002AlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002AlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pmc2002AlmlineXfp1AlarmsIndex_Object = MibTableColumn
pmc2002AlmlineXfp1AlarmsIndex = _Pmc2002AlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 1),
    _Pmc2002AlmlineXfp1AlarmsIndex_Type()
)
pmc2002AlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmlineXfp1AlarmsIndex.setStatus("current")
_Pmc2002AlmLineModNrPortn_Type = EkiOnOff
_Pmc2002AlmLineModNrPortn_Object = MibTableColumn
pmc2002AlmLineModNrPortn = _Pmc2002AlmLineModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 3),
    _Pmc2002AlmLineModNrPortn_Type()
)
pmc2002AlmLineModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineModNrPortn.setStatus("current")
_Pmc2002AlmLineRxCdrNotLockedPortn_Type = EkiOnOff
_Pmc2002AlmLineRxCdrNotLockedPortn_Object = MibTableColumn
pmc2002AlmLineRxCdrNotLockedPortn = _Pmc2002AlmLineRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 4),
    _Pmc2002AlmLineRxCdrNotLockedPortn_Type()
)
pmc2002AlmLineRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineRxCdrNotLockedPortn.setStatus("current")
_Pmc2002AlmLineRxNrPortn_Type = EkiOnOff
_Pmc2002AlmLineRxNrPortn_Object = MibTableColumn
pmc2002AlmLineRxNrPortn = _Pmc2002AlmLineRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 6),
    _Pmc2002AlmLineRxNrPortn_Type()
)
pmc2002AlmLineRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineRxNrPortn.setStatus("current")
_Pmc2002AlmLineTxCdrNotLockedPortn_Type = EkiOnOff
_Pmc2002AlmLineTxCdrNotLockedPortn_Object = MibTableColumn
pmc2002AlmLineTxCdrNotLockedPortn = _Pmc2002AlmLineTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 7),
    _Pmc2002AlmLineTxCdrNotLockedPortn_Type()
)
pmc2002AlmLineTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxCdrNotLockedPortn.setStatus("current")
_Pmc2002AlmLineTxFaultPortn_Type = EkiOnOff
_Pmc2002AlmLineTxFaultPortn_Object = MibTableColumn
pmc2002AlmLineTxFaultPortn = _Pmc2002AlmLineTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 8),
    _Pmc2002AlmLineTxFaultPortn_Type()
)
pmc2002AlmLineTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxFaultPortn.setStatus("current")
_Pmc2002AlmLineTxNrPortn_Type = EkiOnOff
_Pmc2002AlmLineTxNrPortn_Object = MibTableColumn
pmc2002AlmLineTxNrPortn = _Pmc2002AlmLineTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 9),
    _Pmc2002AlmLineTxNrPortn_Type()
)
pmc2002AlmLineTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTxNrPortn.setStatus("current")
_Pmc2002AlmLineWavelengthUnlockedPortn_Type = EkiOnOff
_Pmc2002AlmLineWavelengthUnlockedPortn_Object = MibTableColumn
pmc2002AlmLineWavelengthUnlockedPortn = _Pmc2002AlmLineWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 15),
    _Pmc2002AlmLineWavelengthUnlockedPortn_Type()
)
pmc2002AlmLineWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineWavelengthUnlockedPortn.setStatus("current")
_Pmc2002AlmLineTecFaultPortn_Type = EkiOnOff
_Pmc2002AlmLineTecFaultPortn_Object = MibTableColumn
pmc2002AlmLineTecFaultPortn = _Pmc2002AlmLineTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 16),
    _Pmc2002AlmLineTecFaultPortn_Type()
)
pmc2002AlmLineTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineTecFaultPortn.setStatus("current")
_Pmc2002AlmLineApdSupplyFaultPortn_Type = EkiOnOff
_Pmc2002AlmLineApdSupplyFaultPortn_Object = MibTableColumn
pmc2002AlmLineApdSupplyFaultPortn = _Pmc2002AlmLineApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 2, 3, 3, 211, 1, 17),
    _Pmc2002AlmLineApdSupplyFaultPortn_Type()
)
pmc2002AlmLineApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002AlmLineApdSupplyFaultPortn.setStatus("current")
_Pmc2002measures_ObjectIdentity = ObjectIdentity
pmc2002measures = _Pmc2002measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3)
)
_Pmc2002MesrOther_ObjectIdentity = ObjectIdentity
pmc2002MesrOther = _Pmc2002MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 1)
)
_Pmc2002Mesrsynth0_Type = EkiMeasureType
_Pmc2002Mesrsynth0_Object = MibScalar
pmc2002Mesrsynth0 = _Pmc2002Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 1, 0),
    _Pmc2002Mesrsynth0_Type()
)
pmc2002Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrsynth0.setStatus("deprecated")
_Pmc2002Mesrsynth1_Type = EkiMeasureType
_Pmc2002Mesrsynth1_Object = MibScalar
pmc2002Mesrsynth1 = _Pmc2002Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 1, 1),
    _Pmc2002Mesrsynth1_Type()
)
pmc2002Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrsynth1.setStatus("deprecated")
_Pmc2002MesrClient_ObjectIdentity = ObjectIdentity
pmc2002MesrClient = _Pmc2002MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2)
)
_Pmc2002MesrclientModTempMeasTable_Object = MibTable
pmc2002MesrclientModTempMeasTable = _Pmc2002MesrclientModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmc2002MesrclientModTempMeasTable.setStatus("current")
_Pmc2002MesrclientModTempMeasEntry_Object = MibTableRow
pmc2002MesrclientModTempMeasEntry = _Pmc2002MesrclientModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 16, 1)
)
pmc2002MesrclientModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MesrclientModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MesrclientModTempMeasEntry.setStatus("current")


class _Pmc2002MesrclientModTempMeasIndex_Type(Integer32):
    """Custom type pmc2002MesrclientModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MesrclientModTempMeasIndex_Type.__name__ = "Integer32"
_Pmc2002MesrclientModTempMeasIndex_Object = MibTableColumn
pmc2002MesrclientModTempMeasIndex = _Pmc2002MesrclientModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 16, 1, 1),
    _Pmc2002MesrclientModTempMeasIndex_Type()
)
pmc2002MesrclientModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientModTempMeasIndex.setStatus("current")


class _Pmc2002MesrclientModTempMeasPortn_Type(Integer32):
    """Custom type pmc2002MesrclientModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002MesrclientModTempMeasPortn_Type.__name__ = "Integer32"
_Pmc2002MesrclientModTempMeasPortn_Object = MibTableColumn
pmc2002MesrclientModTempMeasPortn = _Pmc2002MesrclientModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 16, 1, 2),
    _Pmc2002MesrclientModTempMeasPortn_Type()
)
pmc2002MesrclientModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientModTempMeasPortn.setStatus("current")
_Pmc2002MesrclientBiasCurrentMeasTable_Object = MibTable
pmc2002MesrclientBiasCurrentMeasTable = _Pmc2002MesrclientBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmc2002MesrclientBiasCurrentMeasTable.setStatus("current")
_Pmc2002MesrclientBiasCurrentMeasEntry_Object = MibTableRow
pmc2002MesrclientBiasCurrentMeasEntry = _Pmc2002MesrclientBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 32, 1)
)
pmc2002MesrclientBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MesrclientBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MesrclientBiasCurrentMeasEntry.setStatus("current")


class _Pmc2002MesrclientBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pmc2002MesrclientBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MesrclientBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pmc2002MesrclientBiasCurrentMeasIndex_Object = MibTableColumn
pmc2002MesrclientBiasCurrentMeasIndex = _Pmc2002MesrclientBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 32, 1, 1),
    _Pmc2002MesrclientBiasCurrentMeasIndex_Type()
)
pmc2002MesrclientBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientBiasCurrentMeasIndex.setStatus("current")


class _Pmc2002MesrclientBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pmc2002MesrclientBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002MesrclientBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pmc2002MesrclientBiasCurrentMeasPortn_Object = MibTableColumn
pmc2002MesrclientBiasCurrentMeasPortn = _Pmc2002MesrclientBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 32, 1, 2),
    _Pmc2002MesrclientBiasCurrentMeasPortn_Type()
)
pmc2002MesrclientBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientBiasCurrentMeasPortn.setStatus("current")
_Pmc2002MesrclientTxPowerMeasTable_Object = MibTable
pmc2002MesrclientTxPowerMeasTable = _Pmc2002MesrclientTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pmc2002MesrclientTxPowerMeasTable.setStatus("current")
_Pmc2002MesrclientTxPowerMeasEntry_Object = MibTableRow
pmc2002MesrclientTxPowerMeasEntry = _Pmc2002MesrclientTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 40, 1)
)
pmc2002MesrclientTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MesrclientTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MesrclientTxPowerMeasEntry.setStatus("current")


class _Pmc2002MesrclientTxPowerMeasIndex_Type(Integer32):
    """Custom type pmc2002MesrclientTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MesrclientTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc2002MesrclientTxPowerMeasIndex_Object = MibTableColumn
pmc2002MesrclientTxPowerMeasIndex = _Pmc2002MesrclientTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 40, 1, 1),
    _Pmc2002MesrclientTxPowerMeasIndex_Type()
)
pmc2002MesrclientTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientTxPowerMeasIndex.setStatus("current")


class _Pmc2002MesrclientTxPowerMeasPortn_Type(Integer32):
    """Custom type pmc2002MesrclientTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002MesrclientTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc2002MesrclientTxPowerMeasPortn_Object = MibTableColumn
pmc2002MesrclientTxPowerMeasPortn = _Pmc2002MesrclientTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 40, 1, 2),
    _Pmc2002MesrclientTxPowerMeasPortn_Type()
)
pmc2002MesrclientTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientTxPowerMeasPortn.setStatus("current")
_Pmc2002MesrclientRxPowerMeasTable_Object = MibTable
pmc2002MesrclientRxPowerMeasTable = _Pmc2002MesrclientRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmc2002MesrclientRxPowerMeasTable.setStatus("current")
_Pmc2002MesrclientRxPowerMeasEntry_Object = MibTableRow
pmc2002MesrclientRxPowerMeasEntry = _Pmc2002MesrclientRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 48, 1)
)
pmc2002MesrclientRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MesrclientRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MesrclientRxPowerMeasEntry.setStatus("current")


class _Pmc2002MesrclientRxPowerMeasIndex_Type(Integer32):
    """Custom type pmc2002MesrclientRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MesrclientRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc2002MesrclientRxPowerMeasIndex_Object = MibTableColumn
pmc2002MesrclientRxPowerMeasIndex = _Pmc2002MesrclientRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 48, 1, 1),
    _Pmc2002MesrclientRxPowerMeasIndex_Type()
)
pmc2002MesrclientRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientRxPowerMeasIndex.setStatus("current")


class _Pmc2002MesrclientRxPowerMeasPortn_Type(Integer32):
    """Custom type pmc2002MesrclientRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002MesrclientRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc2002MesrclientRxPowerMeasPortn_Object = MibTableColumn
pmc2002MesrclientRxPowerMeasPortn = _Pmc2002MesrclientRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 2, 48, 1, 2),
    _Pmc2002MesrclientRxPowerMeasPortn_Type()
)
pmc2002MesrclientRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MesrclientRxPowerMeasPortn.setStatus("current")
_Pmc2002MesrLine_ObjectIdentity = ObjectIdentity
pmc2002MesrLine = _Pmc2002MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3)
)
_Pmc2002Mesrline1ModTempMeasTable_Object = MibTable
pmc2002Mesrline1ModTempMeasTable = _Pmc2002Mesrline1ModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1ModTempMeasTable.setStatus("current")
_Pmc2002Mesrline1ModTempMeasEntry_Object = MibTableRow
pmc2002Mesrline1ModTempMeasEntry = _Pmc2002Mesrline1ModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 208, 1)
)
pmc2002Mesrline1ModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1ModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1ModTempMeasEntry.setStatus("current")


class _Pmc2002Mesrline1ModTempMeasIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1ModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1ModTempMeasIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1ModTempMeasIndex_Object = MibTableColumn
pmc2002Mesrline1ModTempMeasIndex = _Pmc2002Mesrline1ModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 208, 1, 1),
    _Pmc2002Mesrline1ModTempMeasIndex_Type()
)
pmc2002Mesrline1ModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1ModTempMeasIndex.setStatus("current")


class _Pmc2002Mesrline1ModTempMeasPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1ModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1ModTempMeasPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1ModTempMeasPortn_Object = MibTableColumn
pmc2002Mesrline1ModTempMeasPortn = _Pmc2002Mesrline1ModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 208, 1, 2),
    _Pmc2002Mesrline1ModTempMeasPortn_Type()
)
pmc2002Mesrline1ModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1ModTempMeasPortn.setStatus("current")
_Pmc2002Mesrline1ReservedTable_Object = MibTable
pmc2002Mesrline1ReservedTable = _Pmc2002Mesrline1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1ReservedTable.setStatus("deprecated")
_Pmc2002Mesrline1ReservedEntry_Object = MibTableRow
pmc2002Mesrline1ReservedEntry = _Pmc2002Mesrline1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 209, 1)
)
pmc2002Mesrline1ReservedEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1ReservedEntry.setStatus("deprecated")


class _Pmc2002Mesrline1ReservedIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1ReservedIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1ReservedIndex_Object = MibTableColumn
pmc2002Mesrline1ReservedIndex = _Pmc2002Mesrline1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 209, 1, 1),
    _Pmc2002Mesrline1ReservedIndex_Type()
)
pmc2002Mesrline1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1ReservedIndex.setStatus("deprecated")


class _Pmc2002Mesrline1ReservedPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1ReservedPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1ReservedPortn_Object = MibTableColumn
pmc2002Mesrline1ReservedPortn = _Pmc2002Mesrline1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 209, 1, 2),
    _Pmc2002Mesrline1ReservedPortn_Type()
)
pmc2002Mesrline1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1ReservedPortn.setStatus("deprecated")
_Pmc2002Mesrline1BiasCurrentMeasTable_Object = MibTable
pmc2002Mesrline1BiasCurrentMeasTable = _Pmc2002Mesrline1BiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1BiasCurrentMeasTable.setStatus("current")
_Pmc2002Mesrline1BiasCurrentMeasEntry_Object = MibTableRow
pmc2002Mesrline1BiasCurrentMeasEntry = _Pmc2002Mesrline1BiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 210, 1)
)
pmc2002Mesrline1BiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1BiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1BiasCurrentMeasEntry.setStatus("current")


class _Pmc2002Mesrline1BiasCurrentMeasIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1BiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1BiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1BiasCurrentMeasIndex_Object = MibTableColumn
pmc2002Mesrline1BiasCurrentMeasIndex = _Pmc2002Mesrline1BiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 210, 1, 1),
    _Pmc2002Mesrline1BiasCurrentMeasIndex_Type()
)
pmc2002Mesrline1BiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1BiasCurrentMeasIndex.setStatus("current")


class _Pmc2002Mesrline1BiasCurrentMeasPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1BiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1BiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1BiasCurrentMeasPortn_Object = MibTableColumn
pmc2002Mesrline1BiasCurrentMeasPortn = _Pmc2002Mesrline1BiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 210, 1, 2),
    _Pmc2002Mesrline1BiasCurrentMeasPortn_Type()
)
pmc2002Mesrline1BiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1BiasCurrentMeasPortn.setStatus("current")
_Pmc2002Mesrline1TxPowerMeasTable_Object = MibTable
pmc2002Mesrline1TxPowerMeasTable = _Pmc2002Mesrline1TxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1TxPowerMeasTable.setStatus("current")
_Pmc2002Mesrline1TxPowerMeasEntry_Object = MibTableRow
pmc2002Mesrline1TxPowerMeasEntry = _Pmc2002Mesrline1TxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 211, 1)
)
pmc2002Mesrline1TxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1TxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1TxPowerMeasEntry.setStatus("current")


class _Pmc2002Mesrline1TxPowerMeasIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1TxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1TxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1TxPowerMeasIndex_Object = MibTableColumn
pmc2002Mesrline1TxPowerMeasIndex = _Pmc2002Mesrline1TxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 211, 1, 1),
    _Pmc2002Mesrline1TxPowerMeasIndex_Type()
)
pmc2002Mesrline1TxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1TxPowerMeasIndex.setStatus("current")


class _Pmc2002Mesrline1TxPowerMeasPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1TxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1TxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1TxPowerMeasPortn_Object = MibTableColumn
pmc2002Mesrline1TxPowerMeasPortn = _Pmc2002Mesrline1TxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 211, 1, 2),
    _Pmc2002Mesrline1TxPowerMeasPortn_Type()
)
pmc2002Mesrline1TxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1TxPowerMeasPortn.setStatus("current")
_Pmc2002Mesrline1RxPowerMeasTable_Object = MibTable
pmc2002Mesrline1RxPowerMeasTable = _Pmc2002Mesrline1RxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1RxPowerMeasTable.setStatus("current")
_Pmc2002Mesrline1RxPowerMeasEntry_Object = MibTableRow
pmc2002Mesrline1RxPowerMeasEntry = _Pmc2002Mesrline1RxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 212, 1)
)
pmc2002Mesrline1RxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1RxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1RxPowerMeasEntry.setStatus("current")


class _Pmc2002Mesrline1RxPowerMeasIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1RxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1RxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1RxPowerMeasIndex_Object = MibTableColumn
pmc2002Mesrline1RxPowerMeasIndex = _Pmc2002Mesrline1RxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 212, 1, 1),
    _Pmc2002Mesrline1RxPowerMeasIndex_Type()
)
pmc2002Mesrline1RxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1RxPowerMeasIndex.setStatus("current")


class _Pmc2002Mesrline1RxPowerMeasPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1RxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1RxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1RxPowerMeasPortn_Object = MibTableColumn
pmc2002Mesrline1RxPowerMeasPortn = _Pmc2002Mesrline1RxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 212, 1, 2),
    _Pmc2002Mesrline1RxPowerMeasPortn_Type()
)
pmc2002Mesrline1RxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1RxPowerMeasPortn.setStatus("current")
_Pmc2002Mesrline1Aux1MeasTable_Object = MibTable
pmc2002Mesrline1Aux1MeasTable = _Pmc2002Mesrline1Aux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux1MeasTable.setStatus("deprecated")
_Pmc2002Mesrline1Aux1MeasEntry_Object = MibTableRow
pmc2002Mesrline1Aux1MeasEntry = _Pmc2002Mesrline1Aux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 213, 1)
)
pmc2002Mesrline1Aux1MeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1Aux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux1MeasEntry.setStatus("deprecated")


class _Pmc2002Mesrline1Aux1MeasIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1Aux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1Aux1MeasIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1Aux1MeasIndex_Object = MibTableColumn
pmc2002Mesrline1Aux1MeasIndex = _Pmc2002Mesrline1Aux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 213, 1, 1),
    _Pmc2002Mesrline1Aux1MeasIndex_Type()
)
pmc2002Mesrline1Aux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux1MeasIndex.setStatus("deprecated")


class _Pmc2002Mesrline1Aux1MeasPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1Aux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1Aux1MeasPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1Aux1MeasPortn_Object = MibTableColumn
pmc2002Mesrline1Aux1MeasPortn = _Pmc2002Mesrline1Aux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 213, 1, 2),
    _Pmc2002Mesrline1Aux1MeasPortn_Type()
)
pmc2002Mesrline1Aux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux1MeasPortn.setStatus("deprecated")
_Pmc2002Mesrline1Aux2MeasTable_Object = MibTable
pmc2002Mesrline1Aux2MeasTable = _Pmc2002Mesrline1Aux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux2MeasTable.setStatus("deprecated")
_Pmc2002Mesrline1Aux2MeasEntry_Object = MibTableRow
pmc2002Mesrline1Aux2MeasEntry = _Pmc2002Mesrline1Aux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 214, 1)
)
pmc2002Mesrline1Aux2MeasEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1Aux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux2MeasEntry.setStatus("deprecated")


class _Pmc2002Mesrline1Aux2MeasIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1Aux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1Aux2MeasIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1Aux2MeasIndex_Object = MibTableColumn
pmc2002Mesrline1Aux2MeasIndex = _Pmc2002Mesrline1Aux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 214, 1, 1),
    _Pmc2002Mesrline1Aux2MeasIndex_Type()
)
pmc2002Mesrline1Aux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux2MeasIndex.setStatus("deprecated")


class _Pmc2002Mesrline1Aux2MeasPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1Aux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1Aux2MeasPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1Aux2MeasPortn_Object = MibTableColumn
pmc2002Mesrline1Aux2MeasPortn = _Pmc2002Mesrline1Aux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 214, 1, 2),
    _Pmc2002Mesrline1Aux2MeasPortn_Type()
)
pmc2002Mesrline1Aux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1Aux2MeasPortn.setStatus("deprecated")
_Pmc2002Mesrline1AgingTable_Object = MibTable
pmc2002Mesrline1AgingTable = _Pmc2002Mesrline1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1AgingTable.setStatus("current")
_Pmc2002Mesrline1AgingEntry_Object = MibTableRow
pmc2002Mesrline1AgingEntry = _Pmc2002Mesrline1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 224, 1)
)
pmc2002Mesrline1AgingEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1AgingIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1AgingEntry.setStatus("current")


class _Pmc2002Mesrline1AgingIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1AgingIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1AgingIndex_Object = MibTableColumn
pmc2002Mesrline1AgingIndex = _Pmc2002Mesrline1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 224, 1, 1),
    _Pmc2002Mesrline1AgingIndex_Type()
)
pmc2002Mesrline1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1AgingIndex.setStatus("current")


class _Pmc2002Mesrline1AgingPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1AgingPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1AgingPortn_Object = MibTableColumn
pmc2002Mesrline1AgingPortn = _Pmc2002Mesrline1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 224, 1, 2),
    _Pmc2002Mesrline1AgingPortn_Type()
)
pmc2002Mesrline1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1AgingPortn.setStatus("current")
_Pmc2002Mesrline1LaserTemperatureTable_Object = MibTable
pmc2002Mesrline1LaserTemperatureTable = _Pmc2002Mesrline1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserTemperatureTable.setStatus("deprecated")
_Pmc2002Mesrline1LaserTemperatureEntry_Object = MibTableRow
pmc2002Mesrline1LaserTemperatureEntry = _Pmc2002Mesrline1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 225, 1)
)
pmc2002Mesrline1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserTemperatureEntry.setStatus("deprecated")


class _Pmc2002Mesrline1LaserTemperatureIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1LaserTemperatureIndex_Object = MibTableColumn
pmc2002Mesrline1LaserTemperatureIndex = _Pmc2002Mesrline1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 225, 1, 1),
    _Pmc2002Mesrline1LaserTemperatureIndex_Type()
)
pmc2002Mesrline1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserTemperatureIndex.setStatus("deprecated")


class _Pmc2002Mesrline1LaserTemperaturePortn_Type(Integer32):
    """Custom type pmc2002Mesrline1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1LaserTemperaturePortn_Object = MibTableColumn
pmc2002Mesrline1LaserTemperaturePortn = _Pmc2002Mesrline1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 225, 1, 2),
    _Pmc2002Mesrline1LaserTemperaturePortn_Type()
)
pmc2002Mesrline1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserTemperaturePortn.setStatus("deprecated")
_Pmc2002Mesrline1FreqDeviationTable_Object = MibTable
pmc2002Mesrline1FreqDeviationTable = _Pmc2002Mesrline1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1FreqDeviationTable.setStatus("current")
_Pmc2002Mesrline1FreqDeviationEntry_Object = MibTableRow
pmc2002Mesrline1FreqDeviationEntry = _Pmc2002Mesrline1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 226, 1)
)
pmc2002Mesrline1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1FreqDeviationEntry.setStatus("current")


class _Pmc2002Mesrline1FreqDeviationIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1FreqDeviationIndex_Object = MibTableColumn
pmc2002Mesrline1FreqDeviationIndex = _Pmc2002Mesrline1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 226, 1, 1),
    _Pmc2002Mesrline1FreqDeviationIndex_Type()
)
pmc2002Mesrline1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1FreqDeviationIndex.setStatus("current")


class _Pmc2002Mesrline1FreqDeviationPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1FreqDeviationPortn_Object = MibTableColumn
pmc2002Mesrline1FreqDeviationPortn = _Pmc2002Mesrline1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 226, 1, 2),
    _Pmc2002Mesrline1FreqDeviationPortn_Type()
)
pmc2002Mesrline1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1FreqDeviationPortn.setStatus("current")
_Pmc2002Mesrline1LaserWvlengthTable_Object = MibTable
pmc2002Mesrline1LaserWvlengthTable = _Pmc2002Mesrline1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserWvlengthTable.setStatus("current")
_Pmc2002Mesrline1LaserWvlengthEntry_Object = MibTableRow
pmc2002Mesrline1LaserWvlengthEntry = _Pmc2002Mesrline1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 227, 1)
)
pmc2002Mesrline1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002Mesrline1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserWvlengthEntry.setStatus("current")


class _Pmc2002Mesrline1LaserWvlengthIndex_Type(Integer32):
    """Custom type pmc2002Mesrline1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002Mesrline1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pmc2002Mesrline1LaserWvlengthIndex_Object = MibTableColumn
pmc2002Mesrline1LaserWvlengthIndex = _Pmc2002Mesrline1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 227, 1, 1),
    _Pmc2002Mesrline1LaserWvlengthIndex_Type()
)
pmc2002Mesrline1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserWvlengthIndex.setStatus("current")


class _Pmc2002Mesrline1LaserWvlengthPortn_Type(Integer32):
    """Custom type pmc2002Mesrline1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc2002Mesrline1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pmc2002Mesrline1LaserWvlengthPortn_Object = MibTableColumn
pmc2002Mesrline1LaserWvlengthPortn = _Pmc2002Mesrline1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 3, 3, 227, 1, 2),
    _Pmc2002Mesrline1LaserWvlengthPortn_Type()
)
pmc2002Mesrline1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002Mesrline1LaserWvlengthPortn.setStatus("current")
_Pmc2002counters_ObjectIdentity = ObjectIdentity
pmc2002counters = _Pmc2002counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4)
)
_Pmc2002CntOther_ObjectIdentity = ObjectIdentity
pmc2002CntOther = _Pmc2002CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 1)
)
_Pmc2002CntClient_ObjectIdentity = ObjectIdentity
pmc2002CntClient = _Pmc2002CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2)
)
_Pmc2002CntclientUpErrCntTable_Object = MibTable
pmc2002CntclientUpErrCntTable = _Pmc2002CntclientUpErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pmc2002CntclientUpErrCntTable.setStatus("current")
_Pmc2002CntclientUpErrCntEntry_Object = MibTableRow
pmc2002CntclientUpErrCntEntry = _Pmc2002CntclientUpErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 32, 1)
)
pmc2002CntclientUpErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntclientUpErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntclientUpErrCntEntry.setStatus("current")


class _Pmc2002CntclientUpErrCntIndex_Type(Integer32):
    """Custom type pmc2002CntclientUpErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntclientUpErrCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntclientUpErrCntIndex_Object = MibTableColumn
pmc2002CntclientUpErrCntIndex = _Pmc2002CntclientUpErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 32, 1, 1),
    _Pmc2002CntclientUpErrCntIndex_Type()
)
pmc2002CntclientUpErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpErrCntIndex.setStatus("current")
_Pmc2002CntclientUpErrCntValuePortn_Type = Counter32
_Pmc2002CntclientUpErrCntValuePortn_Object = MibTableColumn
pmc2002CntclientUpErrCntValuePortn = _Pmc2002CntclientUpErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 32, 1, 2),
    _Pmc2002CntclientUpErrCntValuePortn_Type()
)
pmc2002CntclientUpErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpErrCntValuePortn.setStatus("current")
_Pmc2002CntclientUpErrCntErrorPortn_Type = EkiOnOff
_Pmc2002CntclientUpErrCntErrorPortn_Object = MibTableColumn
pmc2002CntclientUpErrCntErrorPortn = _Pmc2002CntclientUpErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 32, 1, 3),
    _Pmc2002CntclientUpErrCntErrorPortn_Type()
)
pmc2002CntclientUpErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpErrCntErrorPortn.setStatus("current")
_Pmc2002CntclientUpErrCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntclientUpErrCntOverloadPortn_Object = MibTableColumn
pmc2002CntclientUpErrCntOverloadPortn = _Pmc2002CntclientUpErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 32, 1, 4),
    _Pmc2002CntclientUpErrCntOverloadPortn_Type()
)
pmc2002CntclientUpErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpErrCntOverloadPortn.setStatus("current")
_Pmc2002CntclientUpTimCntTable_Object = MibTable
pmc2002CntclientUpTimCntTable = _Pmc2002CntclientUpTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pmc2002CntclientUpTimCntTable.setStatus("current")
_Pmc2002CntclientUpTimCntEntry_Object = MibTableRow
pmc2002CntclientUpTimCntEntry = _Pmc2002CntclientUpTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 40, 1)
)
pmc2002CntclientUpTimCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntclientUpTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntclientUpTimCntEntry.setStatus("current")


class _Pmc2002CntclientUpTimCntIndex_Type(Integer32):
    """Custom type pmc2002CntclientUpTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntclientUpTimCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntclientUpTimCntIndex_Object = MibTableColumn
pmc2002CntclientUpTimCntIndex = _Pmc2002CntclientUpTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 40, 1, 1),
    _Pmc2002CntclientUpTimCntIndex_Type()
)
pmc2002CntclientUpTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpTimCntIndex.setStatus("current")
_Pmc2002CntclientUpTimCntValuePortn_Type = Counter32
_Pmc2002CntclientUpTimCntValuePortn_Object = MibTableColumn
pmc2002CntclientUpTimCntValuePortn = _Pmc2002CntclientUpTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 40, 1, 2),
    _Pmc2002CntclientUpTimCntValuePortn_Type()
)
pmc2002CntclientUpTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpTimCntValuePortn.setStatus("current")
_Pmc2002CntclientUpTimCntErrorPortn_Type = EkiOnOff
_Pmc2002CntclientUpTimCntErrorPortn_Object = MibTableColumn
pmc2002CntclientUpTimCntErrorPortn = _Pmc2002CntclientUpTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 40, 1, 3),
    _Pmc2002CntclientUpTimCntErrorPortn_Type()
)
pmc2002CntclientUpTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpTimCntErrorPortn.setStatus("current")
_Pmc2002CntclientUpTimCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntclientUpTimCntOverloadPortn_Object = MibTableColumn
pmc2002CntclientUpTimCntOverloadPortn = _Pmc2002CntclientUpTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 40, 1, 4),
    _Pmc2002CntclientUpTimCntOverloadPortn_Type()
)
pmc2002CntclientUpTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientUpTimCntOverloadPortn.setStatus("current")
_Pmc2002CntclientDwErrCntTable_Object = MibTable
pmc2002CntclientDwErrCntTable = _Pmc2002CntclientDwErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pmc2002CntclientDwErrCntTable.setStatus("current")
_Pmc2002CntclientDwErrCntEntry_Object = MibTableRow
pmc2002CntclientDwErrCntEntry = _Pmc2002CntclientDwErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 64, 1)
)
pmc2002CntclientDwErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntclientDwErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntclientDwErrCntEntry.setStatus("current")


class _Pmc2002CntclientDwErrCntIndex_Type(Integer32):
    """Custom type pmc2002CntclientDwErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntclientDwErrCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntclientDwErrCntIndex_Object = MibTableColumn
pmc2002CntclientDwErrCntIndex = _Pmc2002CntclientDwErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 64, 1, 1),
    _Pmc2002CntclientDwErrCntIndex_Type()
)
pmc2002CntclientDwErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwErrCntIndex.setStatus("current")
_Pmc2002CntclientDwErrCntValuePortn_Type = Counter32
_Pmc2002CntclientDwErrCntValuePortn_Object = MibTableColumn
pmc2002CntclientDwErrCntValuePortn = _Pmc2002CntclientDwErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 64, 1, 2),
    _Pmc2002CntclientDwErrCntValuePortn_Type()
)
pmc2002CntclientDwErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwErrCntValuePortn.setStatus("current")
_Pmc2002CntclientDwErrCntErrorPortn_Type = EkiOnOff
_Pmc2002CntclientDwErrCntErrorPortn_Object = MibTableColumn
pmc2002CntclientDwErrCntErrorPortn = _Pmc2002CntclientDwErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 64, 1, 3),
    _Pmc2002CntclientDwErrCntErrorPortn_Type()
)
pmc2002CntclientDwErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwErrCntErrorPortn.setStatus("current")
_Pmc2002CntclientDwErrCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntclientDwErrCntOverloadPortn_Object = MibTableColumn
pmc2002CntclientDwErrCntOverloadPortn = _Pmc2002CntclientDwErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 64, 1, 4),
    _Pmc2002CntclientDwErrCntOverloadPortn_Type()
)
pmc2002CntclientDwErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwErrCntOverloadPortn.setStatus("current")
_Pmc2002CntclientDwTimCntTable_Object = MibTable
pmc2002CntclientDwTimCntTable = _Pmc2002CntclientDwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pmc2002CntclientDwTimCntTable.setStatus("current")
_Pmc2002CntclientDwTimCntEntry_Object = MibTableRow
pmc2002CntclientDwTimCntEntry = _Pmc2002CntclientDwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 72, 1)
)
pmc2002CntclientDwTimCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntclientDwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntclientDwTimCntEntry.setStatus("current")


class _Pmc2002CntclientDwTimCntIndex_Type(Integer32):
    """Custom type pmc2002CntclientDwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntclientDwTimCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntclientDwTimCntIndex_Object = MibTableColumn
pmc2002CntclientDwTimCntIndex = _Pmc2002CntclientDwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 72, 1, 1),
    _Pmc2002CntclientDwTimCntIndex_Type()
)
pmc2002CntclientDwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwTimCntIndex.setStatus("current")
_Pmc2002CntclientDwTimCntValuePortn_Type = Counter32
_Pmc2002CntclientDwTimCntValuePortn_Object = MibTableColumn
pmc2002CntclientDwTimCntValuePortn = _Pmc2002CntclientDwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 72, 1, 2),
    _Pmc2002CntclientDwTimCntValuePortn_Type()
)
pmc2002CntclientDwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwTimCntValuePortn.setStatus("current")
_Pmc2002CntclientDwTimCntErrorPortn_Type = EkiOnOff
_Pmc2002CntclientDwTimCntErrorPortn_Object = MibTableColumn
pmc2002CntclientDwTimCntErrorPortn = _Pmc2002CntclientDwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 72, 1, 3),
    _Pmc2002CntclientDwTimCntErrorPortn_Type()
)
pmc2002CntclientDwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwTimCntErrorPortn.setStatus("current")
_Pmc2002CntclientDwTimCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntclientDwTimCntOverloadPortn_Object = MibTableColumn
pmc2002CntclientDwTimCntOverloadPortn = _Pmc2002CntclientDwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 2, 72, 1, 4),
    _Pmc2002CntclientDwTimCntOverloadPortn_Type()
)
pmc2002CntclientDwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntclientDwTimCntOverloadPortn.setStatus("current")
_Pmc2002CntLine_ObjectIdentity = ObjectIdentity
pmc2002CntLine = _Pmc2002CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3)
)
_Pmc2002CntlineDfrmErrCntTable_Object = MibTable
pmc2002CntlineDfrmErrCntTable = _Pmc2002CntlineDfrmErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmErrCntTable.setStatus("current")
_Pmc2002CntlineDfrmErrCntEntry_Object = MibTableRow
pmc2002CntlineDfrmErrCntEntry = _Pmc2002CntlineDfrmErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 152, 1)
)
pmc2002CntlineDfrmErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntlineDfrmErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmErrCntEntry.setStatus("current")


class _Pmc2002CntlineDfrmErrCntIndex_Type(Integer32):
    """Custom type pmc2002CntlineDfrmErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntlineDfrmErrCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntlineDfrmErrCntIndex_Object = MibTableColumn
pmc2002CntlineDfrmErrCntIndex = _Pmc2002CntlineDfrmErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 152, 1, 1),
    _Pmc2002CntlineDfrmErrCntIndex_Type()
)
pmc2002CntlineDfrmErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmErrCntIndex.setStatus("current")
_Pmc2002CntlineDfrmErrCntValuePortn_Type = Counter32
_Pmc2002CntlineDfrmErrCntValuePortn_Object = MibTableColumn
pmc2002CntlineDfrmErrCntValuePortn = _Pmc2002CntlineDfrmErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 152, 1, 2),
    _Pmc2002CntlineDfrmErrCntValuePortn_Type()
)
pmc2002CntlineDfrmErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmErrCntValuePortn.setStatus("current")
_Pmc2002CntlineDfrmErrCntErrorPortn_Type = EkiOnOff
_Pmc2002CntlineDfrmErrCntErrorPortn_Object = MibTableColumn
pmc2002CntlineDfrmErrCntErrorPortn = _Pmc2002CntlineDfrmErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 152, 1, 3),
    _Pmc2002CntlineDfrmErrCntErrorPortn_Type()
)
pmc2002CntlineDfrmErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmErrCntErrorPortn.setStatus("current")
_Pmc2002CntlineDfrmErrCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntlineDfrmErrCntOverloadPortn_Object = MibTableColumn
pmc2002CntlineDfrmErrCntOverloadPortn = _Pmc2002CntlineDfrmErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 152, 1, 4),
    _Pmc2002CntlineDfrmErrCntOverloadPortn_Type()
)
pmc2002CntlineDfrmErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmErrCntOverloadPortn.setStatus("current")
_Pmc2002CntlineDfrmTimCntTable_Object = MibTable
pmc2002CntlineDfrmTimCntTable = _Pmc2002CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmTimCntTable.setStatus("current")
_Pmc2002CntlineDfrmTimCntEntry_Object = MibTableRow
pmc2002CntlineDfrmTimCntEntry = _Pmc2002CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 153, 1)
)
pmc2002CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmTimCntEntry.setStatus("current")


class _Pmc2002CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pmc2002CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntlineDfrmTimCntIndex_Object = MibTableColumn
pmc2002CntlineDfrmTimCntIndex = _Pmc2002CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 153, 1, 1),
    _Pmc2002CntlineDfrmTimCntIndex_Type()
)
pmc2002CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmTimCntIndex.setStatus("current")
_Pmc2002CntlineDfrmTimCntValuePortn_Type = Counter32
_Pmc2002CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pmc2002CntlineDfrmTimCntValuePortn = _Pmc2002CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 153, 1, 2),
    _Pmc2002CntlineDfrmTimCntValuePortn_Type()
)
pmc2002CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmTimCntValuePortn.setStatus("current")
_Pmc2002CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pmc2002CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pmc2002CntlineDfrmTimCntErrorPortn = _Pmc2002CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 153, 1, 3),
    _Pmc2002CntlineDfrmTimCntErrorPortn_Type()
)
pmc2002CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pmc2002CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pmc2002CntlineDfrmTimCntOverloadPortn = _Pmc2002CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 153, 1, 4),
    _Pmc2002CntlineDfrmTimCntOverloadPortn_Type()
)
pmc2002CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pmc2002CntlineDfrmPrimErrCntTable_Object = MibTable
pmc2002CntlineDfrmPrimErrCntTable = _Pmc2002CntlineDfrmPrimErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmPrimErrCntTable.setStatus("current")
_Pmc2002CntlineDfrmPrimErrCntEntry_Object = MibTableRow
pmc2002CntlineDfrmPrimErrCntEntry = _Pmc2002CntlineDfrmPrimErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 154, 1)
)
pmc2002CntlineDfrmPrimErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CntlineDfrmPrimErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmPrimErrCntEntry.setStatus("current")


class _Pmc2002CntlineDfrmPrimErrCntIndex_Type(Integer32):
    """Custom type pmc2002CntlineDfrmPrimErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CntlineDfrmPrimErrCntIndex_Type.__name__ = "Integer32"
_Pmc2002CntlineDfrmPrimErrCntIndex_Object = MibTableColumn
pmc2002CntlineDfrmPrimErrCntIndex = _Pmc2002CntlineDfrmPrimErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 154, 1, 1),
    _Pmc2002CntlineDfrmPrimErrCntIndex_Type()
)
pmc2002CntlineDfrmPrimErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmPrimErrCntIndex.setStatus("current")
_Pmc2002CntlineDfrmPrimErrCntValuePortn_Type = Counter32
_Pmc2002CntlineDfrmPrimErrCntValuePortn_Object = MibTableColumn
pmc2002CntlineDfrmPrimErrCntValuePortn = _Pmc2002CntlineDfrmPrimErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 154, 1, 2),
    _Pmc2002CntlineDfrmPrimErrCntValuePortn_Type()
)
pmc2002CntlineDfrmPrimErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmPrimErrCntValuePortn.setStatus("current")
_Pmc2002CntlineDfrmPrimErrCntErrorPortn_Type = EkiOnOff
_Pmc2002CntlineDfrmPrimErrCntErrorPortn_Object = MibTableColumn
pmc2002CntlineDfrmPrimErrCntErrorPortn = _Pmc2002CntlineDfrmPrimErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 154, 1, 3),
    _Pmc2002CntlineDfrmPrimErrCntErrorPortn_Type()
)
pmc2002CntlineDfrmPrimErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmPrimErrCntErrorPortn.setStatus("current")
_Pmc2002CntlineDfrmPrimErrCntOverloadPortn_Type = EkiOnOff
_Pmc2002CntlineDfrmPrimErrCntOverloadPortn_Object = MibTableColumn
pmc2002CntlineDfrmPrimErrCntOverloadPortn = _Pmc2002CntlineDfrmPrimErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 3, 154, 1, 4),
    _Pmc2002CntlineDfrmPrimErrCntOverloadPortn_Type()
)
pmc2002CntlineDfrmPrimErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CntlineDfrmPrimErrCntOverloadPortn.setStatus("current")
_Pmc2002CntCountersReset_Type = EkiOnOff
_Pmc2002CntCountersReset_Object = MibScalar
pmc2002CntCountersReset = _Pmc2002CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 259),
    _Pmc2002CntCountersReset_Type()
)
pmc2002CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CntCountersReset.setStatus("current")
_Pmc2002CntCountersStop_Type = EkiOnOff
_Pmc2002CntCountersStop_Object = MibScalar
pmc2002CntCountersStop = _Pmc2002CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 4, 260),
    _Pmc2002CntCountersStop_Type()
)
pmc2002CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CntCountersStop.setStatus("current")
_Pmc2002controlsWrite_ObjectIdentity = ObjectIdentity
pmc2002controlsWrite = _Pmc2002controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6)
)
_Pmc2002CtrlOther_ObjectIdentity = ObjectIdentity
pmc2002CtrlOther = _Pmc2002CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1)
)
_Pmc2002CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmc2002CtrlconfMgnt1 = _Pmc2002CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 1)
)
_Pmc2002CtrlConf1Load1_Type = EkiOnOff
_Pmc2002CtrlConf1Load1_Object = MibScalar
pmc2002CtrlConf1Load1 = _Pmc2002CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 1, 1),
    _Pmc2002CtrlConf1Load1_Type()
)
pmc2002CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlConf1Load1.setStatus("current")
_Pmc2002CtrlConf2Load1_Type = EkiOnOff
_Pmc2002CtrlConf2Load1_Object = MibScalar
pmc2002CtrlConf2Load1 = _Pmc2002CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 1, 2),
    _Pmc2002CtrlConf2Load1_Type()
)
pmc2002CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlConf2Load1.setStatus("current")
_Pmc2002CtrlConf2Flash1_Type = EkiOnOff
_Pmc2002CtrlConf2Flash1_Object = MibScalar
pmc2002CtrlConf2Flash1 = _Pmc2002CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 1, 10),
    _Pmc2002CtrlConf2Flash1_Type()
)
pmc2002CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlConf2Flash1.setStatus("current")
_Pmc2002CtrlConf2Clear1_Type = EkiOnOff
_Pmc2002CtrlConf2Clear1_Object = MibScalar
pmc2002CtrlConf2Clear1 = _Pmc2002CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 1, 14),
    _Pmc2002CtrlConf2Clear1_Type()
)
pmc2002CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlConf2Clear1.setStatus("current")
_Pmc2002Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmc2002Ctrlsynth4 = _Pmc2002Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 4)
)
_Pmc2002CtrlCorrelatOn_Type = EkiOnOff
_Pmc2002CtrlCorrelatOn_Object = MibScalar
pmc2002CtrlCorrelatOn = _Pmc2002CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 4, 1),
    _Pmc2002CtrlCorrelatOn_Type()
)
pmc2002CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlCorrelatOn.setStatus("current")
_Pmc2002CtrlCorrelatOff_Type = EkiOnOff
_Pmc2002CtrlCorrelatOff_Object = MibScalar
pmc2002CtrlCorrelatOff = _Pmc2002CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 4, 2),
    _Pmc2002CtrlCorrelatOff_Type()
)
pmc2002CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlCorrelatOff.setStatus("current")
_Pmc2002CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmc2002CtrlswMgnt = _Pmc2002CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 5)
)
_Pmc2002CtrlColdReset_Type = EkiOnOff
_Pmc2002CtrlColdReset_Object = MibScalar
pmc2002CtrlColdReset = _Pmc2002CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 5, 2),
    _Pmc2002CtrlColdReset_Type()
)
pmc2002CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlColdReset.setStatus("current")
_Pmc2002CtrlWarmReset_Type = EkiOnOff
_Pmc2002CtrlWarmReset_Object = MibScalar
pmc2002CtrlWarmReset = _Pmc2002CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 5, 3),
    _Pmc2002CtrlWarmReset_Type()
)
pmc2002CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlWarmReset.setStatus("current")
_Pmc2002CtrlLoadSwBank1_Type = EkiOnOff
_Pmc2002CtrlLoadSwBank1_Object = MibScalar
pmc2002CtrlLoadSwBank1 = _Pmc2002CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 5, 5),
    _Pmc2002CtrlLoadSwBank1_Type()
)
pmc2002CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLoadSwBank1.setStatus("current")
_Pmc2002CtrlLoadSwBank2_Type = EkiOnOff
_Pmc2002CtrlLoadSwBank2_Object = MibScalar
pmc2002CtrlLoadSwBank2 = _Pmc2002CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 5, 6),
    _Pmc2002CtrlLoadSwBank2_Type()
)
pmc2002CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLoadSwBank2.setStatus("current")
_Pmc2002CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmc2002CtrlgwMgnt = _Pmc2002CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 6)
)
_Pmc2002CtrlCurrentGwReset_Type = EkiOnOff
_Pmc2002CtrlCurrentGwReset_Object = MibScalar
pmc2002CtrlCurrentGwReset = _Pmc2002CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 6, 1),
    _Pmc2002CtrlCurrentGwReset_Type()
)
pmc2002CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlCurrentGwReset.setStatus("current")
_Pmc2002CtrlLoadGwBank1_Type = EkiOnOff
_Pmc2002CtrlLoadGwBank1_Object = MibScalar
pmc2002CtrlLoadGwBank1 = _Pmc2002CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 6, 5),
    _Pmc2002CtrlLoadGwBank1_Type()
)
pmc2002CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLoadGwBank1.setStatus("current")
_Pmc2002CtrlLoadGwBank2_Type = EkiOnOff
_Pmc2002CtrlLoadGwBank2_Object = MibScalar
pmc2002CtrlLoadGwBank2 = _Pmc2002CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 6, 6),
    _Pmc2002CtrlLoadGwBank2_Type()
)
pmc2002CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLoadGwBank2.setStatus("current")
_Pmc2002CtrlLoadGwBank3_Type = EkiOnOff
_Pmc2002CtrlLoadGwBank3_Object = MibScalar
pmc2002CtrlLoadGwBank3 = _Pmc2002CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 6, 7),
    _Pmc2002CtrlLoadGwBank3_Type()
)
pmc2002CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLoadGwBank3.setStatus("current")
_Pmc2002CtrlLoadGwBank4_Type = EkiOnOff
_Pmc2002CtrlLoadGwBank4_Object = MibScalar
pmc2002CtrlLoadGwBank4 = _Pmc2002CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 6, 8),
    _Pmc2002CtrlLoadGwBank4_Type()
)
pmc2002CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLoadGwBank4.setStatus("current")
_Pmc2002CtrlledTest_ObjectIdentity = ObjectIdentity
pmc2002CtrlledTest = _Pmc2002CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 192)
)
_Pmc2002CtrlGreenLed_Type = EkiOnOff
_Pmc2002CtrlGreenLed_Object = MibScalar
pmc2002CtrlGreenLed = _Pmc2002CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 192, 1),
    _Pmc2002CtrlGreenLed_Type()
)
pmc2002CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlGreenLed.setStatus("current")
_Pmc2002CtrlRedLed_Type = EkiOnOff
_Pmc2002CtrlRedLed_Object = MibScalar
pmc2002CtrlRedLed = _Pmc2002CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 192, 2),
    _Pmc2002CtrlRedLed_Type()
)
pmc2002CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlRedLed.setStatus("current")
_Pmc2002CtrlLedOff_Type = EkiOnOff
_Pmc2002CtrlLedOff_Object = MibScalar
pmc2002CtrlLedOff = _Pmc2002CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 192, 3),
    _Pmc2002CtrlLedOff_Type()
)
pmc2002CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlLedOff.setStatus("current")
_Pmc2002CtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pmc2002CtrlmoduleOosMode = _Pmc2002CtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 193)
)
_Pmc2002CtrlModuleOosMode_Type = EkiOnOff
_Pmc2002CtrlModuleOosMode_Object = MibScalar
pmc2002CtrlModuleOosMode = _Pmc2002CtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 193, 1),
    _Pmc2002CtrlModuleOosMode_Type()
)
pmc2002CtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlModuleOosMode.setStatus("current")
_Pmc2002CtrlmoduleDccMgnt_Type = Pmc2002DccMode
_Pmc2002CtrlmoduleDccMgnt_Object = MibScalar
pmc2002CtrlmoduleDccMgnt = _Pmc2002CtrlmoduleDccMgnt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 196),
    _Pmc2002CtrlmoduleDccMgnt_Type()
)
pmc2002CtrlmoduleDccMgnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlmoduleDccMgnt.setStatus("current")
_Pmc2002CtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pmc2002CtrlmaintenanceMode = _Pmc2002CtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 197)
)
_Pmc2002CtrlMaintenanceMode_Type = EkiOnOff
_Pmc2002CtrlMaintenanceMode_Object = MibScalar
pmc2002CtrlMaintenanceMode = _Pmc2002CtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 1, 197, 1),
    _Pmc2002CtrlMaintenanceMode_Type()
)
pmc2002CtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlMaintenanceMode.setStatus("current")
_Pmc2002CtrlClient_ObjectIdentity = ObjectIdentity
pmc2002CtrlClient = _Pmc2002CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2)
)
_Pmc2002CtrlaccessLoopTable_Object = MibTable
pmc2002CtrlaccessLoopTable = _Pmc2002CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmc2002CtrlaccessLoopTable.setStatus("current")
_Pmc2002CtrlaccessLoopEntry_Object = MibTableRow
pmc2002CtrlaccessLoopEntry = _Pmc2002CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 16, 1)
)
pmc2002CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlaccessLoopEntry.setStatus("current")


class _Pmc2002CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pmc2002CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlaccessLoopIndex_Object = MibTableColumn
pmc2002CtrlaccessLoopIndex = _Pmc2002CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 16, 1, 1),
    _Pmc2002CtrlaccessLoopIndex_Type()
)
pmc2002CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlaccessLoopIndex.setStatus("current")
_Pmc2002CtrlaccessLoopPortn_Type = EkiState
_Pmc2002CtrlaccessLoopPortn_Object = MibTableColumn
pmc2002CtrlaccessLoopPortn = _Pmc2002CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 16, 1, 2),
    _Pmc2002CtrlaccessLoopPortn_Type()
)
pmc2002CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlaccessLoopPortn.setStatus("current")
_Pmc2002CtrlportOosModeTable_Object = MibTable
pmc2002CtrlportOosModeTable = _Pmc2002CtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pmc2002CtrlportOosModeTable.setStatus("current")
_Pmc2002CtrlportOosModeEntry_Object = MibTableRow
pmc2002CtrlportOosModeEntry = _Pmc2002CtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 18, 1)
)
pmc2002CtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlportOosModeEntry.setStatus("current")


class _Pmc2002CtrlportOosModeIndex_Type(Integer32):
    """Custom type pmc2002CtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlportOosModeIndex_Object = MibTableColumn
pmc2002CtrlportOosModeIndex = _Pmc2002CtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 18, 1, 1),
    _Pmc2002CtrlportOosModeIndex_Type()
)
pmc2002CtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlportOosModeIndex.setStatus("current")
_Pmc2002CtrlportOosModePortn_Type = EkiState
_Pmc2002CtrlportOosModePortn_Object = MibTableColumn
pmc2002CtrlportOosModePortn = _Pmc2002CtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 18, 1, 2),
    _Pmc2002CtrlportOosModePortn_Type()
)
pmc2002CtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlportOosModePortn.setStatus("current")
_Pmc2002CtrlsfpOffCtrlTable_Object = MibTable
pmc2002CtrlsfpOffCtrlTable = _Pmc2002CtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pmc2002CtrlsfpOffCtrlTable.setStatus("current")
_Pmc2002CtrlsfpOffCtrlEntry_Object = MibTableRow
pmc2002CtrlsfpOffCtrlEntry = _Pmc2002CtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 20, 1)
)
pmc2002CtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlsfpOffCtrlEntry.setStatus("current")


class _Pmc2002CtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pmc2002CtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlsfpOffCtrlIndex_Object = MibTableColumn
pmc2002CtrlsfpOffCtrlIndex = _Pmc2002CtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 20, 1, 1),
    _Pmc2002CtrlsfpOffCtrlIndex_Type()
)
pmc2002CtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlsfpOffCtrlIndex.setStatus("current")
_Pmc2002CtrlsfpOffCtrlPortn_Type = EkiState
_Pmc2002CtrlsfpOffCtrlPortn_Object = MibTableColumn
pmc2002CtrlsfpOffCtrlPortn = _Pmc2002CtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 20, 1, 2),
    _Pmc2002CtrlsfpOffCtrlPortn_Type()
)
pmc2002CtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlsfpOffCtrlPortn.setStatus("current")
_Pmc2002CtrlcsfUpInsTable_Object = MibTable
pmc2002CtrlcsfUpInsTable = _Pmc2002CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pmc2002CtrlcsfUpInsTable.setStatus("current")
_Pmc2002CtrlcsfUpInsEntry_Object = MibTableRow
pmc2002CtrlcsfUpInsEntry = _Pmc2002CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 21, 1)
)
pmc2002CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlcsfUpInsEntry.setStatus("current")


class _Pmc2002CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pmc2002CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlcsfUpInsIndex_Object = MibTableColumn
pmc2002CtrlcsfUpInsIndex = _Pmc2002CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 21, 1, 1),
    _Pmc2002CtrlcsfUpInsIndex_Type()
)
pmc2002CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlcsfUpInsIndex.setStatus("current")
_Pmc2002CtrlcsfUpInsPortn_Type = EkiState
_Pmc2002CtrlcsfUpInsPortn_Object = MibTableColumn
pmc2002CtrlcsfUpInsPortn = _Pmc2002CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 21, 1, 2),
    _Pmc2002CtrlcsfUpInsPortn_Type()
)
pmc2002CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlcsfUpInsPortn.setStatus("current")
_Pmc2002CtrlcaisDwInsTable_Object = MibTable
pmc2002CtrlcaisDwInsTable = _Pmc2002CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pmc2002CtrlcaisDwInsTable.setStatus("current")
_Pmc2002CtrlcaisDwInsEntry_Object = MibTableRow
pmc2002CtrlcaisDwInsEntry = _Pmc2002CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 22, 1)
)
pmc2002CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlcaisDwInsEntry.setStatus("current")


class _Pmc2002CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pmc2002CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlcaisDwInsIndex_Object = MibTableColumn
pmc2002CtrlcaisDwInsIndex = _Pmc2002CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 22, 1, 1),
    _Pmc2002CtrlcaisDwInsIndex_Type()
)
pmc2002CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlcaisDwInsIndex.setStatus("current")
_Pmc2002CtrlcaisDwInsPortn_Type = EkiState
_Pmc2002CtrlcaisDwInsPortn_Object = MibTableColumn
pmc2002CtrlcaisDwInsPortn = _Pmc2002CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 22, 1, 2),
    _Pmc2002CtrlcaisDwInsPortn_Type()
)
pmc2002CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlcaisDwInsPortn.setStatus("current")
_Pmc2002CtrlclientAccessTermLoopTable_Object = MibTable
pmc2002CtrlclientAccessTermLoopTable = _Pmc2002CtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pmc2002CtrlclientAccessTermLoopTable.setStatus("current")
_Pmc2002CtrlclientAccessTermLoopEntry_Object = MibTableRow
pmc2002CtrlclientAccessTermLoopEntry = _Pmc2002CtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 26, 1)
)
pmc2002CtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlclientAccessTermLoopEntry.setStatus("current")


class _Pmc2002CtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pmc2002CtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlclientAccessTermLoopIndex_Object = MibTableColumn
pmc2002CtrlclientAccessTermLoopIndex = _Pmc2002CtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 26, 1, 1),
    _Pmc2002CtrlclientAccessTermLoopIndex_Type()
)
pmc2002CtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlclientAccessTermLoopIndex.setStatus("current")
_Pmc2002CtrlclientAccessTermLoopPortn_Type = EkiState
_Pmc2002CtrlclientAccessTermLoopPortn_Object = MibTableColumn
pmc2002CtrlclientAccessTermLoopPortn = _Pmc2002CtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 26, 1, 2),
    _Pmc2002CtrlclientAccessTermLoopPortn_Type()
)
pmc2002CtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlclientAccessTermLoopPortn.setStatus("current")
_Pmc2002CtrlprotocolTable_Object = MibTable
pmc2002CtrlprotocolTable = _Pmc2002CtrlprotocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 52)
)
if mibBuilder.loadTexts:
    pmc2002CtrlprotocolTable.setStatus("current")
_Pmc2002CtrlprotocolEntry_Object = MibTableRow
pmc2002CtrlprotocolEntry = _Pmc2002CtrlprotocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 52, 1)
)
pmc2002CtrlprotocolEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlprotocolIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlprotocolEntry.setStatus("current")


class _Pmc2002CtrlprotocolIndex_Type(Integer32):
    """Custom type pmc2002CtrlprotocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlprotocolIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlprotocolIndex_Object = MibTableColumn
pmc2002CtrlprotocolIndex = _Pmc2002CtrlprotocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 52, 1, 1),
    _Pmc2002CtrlprotocolIndex_Type()
)
pmc2002CtrlprotocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlprotocolIndex.setStatus("current")
_Pmc2002CtrlprotocolPortn_Type = EkiProtocol
_Pmc2002CtrlprotocolPortn_Object = MibTableColumn
pmc2002CtrlprotocolPortn = _Pmc2002CtrlprotocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 52, 1, 2),
    _Pmc2002CtrlprotocolPortn_Type()
)
pmc2002CtrlprotocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlprotocolPortn.setStatus("current")
_Pmc2002CtrlclientResetAllCountTable_Object = MibTable
pmc2002CtrlclientResetAllCountTable = _Pmc2002CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 271)
)
if mibBuilder.loadTexts:
    pmc2002CtrlclientResetAllCountTable.setStatus("current")
_Pmc2002CtrlclientResetAllCountEntry_Object = MibTableRow
pmc2002CtrlclientResetAllCountEntry = _Pmc2002CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 271, 1)
)
pmc2002CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlclientResetAllCountEntry.setStatus("current")


class _Pmc2002CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pmc2002CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlclientResetAllCountIndex_Object = MibTableColumn
pmc2002CtrlclientResetAllCountIndex = _Pmc2002CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 271, 1, 1),
    _Pmc2002CtrlclientResetAllCountIndex_Type()
)
pmc2002CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlclientResetAllCountIndex.setStatus("current")
_Pmc2002CtrlclientResetAllCountsPortn_Type = EkiState
_Pmc2002CtrlclientResetAllCountsPortn_Object = MibTableColumn
pmc2002CtrlclientResetAllCountsPortn = _Pmc2002CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 2, 271, 1, 2),
    _Pmc2002CtrlclientResetAllCountsPortn_Type()
)
pmc2002CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlclientResetAllCountsPortn.setStatus("current")
_Pmc2002CtrlLine_ObjectIdentity = ObjectIdentity
pmc2002CtrlLine = _Pmc2002CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3)
)
_Pmc2002CtrlcommAccessLoopTable_Object = MibTable
pmc2002CtrlcommAccessLoopTable = _Pmc2002CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pmc2002CtrlcommAccessLoopTable.setStatus("deprecated")
_Pmc2002CtrlcommAccessLoopEntry_Object = MibTableRow
pmc2002CtrlcommAccessLoopEntry = _Pmc2002CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 64, 1)
)
pmc2002CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlcommAccessLoopEntry.setStatus("deprecated")


class _Pmc2002CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pmc2002CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlcommAccessLoopIndex_Object = MibTableColumn
pmc2002CtrlcommAccessLoopIndex = _Pmc2002CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 64, 1, 1),
    _Pmc2002CtrlcommAccessLoopIndex_Type()
)
pmc2002CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlcommAccessLoopIndex.setStatus("deprecated")
_Pmc2002CtrlcommAccessLoopPortn_Type = EkiState
_Pmc2002CtrlcommAccessLoopPortn_Object = MibTableColumn
pmc2002CtrlcommAccessLoopPortn = _Pmc2002CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 64, 1, 2),
    _Pmc2002CtrlcommAccessLoopPortn_Type()
)
pmc2002CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlcommAccessLoopPortn.setStatus("deprecated")
_Pmc2002CtrllineLoopTable_Object = MibTable
pmc2002CtrllineLoopTable = _Pmc2002CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopTable.setStatus("current")
_Pmc2002CtrllineLoopEntry_Object = MibTableRow
pmc2002CtrllineLoopEntry = _Pmc2002CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 66, 1)
)
pmc2002CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopEntry.setStatus("current")


class _Pmc2002CtrllineLoopIndex_Type(Integer32):
    """Custom type pmc2002CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllineLoopIndex_Object = MibTableColumn
pmc2002CtrllineLoopIndex = _Pmc2002CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 66, 1, 1),
    _Pmc2002CtrllineLoopIndex_Type()
)
pmc2002CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopIndex.setStatus("current")
_Pmc2002CtrllineLoopPortn_Type = EkiState
_Pmc2002CtrllineLoopPortn_Object = MibTableColumn
pmc2002CtrllineLoopPortn = _Pmc2002CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 66, 1, 2),
    _Pmc2002CtrllineLoopPortn_Type()
)
pmc2002CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopPortn.setStatus("current")
_Pmc2002CtrlmsAisTable_Object = MibTable
pmc2002CtrlmsAisTable = _Pmc2002CtrlmsAisTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 67)
)
if mibBuilder.loadTexts:
    pmc2002CtrlmsAisTable.setStatus("current")
_Pmc2002CtrlmsAisEntry_Object = MibTableRow
pmc2002CtrlmsAisEntry = _Pmc2002CtrlmsAisEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 67, 1)
)
pmc2002CtrlmsAisEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlmsAisIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlmsAisEntry.setStatus("current")


class _Pmc2002CtrlmsAisIndex_Type(Integer32):
    """Custom type pmc2002CtrlmsAisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlmsAisIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlmsAisIndex_Object = MibTableColumn
pmc2002CtrlmsAisIndex = _Pmc2002CtrlmsAisIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 67, 1, 1),
    _Pmc2002CtrlmsAisIndex_Type()
)
pmc2002CtrlmsAisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlmsAisIndex.setStatus("current")
_Pmc2002CtrlmsAisPortn_Type = EkiState
_Pmc2002CtrlmsAisPortn_Object = MibTableColumn
pmc2002CtrlmsAisPortn = _Pmc2002CtrlmsAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 67, 1, 2),
    _Pmc2002CtrlmsAisPortn_Type()
)
pmc2002CtrlmsAisPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlmsAisPortn.setStatus("current")
_Pmc2002CtrlfecDisableTable_Object = MibTable
pmc2002CtrlfecDisableTable = _Pmc2002CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pmc2002CtrlfecDisableTable.setStatus("current")
_Pmc2002CtrlfecDisableEntry_Object = MibTableRow
pmc2002CtrlfecDisableEntry = _Pmc2002CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 69, 1)
)
pmc2002CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlfecDisableEntry.setStatus("current")


class _Pmc2002CtrlfecDisableIndex_Type(Integer32):
    """Custom type pmc2002CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlfecDisableIndex_Object = MibTableColumn
pmc2002CtrlfecDisableIndex = _Pmc2002CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 69, 1, 1),
    _Pmc2002CtrlfecDisableIndex_Type()
)
pmc2002CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlfecDisableIndex.setStatus("current")
_Pmc2002CtrlfecDisablePortn_Type = EkiState
_Pmc2002CtrlfecDisablePortn_Object = MibTableColumn
pmc2002CtrlfecDisablePortn = _Pmc2002CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 69, 1, 2),
    _Pmc2002CtrlfecDisablePortn_Type()
)
pmc2002CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlfecDisablePortn.setStatus("current")
_Pmc2002CtrllineOosModeTable_Object = MibTable
pmc2002CtrllineOosModeTable = _Pmc2002CtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pmc2002CtrllineOosModeTable.setStatus("current")
_Pmc2002CtrllineOosModeEntry_Object = MibTableRow
pmc2002CtrllineOosModeEntry = _Pmc2002CtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 74, 1)
)
pmc2002CtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllineOosModeEntry.setStatus("current")


class _Pmc2002CtrllineOosModeIndex_Type(Integer32):
    """Custom type pmc2002CtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllineOosModeIndex_Object = MibTableColumn
pmc2002CtrllineOosModeIndex = _Pmc2002CtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 74, 1, 1),
    _Pmc2002CtrllineOosModeIndex_Type()
)
pmc2002CtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllineOosModeIndex.setStatus("current")
_Pmc2002CtrllineOosModePortn_Type = EkiState
_Pmc2002CtrllineOosModePortn_Object = MibTableColumn
pmc2002CtrllineOosModePortn = _Pmc2002CtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 74, 1, 2),
    _Pmc2002CtrllineOosModePortn_Type()
)
pmc2002CtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllineOosModePortn.setStatus("current")
_Pmc2002CtrlxfpOnoffTable_Object = MibTable
pmc2002CtrlxfpOnoffTable = _Pmc2002CtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pmc2002CtrlxfpOnoffTable.setStatus("current")
_Pmc2002CtrlxfpOnoffEntry_Object = MibTableRow
pmc2002CtrlxfpOnoffEntry = _Pmc2002CtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 208, 1)
)
pmc2002CtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlxfpOnoffEntry.setStatus("current")


class _Pmc2002CtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pmc2002CtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlxfpOnoffIndex_Object = MibTableColumn
pmc2002CtrlxfpOnoffIndex = _Pmc2002CtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 208, 1, 1),
    _Pmc2002CtrlxfpOnoffIndex_Type()
)
pmc2002CtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlxfpOnoffIndex.setStatus("current")
_Pmc2002CtrlxfpOnoffPortn_Type = EkiState
_Pmc2002CtrlxfpOnoffPortn_Object = MibTableColumn
pmc2002CtrlxfpOnoffPortn = _Pmc2002CtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 208, 1, 2),
    _Pmc2002CtrlxfpOnoffPortn_Type()
)
pmc2002CtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlxfpOnoffPortn.setStatus("current")
_Pmc2002CtrlxfpLineLoopTable_Object = MibTable
pmc2002CtrlxfpLineLoopTable = _Pmc2002CtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineLoopTable.setStatus("current")
_Pmc2002CtrlxfpLineLoopEntry_Object = MibTableRow
pmc2002CtrlxfpLineLoopEntry = _Pmc2002CtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 209, 1)
)
pmc2002CtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineLoopEntry.setStatus("current")


class _Pmc2002CtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pmc2002CtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlxfpLineLoopIndex_Object = MibTableColumn
pmc2002CtrlxfpLineLoopIndex = _Pmc2002CtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 209, 1, 1),
    _Pmc2002CtrlxfpLineLoopIndex_Type()
)
pmc2002CtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineLoopIndex.setStatus("current")
_Pmc2002CtrlxfpLineLoopPortn_Type = EkiState
_Pmc2002CtrlxfpLineLoopPortn_Object = MibTableColumn
pmc2002CtrlxfpLineLoopPortn = _Pmc2002CtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 209, 1, 2),
    _Pmc2002CtrlxfpLineLoopPortn_Type()
)
pmc2002CtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineLoopPortn.setStatus("current")
_Pmc2002CtrlxfpLineXfiLoopTable_Object = MibTable
pmc2002CtrlxfpLineXfiLoopTable = _Pmc2002CtrlxfpLineXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineXfiLoopTable.setStatus("current")
_Pmc2002CtrlxfpLineXfiLoopEntry_Object = MibTableRow
pmc2002CtrlxfpLineXfiLoopEntry = _Pmc2002CtrlxfpLineXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 210, 1)
)
pmc2002CtrlxfpLineXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlxfpLineXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineXfiLoopEntry.setStatus("current")


class _Pmc2002CtrlxfpLineXfiLoopIndex_Type(Integer32):
    """Custom type pmc2002CtrlxfpLineXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlxfpLineXfiLoopIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlxfpLineXfiLoopIndex_Object = MibTableColumn
pmc2002CtrlxfpLineXfiLoopIndex = _Pmc2002CtrlxfpLineXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 210, 1, 1),
    _Pmc2002CtrlxfpLineXfiLoopIndex_Type()
)
pmc2002CtrlxfpLineXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineXfiLoopIndex.setStatus("current")
_Pmc2002CtrlxfpLineXfiLoopPortn_Type = EkiState
_Pmc2002CtrlxfpLineXfiLoopPortn_Object = MibTableColumn
pmc2002CtrlxfpLineXfiLoopPortn = _Pmc2002CtrlxfpLineXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 210, 1, 2),
    _Pmc2002CtrlxfpLineXfiLoopPortn_Type()
)
pmc2002CtrlxfpLineXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlxfpLineXfiLoopPortn.setStatus("current")
_Pmc2002CtrllineTunableChannelTable_Object = MibTable
pmc2002CtrllineTunableChannelTable = _Pmc2002CtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pmc2002CtrllineTunableChannelTable.setStatus("current")
_Pmc2002CtrllineTunableChannelEntry_Object = MibTableRow
pmc2002CtrllineTunableChannelEntry = _Pmc2002CtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 212, 1)
)
pmc2002CtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllineTunableChannelEntry.setStatus("current")


class _Pmc2002CtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pmc2002CtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllineTunableChannelIndex_Object = MibTableColumn
pmc2002CtrllineTunableChannelIndex = _Pmc2002CtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 212, 1, 1),
    _Pmc2002CtrllineTunableChannelIndex_Type()
)
pmc2002CtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllineTunableChannelIndex.setStatus("current")
_Pmc2002CtrllineTunableChannelPortn_Type = Pmc2002OtxChannel
_Pmc2002CtrllineTunableChannelPortn_Object = MibTableColumn
pmc2002CtrllineTunableChannelPortn = _Pmc2002CtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 212, 1, 2),
    _Pmc2002CtrllineTunableChannelPortn_Type()
)
pmc2002CtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllineTunableChannelPortn.setStatus("current")
_Pmc2002CtrllinePhotodiodeModeTable_Object = MibTable
pmc2002CtrllinePhotodiodeModeTable = _Pmc2002CtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeModeTable.setStatus("current")
_Pmc2002CtrllinePhotodiodeModeEntry_Object = MibTableRow
pmc2002CtrllinePhotodiodeModeEntry = _Pmc2002CtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 213, 1)
)
pmc2002CtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeModeEntry.setStatus("current")


class _Pmc2002CtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pmc2002CtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllinePhotodiodeModeIndex_Object = MibTableColumn
pmc2002CtrllinePhotodiodeModeIndex = _Pmc2002CtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 213, 1, 1),
    _Pmc2002CtrllinePhotodiodeModeIndex_Type()
)
pmc2002CtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeModeIndex.setStatus("current")
_Pmc2002CtrllinePhotodiodeModePortn_Type = Pmc2002OtxMode
_Pmc2002CtrllinePhotodiodeModePortn_Object = MibTableColumn
pmc2002CtrllinePhotodiodeModePortn = _Pmc2002CtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 213, 1, 2),
    _Pmc2002CtrllinePhotodiodeModePortn_Type()
)
pmc2002CtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeModePortn.setStatus("current")
_Pmc2002CtrllinePhotodiodeValueTable_Object = MibTable
pmc2002CtrllinePhotodiodeValueTable = _Pmc2002CtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeValueTable.setStatus("current")
_Pmc2002CtrllinePhotodiodeValueEntry_Object = MibTableRow
pmc2002CtrllinePhotodiodeValueEntry = _Pmc2002CtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 214, 1)
)
pmc2002CtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeValueEntry.setStatus("current")


class _Pmc2002CtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pmc2002CtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllinePhotodiodeValueIndex_Object = MibTableColumn
pmc2002CtrllinePhotodiodeValueIndex = _Pmc2002CtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 214, 1, 1),
    _Pmc2002CtrllinePhotodiodeValueIndex_Type()
)
pmc2002CtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeValueIndex.setStatus("current")
_Pmc2002CtrllinePhotodiodeValuePortn_Type = Pmc2002AdjustValue
_Pmc2002CtrllinePhotodiodeValuePortn_Object = MibTableColumn
pmc2002CtrllinePhotodiodeValuePortn = _Pmc2002CtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 214, 1, 2),
    _Pmc2002CtrllinePhotodiodeValuePortn_Type()
)
pmc2002CtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllinePhotodiodeValuePortn.setStatus("current")
_Pmc2002CtrllinePowerLaserTable_Object = MibTable
pmc2002CtrllinePowerLaserTable = _Pmc2002CtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pmc2002CtrllinePowerLaserTable.setStatus("current")
_Pmc2002CtrllinePowerLaserEntry_Object = MibTableRow
pmc2002CtrllinePowerLaserEntry = _Pmc2002CtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 215, 1)
)
pmc2002CtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllinePowerLaserEntry.setStatus("current")


class _Pmc2002CtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pmc2002CtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllinePowerLaserIndex_Object = MibTableColumn
pmc2002CtrllinePowerLaserIndex = _Pmc2002CtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 215, 1, 1),
    _Pmc2002CtrllinePowerLaserIndex_Type()
)
pmc2002CtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllinePowerLaserIndex.setStatus("current")


class _Pmc2002CtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pmc2002CtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pmc2002CtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pmc2002CtrllinePowerLaserPortn_Object = MibTableColumn
pmc2002CtrllinePowerLaserPortn = _Pmc2002CtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 215, 1, 2),
    _Pmc2002CtrllinePowerLaserPortn_Type()
)
pmc2002CtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllinePowerLaserPortn.setStatus("current")
_Pmc2002CtrlotxVlhResetTable_Object = MibTable
pmc2002CtrlotxVlhResetTable = _Pmc2002CtrlotxVlhResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 216)
)
if mibBuilder.loadTexts:
    pmc2002CtrlotxVlhResetTable.setStatus("current")
_Pmc2002CtrlotxVlhResetEntry_Object = MibTableRow
pmc2002CtrlotxVlhResetEntry = _Pmc2002CtrlotxVlhResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 216, 1)
)
pmc2002CtrlotxVlhResetEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrlotxVlhResetIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrlotxVlhResetEntry.setStatus("current")


class _Pmc2002CtrlotxVlhResetIndex_Type(Integer32):
    """Custom type pmc2002CtrlotxVlhResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrlotxVlhResetIndex_Type.__name__ = "Integer32"
_Pmc2002CtrlotxVlhResetIndex_Object = MibTableColumn
pmc2002CtrlotxVlhResetIndex = _Pmc2002CtrlotxVlhResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 216, 1, 1),
    _Pmc2002CtrlotxVlhResetIndex_Type()
)
pmc2002CtrlotxVlhResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrlotxVlhResetIndex.setStatus("current")
_Pmc2002CtrlotxVlhResetPortn_Type = EkiState
_Pmc2002CtrlotxVlhResetPortn_Object = MibTableColumn
pmc2002CtrlotxVlhResetPortn = _Pmc2002CtrlotxVlhResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 216, 1, 2),
    _Pmc2002CtrlotxVlhResetPortn_Type()
)
pmc2002CtrlotxVlhResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrlotxVlhResetPortn.setStatus("current")
_Pmc2002CtrllineLoopTransceiverTable_Object = MibTable
pmc2002CtrllineLoopTransceiverTable = _Pmc2002CtrllineLoopTransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 218)
)
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopTransceiverTable.setStatus("current")
_Pmc2002CtrllineLoopTransceiverEntry_Object = MibTableRow
pmc2002CtrllineLoopTransceiverEntry = _Pmc2002CtrllineLoopTransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 218, 1)
)
pmc2002CtrllineLoopTransceiverEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllineLoopTransceiverIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopTransceiverEntry.setStatus("current")


class _Pmc2002CtrllineLoopTransceiverIndex_Type(Integer32):
    """Custom type pmc2002CtrllineLoopTransceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllineLoopTransceiverIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllineLoopTransceiverIndex_Object = MibTableColumn
pmc2002CtrllineLoopTransceiverIndex = _Pmc2002CtrllineLoopTransceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 218, 1, 1),
    _Pmc2002CtrllineLoopTransceiverIndex_Type()
)
pmc2002CtrllineLoopTransceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopTransceiverIndex.setStatus("current")
_Pmc2002CtrllineLoopTransceiverPortn_Type = EkiState
_Pmc2002CtrllineLoopTransceiverPortn_Object = MibTableColumn
pmc2002CtrllineLoopTransceiverPortn = _Pmc2002CtrllineLoopTransceiverPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 218, 1, 2),
    _Pmc2002CtrllineLoopTransceiverPortn_Type()
)
pmc2002CtrllineLoopTransceiverPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllineLoopTransceiverPortn.setStatus("current")
_Pmc2002CtrllineResetAllCountTable_Object = MibTable
pmc2002CtrllineResetAllCountTable = _Pmc2002CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 335)
)
if mibBuilder.loadTexts:
    pmc2002CtrllineResetAllCountTable.setStatus("current")
_Pmc2002CtrllineResetAllCountEntry_Object = MibTableRow
pmc2002CtrllineResetAllCountEntry = _Pmc2002CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 335, 1)
)
pmc2002CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CtrllineResetAllCountEntry.setStatus("current")


class _Pmc2002CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pmc2002CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pmc2002CtrllineResetAllCountIndex_Object = MibTableColumn
pmc2002CtrllineResetAllCountIndex = _Pmc2002CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 335, 1, 1),
    _Pmc2002CtrllineResetAllCountIndex_Type()
)
pmc2002CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CtrllineResetAllCountIndex.setStatus("current")
_Pmc2002CtrllineResetAllCountsPortn_Type = EkiState
_Pmc2002CtrllineResetAllCountsPortn_Object = MibTableColumn
pmc2002CtrllineResetAllCountsPortn = _Pmc2002CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 6, 3, 335, 1, 2),
    _Pmc2002CtrllineResetAllCountsPortn_Type()
)
pmc2002CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CtrllineResetAllCountsPortn.setStatus("current")
_Pmc2002ri_ObjectIdentity = ObjectIdentity
pmc2002ri = _Pmc2002ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7)
)
_Pmc2002riTable_ObjectIdentity = ObjectIdentity
pmc2002riTable = _Pmc2002riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1)
)
_Pmc2002RinvClientTable_Object = MibTable
pmc2002RinvClientTable = _Pmc2002RinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmc2002RinvClientTable.setStatus("current")
_Pmc2002RinvClientEntry_Object = MibTableRow
pmc2002RinvClientEntry = _Pmc2002RinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 1, 1)
)
pmc2002RinvClientEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002RinvClientIndex"),
)
if mibBuilder.loadTexts:
    pmc2002RinvClientEntry.setStatus("current")


class _Pmc2002RinvClientIndex_Type(Integer32):
    """Custom type pmc2002RinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmc2002RinvClientIndex_Type.__name__ = "Integer32"
_Pmc2002RinvClientIndex_Object = MibTableColumn
pmc2002RinvClientIndex = _Pmc2002RinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 1, 1, 1),
    _Pmc2002RinvClientIndex_Type()
)
pmc2002RinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvClientIndex.setStatus("current")
_Pmc2002RinvClient_Type = DisplayString
_Pmc2002RinvClient_Object = MibTableColumn
pmc2002RinvClient = _Pmc2002RinvClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 1, 1, 2),
    _Pmc2002RinvClient_Type()
)
pmc2002RinvClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvClient.setStatus("current")
_Pmc2002RinvLineTable_Object = MibTable
pmc2002RinvLineTable = _Pmc2002RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmc2002RinvLineTable.setStatus("current")
_Pmc2002RinvLineEntry_Object = MibTableRow
pmc2002RinvLineEntry = _Pmc2002RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 2, 1)
)
pmc2002RinvLineEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmc2002RinvLineEntry.setStatus("current")


class _Pmc2002RinvLineIndex_Type(Integer32):
    """Custom type pmc2002RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmc2002RinvLineIndex_Type.__name__ = "Integer32"
_Pmc2002RinvLineIndex_Object = MibTableColumn
pmc2002RinvLineIndex = _Pmc2002RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 2, 1, 1),
    _Pmc2002RinvLineIndex_Type()
)
pmc2002RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvLineIndex.setStatus("current")
_Pmc2002RinvxfpLine_Type = DisplayString
_Pmc2002RinvxfpLine_Object = MibTableColumn
pmc2002RinvxfpLine = _Pmc2002RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 1, 2, 1, 2),
    _Pmc2002RinvxfpLine_Type()
)
pmc2002RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvxfpLine.setStatus("current")
_Pmc2002RinvReloadInventory_Type = EkiOnOff
_Pmc2002RinvReloadInventory_Object = MibScalar
pmc2002RinvReloadInventory = _Pmc2002RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 2),
    _Pmc2002RinvReloadInventory_Type()
)
pmc2002RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002RinvReloadInventory.setStatus("current")
_Pmc2002RinvHwPlatform_Type = DisplayString
_Pmc2002RinvHwPlatform_Object = MibScalar
pmc2002RinvHwPlatform = _Pmc2002RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 3),
    _Pmc2002RinvHwPlatform_Type()
)
pmc2002RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvHwPlatform.setStatus("current")
_Pmc2002RinvModulePlatform_Type = DisplayString
_Pmc2002RinvModulePlatform_Object = MibScalar
pmc2002RinvModulePlatform = _Pmc2002RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 4),
    _Pmc2002RinvModulePlatform_Type()
)
pmc2002RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvModulePlatform.setStatus("current")
_Pmc2002RinvSwPlatform_Type = DisplayString
_Pmc2002RinvSwPlatform_Object = MibScalar
pmc2002RinvSwPlatform = _Pmc2002RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 5),
    _Pmc2002RinvSwPlatform_Type()
)
pmc2002RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvSwPlatform.setStatus("current")
_Pmc2002RinvGwPlatform_Type = DisplayString
_Pmc2002RinvGwPlatform_Object = MibScalar
pmc2002RinvGwPlatform = _Pmc2002RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 7, 6),
    _Pmc2002RinvGwPlatform_Type()
)
pmc2002RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002RinvGwPlatform.setStatus("current")
_Pmc2002download_ObjectIdentity = ObjectIdentity
pmc2002download = _Pmc2002download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8)
)
_Pmc2002DwlOther_ObjectIdentity = ObjectIdentity
pmc2002DwlOther = _Pmc2002DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1)
)
_Pmc2002DwlrestartProcess_ObjectIdentity = ObjectIdentity
pmc2002DwlrestartProcess = _Pmc2002DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 0)
)
_Pmc2002DwlWarmRestartProcessed_Type = EkiOnOff
_Pmc2002DwlWarmRestartProcessed_Object = MibScalar
pmc2002DwlWarmRestartProcessed = _Pmc2002DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 0, 1),
    _Pmc2002DwlWarmRestartProcessed_Type()
)
pmc2002DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlWarmRestartProcessed.setStatus("current")
_Pmc2002DwlColdRestartProcessed_Type = EkiOnOff
_Pmc2002DwlColdRestartProcessed_Object = MibScalar
pmc2002DwlColdRestartProcessed = _Pmc2002DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 0, 2),
    _Pmc2002DwlColdRestartProcessed_Type()
)
pmc2002DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlColdRestartProcessed.setStatus("current")
_Pmc2002DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmc2002DwlswBanksUsed = _Pmc2002DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 1)
)
_Pmc2002DwlSwBank1Used_Type = EkiOnOff
_Pmc2002DwlSwBank1Used_Object = MibScalar
pmc2002DwlSwBank1Used = _Pmc2002DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 1, 1),
    _Pmc2002DwlSwBank1Used_Type()
)
pmc2002DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlSwBank1Used.setStatus("current")
_Pmc2002DwlSwBank2Used_Type = EkiOnOff
_Pmc2002DwlSwBank2Used_Object = MibScalar
pmc2002DwlSwBank2Used = _Pmc2002DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 1, 2),
    _Pmc2002DwlSwBank2Used_Type()
)
pmc2002DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlSwBank2Used.setStatus("current")
_Pmc2002DwlSwBank1Notempty_Type = EkiOnOff
_Pmc2002DwlSwBank1Notempty_Object = MibScalar
pmc2002DwlSwBank1Notempty = _Pmc2002DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 1, 5),
    _Pmc2002DwlSwBank1Notempty_Type()
)
pmc2002DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlSwBank1Notempty.setStatus("current")
_Pmc2002DwlSwBank2Notempty_Type = EkiOnOff
_Pmc2002DwlSwBank2Notempty_Object = MibScalar
pmc2002DwlSwBank2Notempty = _Pmc2002DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 1, 6),
    _Pmc2002DwlSwBank2Notempty_Type()
)
pmc2002DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlSwBank2Notempty.setStatus("current")
_Pmc2002DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmc2002DwlgwBanksUsed = _Pmc2002DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2)
)
_Pmc2002DwlGwBank1Used_Type = EkiOnOff
_Pmc2002DwlGwBank1Used_Object = MibScalar
pmc2002DwlGwBank1Used = _Pmc2002DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 1),
    _Pmc2002DwlGwBank1Used_Type()
)
pmc2002DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank1Used.setStatus("current")
_Pmc2002DwlGwBank2Used_Type = EkiOnOff
_Pmc2002DwlGwBank2Used_Object = MibScalar
pmc2002DwlGwBank2Used = _Pmc2002DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 2),
    _Pmc2002DwlGwBank2Used_Type()
)
pmc2002DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank2Used.setStatus("deprecated")
_Pmc2002DwlGwBank3Used_Type = EkiOnOff
_Pmc2002DwlGwBank3Used_Object = MibScalar
pmc2002DwlGwBank3Used = _Pmc2002DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 3),
    _Pmc2002DwlGwBank3Used_Type()
)
pmc2002DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank3Used.setStatus("current")
_Pmc2002DwlGwBank4Used_Type = EkiOnOff
_Pmc2002DwlGwBank4Used_Object = MibScalar
pmc2002DwlGwBank4Used = _Pmc2002DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 4),
    _Pmc2002DwlGwBank4Used_Type()
)
pmc2002DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank4Used.setStatus("deprecated")
_Pmc2002DwlGwBank1Notempty_Type = EkiOnOff
_Pmc2002DwlGwBank1Notempty_Object = MibScalar
pmc2002DwlGwBank1Notempty = _Pmc2002DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 5),
    _Pmc2002DwlGwBank1Notempty_Type()
)
pmc2002DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank1Notempty.setStatus("current")
_Pmc2002DwlGwBank2Notempty_Type = EkiOnOff
_Pmc2002DwlGwBank2Notempty_Object = MibScalar
pmc2002DwlGwBank2Notempty = _Pmc2002DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 6),
    _Pmc2002DwlGwBank2Notempty_Type()
)
pmc2002DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank2Notempty.setStatus("deprecated")
_Pmc2002DwlGwBank3Notempty_Type = EkiOnOff
_Pmc2002DwlGwBank3Notempty_Object = MibScalar
pmc2002DwlGwBank3Notempty = _Pmc2002DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 7),
    _Pmc2002DwlGwBank3Notempty_Type()
)
pmc2002DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank3Notempty.setStatus("current")
_Pmc2002DwlGwBank4Notempty_Type = EkiOnOff
_Pmc2002DwlGwBank4Notempty_Object = MibScalar
pmc2002DwlGwBank4Notempty = _Pmc2002DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 1, 2, 8),
    _Pmc2002DwlGwBank4Notempty_Type()
)
pmc2002DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002DwlGwBank4Notempty.setStatus("deprecated")
_Pmc2002DwlClient_ObjectIdentity = ObjectIdentity
pmc2002DwlClient = _Pmc2002DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 2)
)
_Pmc2002DwlLine_ObjectIdentity = ObjectIdentity
pmc2002DwlLine = _Pmc2002DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 8, 3)
)
_Pmc2002Config_ObjectIdentity = ObjectIdentity
pmc2002Config = _Pmc2002Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10)
)
_Pmc2002CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pmc2002CfgAccessCAisCsf = _Pmc2002CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1)
)
_Pmc2002CfgClientcaiscsfTable_Object = MibTable
pmc2002CfgClientcaiscsfTable = _Pmc2002CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1)
)
if mibBuilder.loadTexts:
    pmc2002CfgClientcaiscsfTable.setStatus("current")
_Pmc2002CfgClientcaiscsfEntry_Object = MibTableRow
pmc2002CfgClientcaiscsfEntry = _Pmc2002CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1)
)
pmc2002CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgClientcaiscsfEntry.setStatus("current")


class _Pmc2002CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pmc2002CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pmc2002CfgClientcaiscsfIndex_Object = MibTableColumn
pmc2002CfgClientcaiscsfIndex = _Pmc2002CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 1),
    _Pmc2002CfgClientcaiscsfIndex_Type()
)
pmc2002CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgClientcaiscsfIndex.setStatus("current")


class _Pmc2002CfgCAisModePortn_Type(Unsigned32):
    """Custom type pmc2002CfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgCAisModePortn_Object = MibTableColumn
pmc2002CfgCAisModePortn = _Pmc2002CfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 3),
    _Pmc2002CfgCAisModePortn_Type()
)
pmc2002CfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgCAisModePortn.setStatus("current")


class _Pmc2002CfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pmc2002CfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgUpAccessioAlmPortn_Object = MibTableColumn
pmc2002CfgUpAccessioAlmPortn = _Pmc2002CfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 9),
    _Pmc2002CfgUpAccessioAlmPortn_Type()
)
pmc2002CfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgUpAccessioAlmPortn.setStatus("current")


class _Pmc2002CfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pmc2002CfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgUpMapperDeAlmPortn_Object = MibTableColumn
pmc2002CfgUpMapperDeAlmPortn = _Pmc2002CfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 10),
    _Pmc2002CfgUpMapperDeAlmPortn_Type()
)
pmc2002CfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgUpMapperDeAlmPortn.setStatus("current")


class _Pmc2002CfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pmc2002CfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgDownAccessioAlmPortn_Object = MibTableColumn
pmc2002CfgDownAccessioAlmPortn = _Pmc2002CfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 17),
    _Pmc2002CfgDownAccessioAlmPortn_Type()
)
pmc2002CfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgDownAccessioAlmPortn.setStatus("current")


class _Pmc2002CfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pmc2002CfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgDownMapperDeAlmPortn_Object = MibTableColumn
pmc2002CfgDownMapperDeAlmPortn = _Pmc2002CfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 18),
    _Pmc2002CfgDownMapperDeAlmPortn_Type()
)
pmc2002CfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgDownMapperDeAlmPortn.setStatus("current")


class _Pmc2002CfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pmc2002CfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgDownDfrmAlmPortn_Object = MibTableColumn
pmc2002CfgDownDfrmAlmPortn = _Pmc2002CfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 19),
    _Pmc2002CfgDownDfrmAlmPortn_Type()
)
pmc2002CfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgDownDfrmAlmPortn.setStatus("current")


class _Pmc2002CfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pmc2002CfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pmc2002CfgDownLineSyncAlarmsPortn = _Pmc2002CfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 1, 1, 1, 20),
    _Pmc2002CfgDownLineSyncAlarmsPortn_Type()
)
pmc2002CfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pmc2002CfgStartup_ObjectIdentity = ObjectIdentity
pmc2002CfgStartup = _Pmc2002CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2)
)
_Pmc2002CfgClientStartupTable_Object = MibTable
pmc2002CfgClientStartupTable = _Pmc2002CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 1)
)
if mibBuilder.loadTexts:
    pmc2002CfgClientStartupTable.setStatus("current")
_Pmc2002CfgClientStartupEntry_Object = MibTableRow
pmc2002CfgClientStartupEntry = _Pmc2002CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 1, 1)
)
pmc2002CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgClientStartupEntry.setStatus("current")


class _Pmc2002CfgClientStartupIndex_Type(Integer32):
    """Custom type pmc2002CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pmc2002CfgClientStartupIndex_Object = MibTableColumn
pmc2002CfgClientStartupIndex = _Pmc2002CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 1, 1, 1),
    _Pmc2002CfgClientStartupIndex_Type()
)
pmc2002CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgClientStartupIndex.setStatus("current")


class _Pmc2002CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pmc2002CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgSystConfPortPortn_Object = MibTableColumn
pmc2002CfgSystConfPortPortn = _Pmc2002CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 1, 1, 3),
    _Pmc2002CfgSystConfPortPortn_Type()
)
pmc2002CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgSystConfPortPortn.setStatus("current")


class _Pmc2002CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pmc2002CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgNetConfPortPortn_Object = MibTableColumn
pmc2002CfgNetConfPortPortn = _Pmc2002CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 1, 1, 4),
    _Pmc2002CfgNetConfPortPortn_Type()
)
pmc2002CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgNetConfPortPortn.setStatus("current")


class _Pmc2002CfgPortsOptionsPortn_Type(Unsigned32):
    """Custom type pmc2002CfgPortsOptionsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgPortsOptionsPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgPortsOptionsPortn_Object = MibTableColumn
pmc2002CfgPortsOptionsPortn = _Pmc2002CfgPortsOptionsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 1, 1, 6),
    _Pmc2002CfgPortsOptionsPortn_Type()
)
pmc2002CfgPortsOptionsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgPortsOptionsPortn.setStatus("current")
_Pmc2002tablelineStartup_ObjectIdentity = ObjectIdentity
pmc2002tablelineStartup = _Pmc2002tablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 2)
)


class _Pmc2002CfgsynthTransLine1_Type(Unsigned32):
    """Custom type pmc2002CfgsynthTransLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgsynthTransLine1_Type.__name__ = "Unsigned32"
_Pmc2002CfgsynthTransLine1_Object = MibScalar
pmc2002CfgsynthTransLine1 = _Pmc2002CfgsynthTransLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 2, 2),
    _Pmc2002CfgsynthTransLine1_Type()
)
pmc2002CfgsynthTransLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgsynthTransLine1.setStatus("current")


class _Pmc2002CfgnetConfMod_Type(Unsigned32):
    """Custom type pmc2002CfgnetConfMod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgnetConfMod_Type.__name__ = "Unsigned32"
_Pmc2002CfgnetConfMod_Object = MibScalar
pmc2002CfgnetConfMod = _Pmc2002CfgnetConfMod_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 2, 3),
    _Pmc2002CfgnetConfMod_Type()
)
pmc2002CfgnetConfMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgnetConfMod.setStatus("current")


class _Pmc2002CfglineOptions1_Type(Unsigned32):
    """Custom type pmc2002CfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfglineOptions1_Type.__name__ = "Unsigned32"
_Pmc2002CfglineOptions1_Object = MibScalar
pmc2002CfglineOptions1 = _Pmc2002CfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 2, 5),
    _Pmc2002CfglineOptions1_Type()
)
pmc2002CfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfglineOptions1.setStatus("current")


class _Pmc2002CfgsystTransLine2_Type(Unsigned32):
    """Custom type pmc2002CfgsystTransLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgsystTransLine2_Type.__name__ = "Unsigned32"
_Pmc2002CfgsystTransLine2_Object = MibScalar
pmc2002CfgsystTransLine2 = _Pmc2002CfgsystTransLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 2, 6),
    _Pmc2002CfgsystTransLine2_Type()
)
pmc2002CfgsystTransLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgsystTransLine2.setStatus("current")


class _Pmc2002CfglineSelection_Type(Unsigned32):
    """Custom type pmc2002CfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfglineSelection_Type.__name__ = "Unsigned32"
_Pmc2002CfglineSelection_Object = MibScalar
pmc2002CfglineSelection = _Pmc2002CfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 2, 7),
    _Pmc2002CfglineSelection_Type()
)
pmc2002CfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfglineSelection.setStatus("current")
_Pmc2002CfgXfpTable_Object = MibTable
pmc2002CfgXfpTable = _Pmc2002CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 3)
)
if mibBuilder.loadTexts:
    pmc2002CfgXfpTable.setStatus("current")
_Pmc2002CfgXfpEntry_Object = MibTableRow
pmc2002CfgXfpEntry = _Pmc2002CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 3, 1)
)
pmc2002CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgXfpEntry.setStatus("current")


class _Pmc2002CfgXfpIndex_Type(Integer32):
    """Custom type pmc2002CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgXfpIndex_Type.__name__ = "Integer32"
_Pmc2002CfgXfpIndex_Object = MibTableColumn
pmc2002CfgXfpIndex = _Pmc2002CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 3, 1, 1),
    _Pmc2002CfgXfpIndex_Type()
)
pmc2002CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgXfpIndex.setStatus("current")


class _Pmc2002CfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pmc2002CfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgSystConfXfpPortn_Object = MibTableColumn
pmc2002CfgSystConfXfpPortn = _Pmc2002CfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 3, 1, 3),
    _Pmc2002CfgSystConfXfpPortn_Type()
)
pmc2002CfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgSystConfXfpPortn.setStatus("current")


class _Pmc2002CfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pmc2002CfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgDataRateConfXfpPortn_Object = MibTableColumn
pmc2002CfgDataRateConfXfpPortn = _Pmc2002CfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 3, 1, 4),
    _Pmc2002CfgDataRateConfXfpPortn_Type()
)
pmc2002CfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgDataRateConfXfpPortn.setStatus("deprecated")
_Pmc2002CfgOtxtlhTable_Object = MibTable
pmc2002CfgOtxtlhTable = _Pmc2002CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4)
)
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhTable.setStatus("current")
_Pmc2002CfgOtxtlhEntry_Object = MibTableRow
pmc2002CfgOtxtlhEntry = _Pmc2002CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1)
)
pmc2002CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhEntry.setStatus("current")


class _Pmc2002CfgOtxtlhIndex_Type(Integer32):
    """Custom type pmc2002CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pmc2002CfgOtxtlhIndex_Object = MibTableColumn
pmc2002CfgOtxtlhIndex = _Pmc2002CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 1),
    _Pmc2002CfgOtxtlhIndex_Type()
)
pmc2002CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhIndex.setStatus("current")


class _Pmc2002CfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pmc2002CfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLineDitherRatePortn_Object = MibTableColumn
pmc2002CfgLineDitherRatePortn = _Pmc2002CfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 4),
    _Pmc2002CfgLineDitherRatePortn_Type()
)
pmc2002CfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLineDitherRatePortn.setStatus("current")


class _Pmc2002CfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pmc2002CfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLineDitherFhzPortn_Object = MibTableColumn
pmc2002CfgLineDitherFhzPortn = _Pmc2002CfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 5),
    _Pmc2002CfgLineDitherFhzPortn_Type()
)
pmc2002CfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLineDitherFhzPortn.setStatus("current")


class _Pmc2002CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pmc2002CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLinePwrLaserPortn_Object = MibTableColumn
pmc2002CfgLinePwrLaserPortn = _Pmc2002CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 6),
    _Pmc2002CfgLinePwrLaserPortn_Type()
)
pmc2002CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLinePwrLaserPortn.setStatus("current")


class _Pmc2002CfgFPortn_Type(Unsigned32):
    """Custom type pmc2002CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgFPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgFPortn_Object = MibTableColumn
pmc2002CfgFPortn = _Pmc2002CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 9),
    _Pmc2002CfgFPortn_Type()
)
pmc2002CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgFPortn.setStatus("current")


class _Pmc2002CfgReservedPortn_Type(Unsigned32):
    """Custom type pmc2002CfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgReservedPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgReservedPortn_Object = MibTableColumn
pmc2002CfgReservedPortn = _Pmc2002CfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 10),
    _Pmc2002CfgReservedPortn_Type()
)
pmc2002CfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgReservedPortn.setStatus("deprecated")


class _Pmc2002CfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pmc2002CfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLinePhotodiodeModePortn_Object = MibTableColumn
pmc2002CfgLinePhotodiodeModePortn = _Pmc2002CfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 11),
    _Pmc2002CfgLinePhotodiodeModePortn_Type()
)
pmc2002CfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLinePhotodiodeModePortn.setStatus("current")


class _Pmc2002CfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pmc2002CfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLinePhotodiodeValuePortn_Object = MibTableColumn
pmc2002CfgLinePhotodiodeValuePortn = _Pmc2002CfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 4, 1, 12),
    _Pmc2002CfgLinePhotodiodeValuePortn_Type()
)
pmc2002CfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLinePhotodiodeValuePortn.setStatus("current")
_Pmc2002CfgOtxtlhCommonTable_Object = MibTable
pmc2002CfgOtxtlhCommonTable = _Pmc2002CfgOtxtlhCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 5)
)
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhCommonTable.setStatus("current")
_Pmc2002CfgOtxtlhCommonEntry_Object = MibTableRow
pmc2002CfgOtxtlhCommonEntry = _Pmc2002CfgOtxtlhCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 5, 1)
)
pmc2002CfgOtxtlhCommonEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgOtxtlhCommonIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhCommonEntry.setStatus("current")


class _Pmc2002CfgOtxtlhCommonIndex_Type(Integer32):
    """Custom type pmc2002CfgOtxtlhCommonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgOtxtlhCommonIndex_Type.__name__ = "Integer32"
_Pmc2002CfgOtxtlhCommonIndex_Object = MibTableColumn
pmc2002CfgOtxtlhCommonIndex = _Pmc2002CfgOtxtlhCommonIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 5, 1, 1),
    _Pmc2002CfgOtxtlhCommonIndex_Type()
)
pmc2002CfgOtxtlhCommonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhCommonIndex.setStatus("current")


class _Pmc2002CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmc2002CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLineFCurrentPortn_Object = MibTableColumn
pmc2002CfgLineFCurrentPortn = _Pmc2002CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 5, 1, 7),
    _Pmc2002CfgLineFCurrentPortn_Type()
)
pmc2002CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLineFCurrentPortn.setStatus("current")


class _Pmc2002CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pmc2002CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLineGridCurrentPortn_Object = MibTableColumn
pmc2002CfgLineGridCurrentPortn = _Pmc2002CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 2, 5, 1, 8),
    _Pmc2002CfgLineGridCurrentPortn_Type()
)
pmc2002CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLineGridCurrentPortn.setStatus("current")
_Pmc2002CfgLabels_ObjectIdentity = ObjectIdentity
pmc2002CfgLabels = _Pmc2002CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3)
)
_Pmc2002CfgLabelclientTable_Object = MibTable
pmc2002CfgLabelclientTable = _Pmc2002CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 1)
)
if mibBuilder.loadTexts:
    pmc2002CfgLabelclientTable.setStatus("current")
_Pmc2002CfgLabelclientEntry_Object = MibTableRow
pmc2002CfgLabelclientEntry = _Pmc2002CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 1, 1)
)
pmc2002CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgLabelclientEntry.setStatus("current")


class _Pmc2002CfgLabelclientIndex_Type(Integer32):
    """Custom type pmc2002CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmc2002CfgLabelclientIndex_Object = MibTableColumn
pmc2002CfgLabelclientIndex = _Pmc2002CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 1, 1, 1),
    _Pmc2002CfgLabelclientIndex_Type()
)
pmc2002CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgLabelclientIndex.setStatus("current")


class _Pmc2002CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmc2002CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmc2002CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmc2002CfgLabelclientPortn_Object = MibTableColumn
pmc2002CfgLabelclientPortn = _Pmc2002CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 1, 1, 3),
    _Pmc2002CfgLabelclientPortn_Type()
)
pmc2002CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLabelclientPortn.setStatus("current")
_Pmc2002CfgLabellineTable_Object = MibTable
pmc2002CfgLabellineTable = _Pmc2002CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 2)
)
if mibBuilder.loadTexts:
    pmc2002CfgLabellineTable.setStatus("current")
_Pmc2002CfgLabellineEntry_Object = MibTableRow
pmc2002CfgLabellineEntry = _Pmc2002CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 2, 1)
)
pmc2002CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgLabellineEntry.setStatus("current")


class _Pmc2002CfgLabellineIndex_Type(Integer32):
    """Custom type pmc2002CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmc2002CfgLabellineIndex_Object = MibTableColumn
pmc2002CfgLabellineIndex = _Pmc2002CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 2, 1, 1),
    _Pmc2002CfgLabellineIndex_Type()
)
pmc2002CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgLabellineIndex.setStatus("current")


class _Pmc2002CfgLabellinePortn_Type(DisplayString):
    """Custom type pmc2002CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmc2002CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmc2002CfgLabellinePortn_Object = MibTableColumn
pmc2002CfgLabellinePortn = _Pmc2002CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 3, 2, 1, 3),
    _Pmc2002CfgLabellinePortn_Type()
)
pmc2002CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgLabellinePortn.setStatus("current")
_Pmc2002CfgOther_ObjectIdentity = ObjectIdentity
pmc2002CfgOther = _Pmc2002CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 4)
)
_Pmc2002tablemoduleOther_ObjectIdentity = ObjectIdentity
pmc2002tablemoduleOther = _Pmc2002tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 4, 1)
)


class _Pmc2002Cfgmode_Type(Unsigned32):
    """Custom type pmc2002Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002Cfgmode_Type.__name__ = "Unsigned32"
_Pmc2002Cfgmode_Object = MibScalar
pmc2002Cfgmode = _Pmc2002Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 4, 1, 2),
    _Pmc2002Cfgmode_Type()
)
pmc2002Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Cfgmode.setStatus("current")
_Pmc2002CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pmc2002CfgStartuptablefive = _Pmc2002CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5)
)
_Pmc2002CfgOtxtlhcapabilitiesTable_Object = MibTable
pmc2002CfgOtxtlhcapabilitiesTable = _Pmc2002CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1)
)
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pmc2002CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pmc2002CfgOtxtlhcapabilitiesEntry = _Pmc2002CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1)
)
pmc2002CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pmc2002CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pmc2002CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pmc2002CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pmc2002CfgOtxtlhcapabilitiesIndex = _Pmc2002CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1, 1),
    _Pmc2002CfgOtxtlhcapabilitiesIndex_Type()
)
pmc2002CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pmc2002CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pmc2002CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgComponentTypePortn_Object = MibTableColumn
pmc2002CfgComponentTypePortn = _Pmc2002CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1, 3),
    _Pmc2002CfgComponentTypePortn_Type()
)
pmc2002CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgComponentTypePortn.setStatus("current")


class _Pmc2002CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pmc2002CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgMiscellaneousPortn_Object = MibTableColumn
pmc2002CfgMiscellaneousPortn = _Pmc2002CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1, 4),
    _Pmc2002CfgMiscellaneousPortn_Type()
)
pmc2002CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgMiscellaneousPortn.setStatus("current")


class _Pmc2002CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pmc2002CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgFirstChannelPortn_Object = MibTableColumn
pmc2002CfgFirstChannelPortn = _Pmc2002CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1, 5),
    _Pmc2002CfgFirstChannelPortn_Type()
)
pmc2002CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgFirstChannelPortn.setStatus("current")


class _Pmc2002CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pmc2002CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgLastChannelPortn_Object = MibTableColumn
pmc2002CfgLastChannelPortn = _Pmc2002CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1, 6),
    _Pmc2002CfgLastChannelPortn_Type()
)
pmc2002CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgLastChannelPortn.setStatus("current")


class _Pmc2002CfgGridPortn_Type(Unsigned32):
    """Custom type pmc2002CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc2002CfgGridPortn_Type.__name__ = "Unsigned32"
_Pmc2002CfgGridPortn_Object = MibTableColumn
pmc2002CfgGridPortn = _Pmc2002CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 5, 1, 1, 7),
    _Pmc2002CfgGridPortn_Type()
)
pmc2002CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002CfgGridPortn.setStatus("current")
_Pmc2002CfgWriteConfiguration_Type = EkiOnOff
_Pmc2002CfgWriteConfiguration_Object = MibScalar
pmc2002CfgWriteConfiguration = _Pmc2002CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 10, 257),
    _Pmc2002CfgWriteConfiguration_Type()
)
pmc2002CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002CfgWriteConfiguration.setStatus("current")
_Pmc2002traps_ObjectIdentity = ObjectIdentity
pmc2002traps = _Pmc2002traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11)
)


class _Pmc2002trapBoardNumber_Type(Integer32):
    """Custom type pmc2002trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc2002trapBoardNumber_Type.__name__ = "Integer32"
_Pmc2002trapBoardNumber_Object = MibScalar
pmc2002trapBoardNumber = _Pmc2002trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 1),
    _Pmc2002trapBoardNumber_Type()
)
pmc2002trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002trapBoardNumber.setStatus("current")


class _Pmc2002trapClientNumber_Type(Integer32):
    """Custom type pmc2002trapClientNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc2002trapClientNumber_Type.__name__ = "Integer32"
_Pmc2002trapClientNumber_Object = MibScalar
pmc2002trapClientNumber = _Pmc2002trapClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 2),
    _Pmc2002trapClientNumber_Type()
)
pmc2002trapClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002trapClientNumber.setStatus("current")


class _Pmc2002trapLineNumber_Type(Integer32):
    """Custom type pmc2002trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc2002trapLineNumber_Type.__name__ = "Integer32"
_Pmc2002trapLineNumber_Object = MibScalar
pmc2002trapLineNumber = _Pmc2002trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 3),
    _Pmc2002trapLineNumber_Type()
)
pmc2002trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002trapLineNumber.setStatus("current")
_Pmc2002Monitoring_ObjectIdentity = ObjectIdentity
pmc2002Monitoring = _Pmc2002Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12)
)
_Pmc2002MonOther_ObjectIdentity = ObjectIdentity
pmc2002MonOther = _Pmc2002MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1)
)
_Pmc2002MonSync_ObjectIdentity = ObjectIdentity
pmc2002MonSync = _Pmc2002MonSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 1)
)
_Pmc2002PerfEnable_Type = EkiOnOff
_Pmc2002PerfEnable_Object = MibScalar
pmc2002PerfEnable = _Pmc2002PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 1, 257),
    _Pmc2002PerfEnable_Type()
)
pmc2002PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002PerfEnable.setStatus("current")
_Pmc2002Perf15minSync_Type = EkiOnOff
_Pmc2002Perf15minSync_Object = MibScalar
pmc2002Perf15minSync = _Pmc2002Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 1, 259),
    _Pmc2002Perf15minSync_Type()
)
pmc2002Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Perf15minSync.setStatus("current")
_Pmc2002Perf24hSync_Type = EkiOnOff
_Pmc2002Perf24hSync_Object = MibScalar
pmc2002Perf24hSync = _Pmc2002Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 1, 260),
    _Pmc2002Perf24hSync_Type()
)
pmc2002Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Perf24hSync.setStatus("current")
_Pmc2002MonTimeStamp_ObjectIdentity = ObjectIdentity
pmc2002MonTimeStamp = _Pmc2002MonTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2)
)
_Pmc2002Perf15MinShort_Type = EkiOnOff
_Pmc2002Perf15MinShort_Object = MibScalar
pmc2002Perf15MinShort = _Pmc2002Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2, 1),
    _Pmc2002Perf15MinShort_Type()
)
pmc2002Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Perf15MinShort.setStatus("current")
_Pmc2002Perf15MinLong_Type = EkiOnOff
_Pmc2002Perf15MinLong_Object = MibScalar
pmc2002Perf15MinLong = _Pmc2002Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2, 2),
    _Pmc2002Perf15MinLong_Type()
)
pmc2002Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Perf15MinLong.setStatus("current")
_Pmc2002Perf24HoursShort_Type = Counter32
_Pmc2002Perf24HoursShort_Object = MibScalar
pmc2002Perf24HoursShort = _Pmc2002Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2, 5),
    _Pmc2002Perf24HoursShort_Type()
)
pmc2002Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Perf24HoursShort.setStatus("current")
_Pmc2002Perf24HoursLong_Type = Counter32
_Pmc2002Perf24HoursLong_Object = MibScalar
pmc2002Perf24HoursLong = _Pmc2002Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2, 6),
    _Pmc2002Perf24HoursLong_Type()
)
pmc2002Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002Perf24HoursLong.setStatus("current")
_Pmc2002PerfCurrent15MinElapsedTime_Type = Counter32
_Pmc2002PerfCurrent15MinElapsedTime_Object = MibScalar
pmc2002PerfCurrent15MinElapsedTime = _Pmc2002PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2, 7),
    _Pmc2002PerfCurrent15MinElapsedTime_Type()
)
pmc2002PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002PerfCurrent15MinElapsedTime.setStatus("current")
_Pmc2002PerfCurrent24HoursElapsedTime_Type = Counter32
_Pmc2002PerfCurrent24HoursElapsedTime_Object = MibScalar
pmc2002PerfCurrent24HoursElapsedTime = _Pmc2002PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 1, 2, 8),
    _Pmc2002PerfCurrent24HoursElapsedTime_Type()
)
pmc2002PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002PerfCurrent24HoursElapsedTime.setStatus("current")
_Pmc2002MonClient_ObjectIdentity = ObjectIdentity
pmc2002MonClient = _Pmc2002MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2)
)
_Pmc2002PerfTelecomClientCurrent15StatTable_Object = MibTable
pmc2002PerfTelecomClientCurrent15StatTable = _Pmc2002PerfTelecomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatTable.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatEntry_Object = MibTableRow
pmc2002PerfTelecomClientCurrent15StatEntry = _Pmc2002PerfTelecomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1)
)
pmc2002PerfTelecomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatEntry.setStatus("current")


class _Pmc2002PerfTelecomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pmc2002PerfTelecomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomClientCurrent15StatIndex_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatIndex = _Pmc2002PerfTelecomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 1),
    _Pmc2002PerfTelecomClientCurrent15StatIndex_Type()
)
pmc2002PerfTelecomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatIndex.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent15StatInvCvPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatInvCvPortn = _Pmc2002PerfTelecomClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 2),
    _Pmc2002PerfTelecomClientCurrent15StatInvCvPortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatInvCvPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent15StatCvValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatCvValuePortn = _Pmc2002PerfTelecomClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 3),
    _Pmc2002PerfTelecomClientCurrent15StatCvValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatCvValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent15StatInvEsPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatInvEsPortn = _Pmc2002PerfTelecomClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 4),
    _Pmc2002PerfTelecomClientCurrent15StatInvEsPortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatInvEsPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent15StatEsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatEsValuePortn = _Pmc2002PerfTelecomClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 5),
    _Pmc2002PerfTelecomClientCurrent15StatEsValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatEsValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent15StatInvSesPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatInvSesPortn = _Pmc2002PerfTelecomClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 6),
    _Pmc2002PerfTelecomClientCurrent15StatInvSesPortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatInvSesPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent15StatSesValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatSesValuePortn = _Pmc2002PerfTelecomClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 7),
    _Pmc2002PerfTelecomClientCurrent15StatSesValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatSesValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatInvSefsPortn = _Pmc2002PerfTelecomClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 8),
    _Pmc2002PerfTelecomClientCurrent15StatInvSefsPortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatInvSefsPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatSefsValuePortn = _Pmc2002PerfTelecomClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 9),
    _Pmc2002PerfTelecomClientCurrent15StatSefsValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatSefsValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent15StatInvUasPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatInvUasPortn = _Pmc2002PerfTelecomClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 10),
    _Pmc2002PerfTelecomClientCurrent15StatInvUasPortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatInvUasPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent15StatUasValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent15StatUasValuePortn = _Pmc2002PerfTelecomClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 16, 1, 11),
    _Pmc2002PerfTelecomClientCurrent15StatUasValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent15StatUasValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryPort1Table_Object = MibTable
pmc2002PerfTelecomClientPast15StatHistoryPort1Table = _Pmc2002PerfTelecomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryPort1Table.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pmc2002PerfTelecomClientPast15StatHistoryPort1Entry = _Pmc2002PerfTelecomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1)
)
pmc2002PerfTelecomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pmc2002PerfTelecomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc2002PerfTelecomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryPort1Index = _Pmc2002PerfTelecomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 1),
    _Pmc2002PerfTelecomClientPast15StatHistoryPort1Index_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryPort1Index.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1 = _Pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 2),
    _Pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1 = _Pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 3),
    _Pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1 = _Pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 4),
    _Pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1 = _Pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 5),
    _Pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1 = _Pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 6),
    _Pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistorySesValuePort1 = _Pmc2002PerfTelecomClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 7),
    _Pmc2002PerfTelecomClientPast15StatHistorySesValuePort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistorySesValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1 = _Pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 8),
    _Pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1 = _Pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 9),
    _Pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1 = _Pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 10),
    _Pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1 = _Pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 24, 1, 11),
    _Pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1_Type()
)
pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatTable_Object = MibTable
pmc2002PerfTelecomClientCurrent24StatTable = _Pmc2002PerfTelecomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatTable.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatEntry_Object = MibTableRow
pmc2002PerfTelecomClientCurrent24StatEntry = _Pmc2002PerfTelecomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1)
)
pmc2002PerfTelecomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatEntry.setStatus("current")


class _Pmc2002PerfTelecomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pmc2002PerfTelecomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomClientCurrent24StatIndex_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatIndex = _Pmc2002PerfTelecomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 1),
    _Pmc2002PerfTelecomClientCurrent24StatIndex_Type()
)
pmc2002PerfTelecomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatIndex.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent24StatInvCvPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatInvCvPortn = _Pmc2002PerfTelecomClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 2),
    _Pmc2002PerfTelecomClientCurrent24StatInvCvPortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatInvCvPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent24StatCvValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatCvValuePortn = _Pmc2002PerfTelecomClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 3),
    _Pmc2002PerfTelecomClientCurrent24StatCvValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatCvValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent24StatInvEsPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatInvEsPortn = _Pmc2002PerfTelecomClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 4),
    _Pmc2002PerfTelecomClientCurrent24StatInvEsPortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatInvEsPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent24StatEsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatEsValuePortn = _Pmc2002PerfTelecomClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 5),
    _Pmc2002PerfTelecomClientCurrent24StatEsValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatEsValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent24StatInvSesPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatInvSesPortn = _Pmc2002PerfTelecomClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 6),
    _Pmc2002PerfTelecomClientCurrent24StatInvSesPortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatInvSesPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent24StatSesValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatSesValuePortn = _Pmc2002PerfTelecomClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 7),
    _Pmc2002PerfTelecomClientCurrent24StatSesValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatSesValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatInvSefsPortn = _Pmc2002PerfTelecomClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 8),
    _Pmc2002PerfTelecomClientCurrent24StatInvSefsPortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatInvSefsPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatSefsValuePortn = _Pmc2002PerfTelecomClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 9),
    _Pmc2002PerfTelecomClientCurrent24StatSefsValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatSefsValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pmc2002PerfTelecomClientCurrent24StatInvUasPortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatInvUasPortn = _Pmc2002PerfTelecomClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 10),
    _Pmc2002PerfTelecomClientCurrent24StatInvUasPortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatInvUasPortn.setStatus("current")
_Pmc2002PerfTelecomClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomClientCurrent24StatUasValuePortn_Object = MibTableColumn
pmc2002PerfTelecomClientCurrent24StatUasValuePortn = _Pmc2002PerfTelecomClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 32, 1, 11),
    _Pmc2002PerfTelecomClientCurrent24StatUasValuePortn_Type()
)
pmc2002PerfTelecomClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientCurrent24StatUasValuePortn.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryPort1Table_Object = MibTable
pmc2002PerfTelecomClientPast24StatHistoryPort1Table = _Pmc2002PerfTelecomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryPort1Table.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pmc2002PerfTelecomClientPast24StatHistoryPort1Entry = _Pmc2002PerfTelecomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1)
)
pmc2002PerfTelecomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pmc2002PerfTelecomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc2002PerfTelecomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryPort1Index = _Pmc2002PerfTelecomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 1),
    _Pmc2002PerfTelecomClientPast24StatHistoryPort1Index_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryPort1Index.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1 = _Pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 2),
    _Pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1 = _Pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 3),
    _Pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1 = _Pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 4),
    _Pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1 = _Pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 5),
    _Pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1 = _Pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 6),
    _Pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistorySesValuePort1 = _Pmc2002PerfTelecomClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 7),
    _Pmc2002PerfTelecomClientPast24StatHistorySesValuePort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistorySesValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1 = _Pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 8),
    _Pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1 = _Pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 9),
    _Pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1 = _Pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 10),
    _Pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1 = _Pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 40, 1, 11),
    _Pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1_Type()
)
pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pmc2002PerfDatacomClientCurrent15StatTable_Object = MibTable
pmc2002PerfDatacomClientCurrent15StatTable = _Pmc2002PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256)
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientCurrent15StatTable.setStatus("current")
_Pmc2002PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pmc2002PerfDatacomClientCurrent15StatEntry = _Pmc2002PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1)
)
pmc2002PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pmc2002PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pmc2002PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc2002PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pmc2002PerfDatacomClientCurrent15StatIndex = _Pmc2002PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 1),
    _Pmc2002PerfDatacomClientCurrent15StatIndex_Type()
)
pmc2002PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 2),
    _Pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInBytesCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatInBytesCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInBytesCountPortn = _Pmc2002perfdatacomclientCurrent15StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 3),
    _Pmc2002perfdatacomclientCurrent15StatInBytesCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInBytesCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 4),
    _Pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInCrcCountPortn = _Pmc2002perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 5),
    _Pmc2002perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 8),
    _Pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn = _Pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 9),
    _Pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 10),
    _Pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn = _Pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 11),
    _Pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 20),
    _Pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn = _Pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 21),
    _Pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 22),
    _Pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn = _Pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 23),
    _Pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 26),
    _Pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn = _Pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 27),
    _Pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 32),
    _Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn = _Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 33),
    _Pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 34),
    _Pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn = _Pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 35),
    _Pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 42),
    _Pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn = _Pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 43),
    _Pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn = _Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 44),
    _Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn = _Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 256, 1, 45),
    _Pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn.setStatus("current")
_Pmc2002PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pmc2002PerfDatacomClientPast15StatHistoryPort1Table = _Pmc2002PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264)
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pmc2002PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pmc2002PerfDatacomClientPast15StatHistoryPort1Entry = _Pmc2002PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1)
)
pmc2002PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pmc2002PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc2002PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc2002PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pmc2002PerfDatacomClientPast15StatHistoryPort1Index = _Pmc2002PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 1),
    _Pmc2002PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pmc2002PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInBytesCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatInBytesCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInBytesCountInvPort1 = _Pmc2002perfdatacomclientPast15StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 2),
    _Pmc2002perfdatacomclientPast15StatInBytesCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInBytesCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInBytesCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatInBytesCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInBytesCountPort1 = _Pmc2002perfdatacomclientPast15StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 3),
    _Pmc2002perfdatacomclientPast15StatInBytesCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInBytesCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInCrcCountInvPort1 = _Pmc2002perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 4),
    _Pmc2002perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInCrcCountPort1 = _Pmc2002perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 5),
    _Pmc2002perfdatacomclientPast15StatInCrcCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 8),
    _Pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInBroadcastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatInBroadcastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInBroadcastCountPort1 = _Pmc2002perfdatacomclientPast15StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 9),
    _Pmc2002perfdatacomclientPast15StatInBroadcastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInBroadcastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 10),
    _Pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInMulticastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatInMulticastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInMulticastCountPort1 = _Pmc2002perfdatacomclientPast15StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 11),
    _Pmc2002perfdatacomclientPast15StatInMulticastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInMulticastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 20),
    _Pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInUnicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatInUnicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInUnicastCountPort1 = _Pmc2002perfdatacomclientPast15StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 21),
    _Pmc2002perfdatacomclientPast15StatInUnicastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInUnicastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 22),
    _Pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatInNonunicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatInNonunicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatInNonunicastCountPort1 = _Pmc2002perfdatacomclientPast15StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 23),
    _Pmc2002perfdatacomclientPast15StatInNonunicastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatInNonunicastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1 = _Pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 26),
    _Pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutBytesCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatOutBytesCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutBytesCountPort1 = _Pmc2002perfdatacomclientPast15StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 27),
    _Pmc2002perfdatacomclientPast15StatOutBytesCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutBytesCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 32),
    _Pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1 = _Pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 33),
    _Pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 34),
    _Pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutMulticastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatOutMulticastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutMulticastCountPort1 = _Pmc2002perfdatacomclientPast15StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 35),
    _Pmc2002perfdatacomclientPast15StatOutMulticastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutMulticastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 42),
    _Pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutUnicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatOutUnicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutUnicastCountPort1 = _Pmc2002perfdatacomclientPast15StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 43),
    _Pmc2002perfdatacomclientPast15StatOutUnicastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutUnicastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1 = _Pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 44),
    _Pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1 = _Pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 264, 1, 45),
    _Pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1_Type()
)
pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1.setStatus("current")
_Pmc2002PerfDatacomClientCurrent24StatTable_Object = MibTable
pmc2002PerfDatacomClientCurrent24StatTable = _Pmc2002PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272)
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientCurrent24StatTable.setStatus("current")
_Pmc2002PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pmc2002PerfDatacomClientCurrent24StatEntry = _Pmc2002PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1)
)
pmc2002PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pmc2002PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pmc2002PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc2002PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pmc2002PerfDatacomClientCurrent24StatIndex = _Pmc2002PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 1),
    _Pmc2002PerfDatacomClientCurrent24StatIndex_Type()
)
pmc2002PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 2),
    _Pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInBytesCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatInBytesCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInBytesCountPortn = _Pmc2002perfdatacomclientCurrent24StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 3),
    _Pmc2002perfdatacomclientCurrent24StatInBytesCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInBytesCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 4),
    _Pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInCrcCountPortn = _Pmc2002perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 5),
    _Pmc2002perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 8),
    _Pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn = _Pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 9),
    _Pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 10),
    _Pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn = _Pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 11),
    _Pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 20),
    _Pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn = _Pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 21),
    _Pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 22),
    _Pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn = _Pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 23),
    _Pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 26),
    _Pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn = _Pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 27),
    _Pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 32),
    _Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn = _Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 33),
    _Pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 34),
    _Pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn = _Pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 35),
    _Pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 42),
    _Pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn = _Pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 43),
    _Pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn = _Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 44),
    _Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setStatus("current")
_Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Type = Counter64
_Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Object = MibTableColumn
pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn = _Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 272, 1, 45),
    _Pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Type()
)
pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn.setStatus("current")
_Pmc2002PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pmc2002PerfDatacomClientPast24StatHistoryPort1Table = _Pmc2002PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280)
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pmc2002PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pmc2002PerfDatacomClientPast24StatHistoryPort1Entry = _Pmc2002PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1)
)
pmc2002PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pmc2002PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc2002PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc2002PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pmc2002PerfDatacomClientPast24StatHistoryPort1Index = _Pmc2002PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 1),
    _Pmc2002PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pmc2002PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInBytesCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatInBytesCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInBytesCountInvPort1 = _Pmc2002perfdatacomclientPast24StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 2),
    _Pmc2002perfdatacomclientPast24StatInBytesCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInBytesCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInBytesCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatInBytesCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInBytesCountPort1 = _Pmc2002perfdatacomclientPast24StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 3),
    _Pmc2002perfdatacomclientPast24StatInBytesCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInBytesCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInCrcCountInvPort1 = _Pmc2002perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 4),
    _Pmc2002perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInCrcCountPort1 = _Pmc2002perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 5),
    _Pmc2002perfdatacomclientPast24StatInCrcCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 8),
    _Pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInBroadcastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatInBroadcastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInBroadcastCountPort1 = _Pmc2002perfdatacomclientPast24StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 9),
    _Pmc2002perfdatacomclientPast24StatInBroadcastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInBroadcastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 10),
    _Pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInMulticastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatInMulticastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInMulticastCountPort1 = _Pmc2002perfdatacomclientPast24StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 11),
    _Pmc2002perfdatacomclientPast24StatInMulticastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInMulticastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 20),
    _Pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInUnicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatInUnicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInUnicastCountPort1 = _Pmc2002perfdatacomclientPast24StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 21),
    _Pmc2002perfdatacomclientPast24StatInUnicastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInUnicastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 22),
    _Pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatInNonunicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatInNonunicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatInNonunicastCountPort1 = _Pmc2002perfdatacomclientPast24StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 23),
    _Pmc2002perfdatacomclientPast24StatInNonunicastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatInNonunicastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1 = _Pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 26),
    _Pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutBytesCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatOutBytesCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutBytesCountPort1 = _Pmc2002perfdatacomclientPast24StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 27),
    _Pmc2002perfdatacomclientPast24StatOutBytesCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutBytesCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 32),
    _Pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1 = _Pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 33),
    _Pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 34),
    _Pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutMulticastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatOutMulticastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutMulticastCountPort1 = _Pmc2002perfdatacomclientPast24StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 35),
    _Pmc2002perfdatacomclientPast24StatOutMulticastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutMulticastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 42),
    _Pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutUnicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatOutUnicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutUnicastCountPort1 = _Pmc2002perfdatacomclientPast24StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 43),
    _Pmc2002perfdatacomclientPast24StatOutUnicastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutUnicastCountPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1 = _Pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 44),
    _Pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1.setStatus("current")
_Pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1_Type = Counter64
_Pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1_Object = MibTableColumn
pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1 = _Pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 2, 280, 1, 45),
    _Pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1_Type()
)
pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1.setStatus("current")
_Pmc2002MonLine_ObjectIdentity = ObjectIdentity
pmc2002MonLine = _Pmc2002MonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3)
)
_Pmc2002PerfTelecomLineCurrent15StatTable_Object = MibTable
pmc2002PerfTelecomLineCurrent15StatTable = _Pmc2002PerfTelecomLineCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatTable.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatEntry_Object = MibTableRow
pmc2002PerfTelecomLineCurrent15StatEntry = _Pmc2002PerfTelecomLineCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1)
)
pmc2002PerfTelecomLineCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomLineCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatEntry.setStatus("current")


class _Pmc2002PerfTelecomLineCurrent15StatIndex_Type(Integer32):
    """Custom type pmc2002PerfTelecomLineCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomLineCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomLineCurrent15StatIndex_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatIndex = _Pmc2002PerfTelecomLineCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 1),
    _Pmc2002PerfTelecomLineCurrent15StatIndex_Type()
)
pmc2002PerfTelecomLineCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatIndex.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatInvCvPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent15StatInvCvPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatInvCvPortn = _Pmc2002PerfTelecomLineCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 2),
    _Pmc2002PerfTelecomLineCurrent15StatInvCvPortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatInvCvPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatCvValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent15StatCvValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatCvValuePortn = _Pmc2002PerfTelecomLineCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 3),
    _Pmc2002PerfTelecomLineCurrent15StatCvValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatCvValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatInvEsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent15StatInvEsPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatInvEsPortn = _Pmc2002PerfTelecomLineCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 4),
    _Pmc2002PerfTelecomLineCurrent15StatInvEsPortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatInvEsPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatEsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent15StatEsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatEsValuePortn = _Pmc2002PerfTelecomLineCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 5),
    _Pmc2002PerfTelecomLineCurrent15StatEsValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatEsValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatInvSesPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent15StatInvSesPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatInvSesPortn = _Pmc2002PerfTelecomLineCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 6),
    _Pmc2002PerfTelecomLineCurrent15StatInvSesPortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatInvSesPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatSesValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent15StatSesValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatSesValuePortn = _Pmc2002PerfTelecomLineCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 7),
    _Pmc2002PerfTelecomLineCurrent15StatSesValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatSesValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent15StatInvSefsPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatInvSefsPortn = _Pmc2002PerfTelecomLineCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 8),
    _Pmc2002PerfTelecomLineCurrent15StatInvSefsPortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatInvSefsPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatSefsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent15StatSefsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatSefsValuePortn = _Pmc2002PerfTelecomLineCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 9),
    _Pmc2002PerfTelecomLineCurrent15StatSefsValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatSefsValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatInvUasPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent15StatInvUasPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatInvUasPortn = _Pmc2002PerfTelecomLineCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 10),
    _Pmc2002PerfTelecomLineCurrent15StatInvUasPortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatInvUasPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent15StatUasValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent15StatUasValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent15StatUasValuePortn = _Pmc2002PerfTelecomLineCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 128, 1, 11),
    _Pmc2002PerfTelecomLineCurrent15StatUasValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent15StatUasValuePortn.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryPort1Table_Object = MibTable
pmc2002PerfTelecomLinePast15StatHistoryPort1Table = _Pmc2002PerfTelecomLinePast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryPort1Table.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryPort1Entry_Object = MibTableRow
pmc2002PerfTelecomLinePast15StatHistoryPort1Entry = _Pmc2002PerfTelecomLinePast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1)
)
pmc2002PerfTelecomLinePast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomLinePast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryPort1Entry.setStatus("current")


class _Pmc2002PerfTelecomLinePast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc2002PerfTelecomLinePast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomLinePast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomLinePast15StatHistoryPort1Index_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryPort1Index = _Pmc2002PerfTelecomLinePast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 1),
    _Pmc2002PerfTelecomLinePast15StatHistoryPort1Index_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryPort1Index.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1 = _Pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 2),
    _Pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1 = _Pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 3),
    _Pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1 = _Pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 4),
    _Pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1 = _Pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 5),
    _Pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1 = _Pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 6),
    _Pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistorySesValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast15StatHistorySesValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistorySesValuePort1 = _Pmc2002PerfTelecomLinePast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 7),
    _Pmc2002PerfTelecomLinePast15StatHistorySesValuePort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistorySesValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1 = _Pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 8),
    _Pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1 = _Pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 9),
    _Pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1 = _Pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 10),
    _Pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1 = _Pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 129, 1, 11),
    _Pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1_Type()
)
pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatTable_Object = MibTable
pmc2002PerfTelecomLineCurrent24StatTable = _Pmc2002PerfTelecomLineCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatTable.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatEntry_Object = MibTableRow
pmc2002PerfTelecomLineCurrent24StatEntry = _Pmc2002PerfTelecomLineCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1)
)
pmc2002PerfTelecomLineCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomLineCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatEntry.setStatus("current")


class _Pmc2002PerfTelecomLineCurrent24StatIndex_Type(Integer32):
    """Custom type pmc2002PerfTelecomLineCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomLineCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomLineCurrent24StatIndex_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatIndex = _Pmc2002PerfTelecomLineCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 1),
    _Pmc2002PerfTelecomLineCurrent24StatIndex_Type()
)
pmc2002PerfTelecomLineCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatIndex.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatInvCvPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent24StatInvCvPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatInvCvPortn = _Pmc2002PerfTelecomLineCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 2),
    _Pmc2002PerfTelecomLineCurrent24StatInvCvPortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatInvCvPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatCvValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent24StatCvValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatCvValuePortn = _Pmc2002PerfTelecomLineCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 3),
    _Pmc2002PerfTelecomLineCurrent24StatCvValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatCvValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatInvEsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent24StatInvEsPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatInvEsPortn = _Pmc2002PerfTelecomLineCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 4),
    _Pmc2002PerfTelecomLineCurrent24StatInvEsPortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatInvEsPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatEsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent24StatEsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatEsValuePortn = _Pmc2002PerfTelecomLineCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 5),
    _Pmc2002PerfTelecomLineCurrent24StatEsValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatEsValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatInvSesPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent24StatInvSesPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatInvSesPortn = _Pmc2002PerfTelecomLineCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 6),
    _Pmc2002PerfTelecomLineCurrent24StatInvSesPortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatInvSesPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatSesValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent24StatSesValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatSesValuePortn = _Pmc2002PerfTelecomLineCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 7),
    _Pmc2002PerfTelecomLineCurrent24StatSesValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatSesValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent24StatInvSefsPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatInvSefsPortn = _Pmc2002PerfTelecomLineCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 8),
    _Pmc2002PerfTelecomLineCurrent24StatInvSefsPortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatInvSefsPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatSefsValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent24StatSefsValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatSefsValuePortn = _Pmc2002PerfTelecomLineCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 9),
    _Pmc2002PerfTelecomLineCurrent24StatSefsValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatSefsValuePortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatInvUasPortn_Type = EkiOnOff
_Pmc2002PerfTelecomLineCurrent24StatInvUasPortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatInvUasPortn = _Pmc2002PerfTelecomLineCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 10),
    _Pmc2002PerfTelecomLineCurrent24StatInvUasPortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatInvUasPortn.setStatus("current")
_Pmc2002PerfTelecomLineCurrent24StatUasValuePortn_Type = Unsigned32
_Pmc2002PerfTelecomLineCurrent24StatUasValuePortn_Object = MibTableColumn
pmc2002PerfTelecomLineCurrent24StatUasValuePortn = _Pmc2002PerfTelecomLineCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 130, 1, 11),
    _Pmc2002PerfTelecomLineCurrent24StatUasValuePortn_Type()
)
pmc2002PerfTelecomLineCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLineCurrent24StatUasValuePortn.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryPort1Table_Object = MibTable
pmc2002PerfTelecomLinePast24StatHistoryPort1Table = _Pmc2002PerfTelecomLinePast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131)
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryPort1Table.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryPort1Entry_Object = MibTableRow
pmc2002PerfTelecomLinePast24StatHistoryPort1Entry = _Pmc2002PerfTelecomLinePast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1)
)
pmc2002PerfTelecomLinePast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002PerfTelecomLinePast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryPort1Entry.setStatus("current")


class _Pmc2002PerfTelecomLinePast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc2002PerfTelecomLinePast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002PerfTelecomLinePast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc2002PerfTelecomLinePast24StatHistoryPort1Index_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryPort1Index = _Pmc2002PerfTelecomLinePast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 1),
    _Pmc2002PerfTelecomLinePast24StatHistoryPort1Index_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryPort1Index.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1 = _Pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 2),
    _Pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1 = _Pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 3),
    _Pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1 = _Pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 4),
    _Pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1 = _Pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 5),
    _Pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1 = _Pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 6),
    _Pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistorySesValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast24StatHistorySesValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistorySesValuePort1 = _Pmc2002PerfTelecomLinePast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 7),
    _Pmc2002PerfTelecomLinePast24StatHistorySesValuePort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistorySesValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1 = _Pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 8),
    _Pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1 = _Pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 9),
    _Pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1 = _Pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 10),
    _Pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1.setStatus("current")
_Pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1_Type = Unsigned32
_Pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1_Object = MibTableColumn
pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1 = _Pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 3, 131, 1, 11),
    _Pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1_Type()
)
pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1.setStatus("current")
_Pmc2002Rmon_ObjectIdentity = ObjectIdentity
pmc2002Rmon = _Pmc2002Rmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4)
)
_Pmc2002RmonClient_ObjectIdentity = ObjectIdentity
pmc2002RmonClient = _Pmc2002RmonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1)
)
_Pmc2002MonupRmonByteCntTable_Object = MibTable
pmc2002MonupRmonByteCntTable = _Pmc2002MonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 16)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonByteCntTable.setStatus("current")
_Pmc2002MonupRmonByteCntEntry_Object = MibTableRow
pmc2002MonupRmonByteCntEntry = _Pmc2002MonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 16, 1)
)
pmc2002MonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonByteCntEntry.setStatus("current")


class _Pmc2002MonupRmonByteCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonByteCntIndex_Object = MibTableColumn
pmc2002MonupRmonByteCntIndex = _Pmc2002MonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 16, 1, 1),
    _Pmc2002MonupRmonByteCntIndex_Type()
)
pmc2002MonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonByteCntIndex.setStatus("current")
_Pmc2002MonupRmonByteCntValuePortn_Type = Counter64
_Pmc2002MonupRmonByteCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonByteCntValuePortn = _Pmc2002MonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 16, 1, 2),
    _Pmc2002MonupRmonByteCntValuePortn_Type()
)
pmc2002MonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonByteCntValuePortn.setStatus("current")
_Pmc2002MonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonByteCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonByteCntErrorPortn = _Pmc2002MonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 16, 1, 3),
    _Pmc2002MonupRmonByteCntErrorPortn_Type()
)
pmc2002MonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonByteCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonByteCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonByteCntOverloadPortn = _Pmc2002MonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 16, 1, 4),
    _Pmc2002MonupRmonByteCntOverloadPortn_Type()
)
pmc2002MonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonByteCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonCrcErrorCntTable_Object = MibTable
pmc2002MonupRmonCrcErrorCntTable = _Pmc2002MonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 24)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonCrcErrorCntTable.setStatus("current")
_Pmc2002MonupRmonCrcErrorCntEntry_Object = MibTableRow
pmc2002MonupRmonCrcErrorCntEntry = _Pmc2002MonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 24, 1)
)
pmc2002MonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonCrcErrorCntEntry.setStatus("current")


class _Pmc2002MonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonCrcErrorCntIndex_Object = MibTableColumn
pmc2002MonupRmonCrcErrorCntIndex = _Pmc2002MonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 24, 1, 1),
    _Pmc2002MonupRmonCrcErrorCntIndex_Type()
)
pmc2002MonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonCrcErrorCntIndex.setStatus("current")
_Pmc2002MonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pmc2002MonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonCrcErrorCntValuePortn = _Pmc2002MonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 24, 1, 2),
    _Pmc2002MonupRmonCrcErrorCntValuePortn_Type()
)
pmc2002MonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pmc2002MonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonCrcErrorCntErrorPortn = _Pmc2002MonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 24, 1, 3),
    _Pmc2002MonupRmonCrcErrorCntErrorPortn_Type()
)
pmc2002MonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonCrcErrorCntOverloadPortn = _Pmc2002MonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 24, 1, 4),
    _Pmc2002MonupRmonCrcErrorCntOverloadPortn_Type()
)
pmc2002MonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonPacketsCntTable_Object = MibTable
pmc2002MonupRmonPacketsCntTable = _Pmc2002MonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 32)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonPacketsCntTable.setStatus("current")
_Pmc2002MonupRmonPacketsCntEntry_Object = MibTableRow
pmc2002MonupRmonPacketsCntEntry = _Pmc2002MonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 32, 1)
)
pmc2002MonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonPacketsCntEntry.setStatus("current")


class _Pmc2002MonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonPacketsCntIndex_Object = MibTableColumn
pmc2002MonupRmonPacketsCntIndex = _Pmc2002MonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 32, 1, 1),
    _Pmc2002MonupRmonPacketsCntIndex_Type()
)
pmc2002MonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPacketsCntIndex.setStatus("current")
_Pmc2002MonupRmonPacketsCntValuePortn_Type = Counter64
_Pmc2002MonupRmonPacketsCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonPacketsCntValuePortn = _Pmc2002MonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 32, 1, 2),
    _Pmc2002MonupRmonPacketsCntValuePortn_Type()
)
pmc2002MonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPacketsCntValuePortn.setStatus("current")
_Pmc2002MonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonPacketsCntErrorPortn = _Pmc2002MonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 32, 1, 3),
    _Pmc2002MonupRmonPacketsCntErrorPortn_Type()
)
pmc2002MonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPacketsCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonPacketsCntOverloadPortn = _Pmc2002MonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 32, 1, 4),
    _Pmc2002MonupRmonPacketsCntOverloadPortn_Type()
)
pmc2002MonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonBroadcastCntTable_Object = MibTable
pmc2002MonupRmonBroadcastCntTable = _Pmc2002MonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 40)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonBroadcastCntTable.setStatus("current")
_Pmc2002MonupRmonBroadcastCntEntry_Object = MibTableRow
pmc2002MonupRmonBroadcastCntEntry = _Pmc2002MonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 40, 1)
)
pmc2002MonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonBroadcastCntEntry.setStatus("current")


class _Pmc2002MonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonBroadcastCntIndex_Object = MibTableColumn
pmc2002MonupRmonBroadcastCntIndex = _Pmc2002MonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 40, 1, 1),
    _Pmc2002MonupRmonBroadcastCntIndex_Type()
)
pmc2002MonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBroadcastCntIndex.setStatus("current")
_Pmc2002MonupRmonBroadcastCntValuePortn_Type = Counter64
_Pmc2002MonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonBroadcastCntValuePortn = _Pmc2002MonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 40, 1, 2),
    _Pmc2002MonupRmonBroadcastCntValuePortn_Type()
)
pmc2002MonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBroadcastCntValuePortn.setStatus("current")
_Pmc2002MonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonBroadcastCntErrorPortn = _Pmc2002MonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 40, 1, 3),
    _Pmc2002MonupRmonBroadcastCntErrorPortn_Type()
)
pmc2002MonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonBroadcastCntOverloadPortn = _Pmc2002MonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 40, 1, 4),
    _Pmc2002MonupRmonBroadcastCntOverloadPortn_Type()
)
pmc2002MonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonMulticastCntTable_Object = MibTable
pmc2002MonupRmonMulticastCntTable = _Pmc2002MonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 48)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonMulticastCntTable.setStatus("current")
_Pmc2002MonupRmonMulticastCntEntry_Object = MibTableRow
pmc2002MonupRmonMulticastCntEntry = _Pmc2002MonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 48, 1)
)
pmc2002MonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonMulticastCntEntry.setStatus("current")


class _Pmc2002MonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonMulticastCntIndex_Object = MibTableColumn
pmc2002MonupRmonMulticastCntIndex = _Pmc2002MonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 48, 1, 1),
    _Pmc2002MonupRmonMulticastCntIndex_Type()
)
pmc2002MonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonMulticastCntIndex.setStatus("current")
_Pmc2002MonupRmonMulticastCntValuePortn_Type = Counter64
_Pmc2002MonupRmonMulticastCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonMulticastCntValuePortn = _Pmc2002MonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 48, 1, 2),
    _Pmc2002MonupRmonMulticastCntValuePortn_Type()
)
pmc2002MonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonMulticastCntValuePortn.setStatus("current")
_Pmc2002MonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonMulticastCntErrorPortn = _Pmc2002MonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 48, 1, 3),
    _Pmc2002MonupRmonMulticastCntErrorPortn_Type()
)
pmc2002MonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonMulticastCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonMulticastCntOverloadPortn = _Pmc2002MonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 48, 1, 4),
    _Pmc2002MonupRmonMulticastCntOverloadPortn_Type()
)
pmc2002MonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonTimerCntTable_Object = MibTable
pmc2002MonupRmonTimerCntTable = _Pmc2002MonupRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 56)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonTimerCntTable.setStatus("current")
_Pmc2002MonupRmonTimerCntEntry_Object = MibTableRow
pmc2002MonupRmonTimerCntEntry = _Pmc2002MonupRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 56, 1)
)
pmc2002MonupRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonTimerCntEntry.setStatus("current")


class _Pmc2002MonupRmonTimerCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonTimerCntIndex_Object = MibTableColumn
pmc2002MonupRmonTimerCntIndex = _Pmc2002MonupRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 56, 1, 1),
    _Pmc2002MonupRmonTimerCntIndex_Type()
)
pmc2002MonupRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonTimerCntIndex.setStatus("current")
_Pmc2002MonupRmonTimerCntValuePortn_Type = Counter64
_Pmc2002MonupRmonTimerCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonTimerCntValuePortn = _Pmc2002MonupRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 56, 1, 2),
    _Pmc2002MonupRmonTimerCntValuePortn_Type()
)
pmc2002MonupRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonTimerCntValuePortn.setStatus("current")
_Pmc2002MonupRmonTimerCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonTimerCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonTimerCntErrorPortn = _Pmc2002MonupRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 56, 1, 3),
    _Pmc2002MonupRmonTimerCntErrorPortn_Type()
)
pmc2002MonupRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonTimerCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonTimerCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonTimerCntOverloadPortn = _Pmc2002MonupRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 56, 1, 4),
    _Pmc2002MonupRmonTimerCntOverloadPortn_Type()
)
pmc2002MonupRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonTimerCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonPauseFrameCntTable_Object = MibTable
pmc2002MonupRmonPauseFrameCntTable = _Pmc2002MonupRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 64)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonPauseFrameCntTable.setStatus("current")
_Pmc2002MonupRmonPauseFrameCntEntry_Object = MibTableRow
pmc2002MonupRmonPauseFrameCntEntry = _Pmc2002MonupRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 64, 1)
)
pmc2002MonupRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonPauseFrameCntEntry.setStatus("current")


class _Pmc2002MonupRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonPauseFrameCntIndex_Object = MibTableColumn
pmc2002MonupRmonPauseFrameCntIndex = _Pmc2002MonupRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 64, 1, 1),
    _Pmc2002MonupRmonPauseFrameCntIndex_Type()
)
pmc2002MonupRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPauseFrameCntIndex.setStatus("current")
_Pmc2002MonupRmonPauseFrameCntValuePortn_Type = Counter64
_Pmc2002MonupRmonPauseFrameCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonPauseFrameCntValuePortn = _Pmc2002MonupRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 64, 1, 2),
    _Pmc2002MonupRmonPauseFrameCntValuePortn_Type()
)
pmc2002MonupRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPauseFrameCntValuePortn.setStatus("current")
_Pmc2002MonupRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonPauseFrameCntErrorPortn = _Pmc2002MonupRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 64, 1, 3),
    _Pmc2002MonupRmonPauseFrameCntErrorPortn_Type()
)
pmc2002MonupRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPauseFrameCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonPauseFrameCntOverloadPortn = _Pmc2002MonupRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 64, 1, 4),
    _Pmc2002MonupRmonPauseFrameCntOverloadPortn_Type()
)
pmc2002MonupRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonDropFrameCntTable_Object = MibTable
pmc2002MonupRmonDropFrameCntTable = _Pmc2002MonupRmonDropFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 72)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonDropFrameCntTable.setStatus("current")
_Pmc2002MonupRmonDropFrameCntEntry_Object = MibTableRow
pmc2002MonupRmonDropFrameCntEntry = _Pmc2002MonupRmonDropFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 72, 1)
)
pmc2002MonupRmonDropFrameCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonDropFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonDropFrameCntEntry.setStatus("current")


class _Pmc2002MonupRmonDropFrameCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonDropFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonDropFrameCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonDropFrameCntIndex_Object = MibTableColumn
pmc2002MonupRmonDropFrameCntIndex = _Pmc2002MonupRmonDropFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 72, 1, 1),
    _Pmc2002MonupRmonDropFrameCntIndex_Type()
)
pmc2002MonupRmonDropFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonDropFrameCntIndex.setStatus("current")
_Pmc2002MonupRmonDropFrameCntValuePortn_Type = Counter64
_Pmc2002MonupRmonDropFrameCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonDropFrameCntValuePortn = _Pmc2002MonupRmonDropFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 72, 1, 2),
    _Pmc2002MonupRmonDropFrameCntValuePortn_Type()
)
pmc2002MonupRmonDropFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonDropFrameCntValuePortn.setStatus("current")
_Pmc2002MonupRmonDropFrameCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonDropFrameCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonDropFrameCntErrorPortn = _Pmc2002MonupRmonDropFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 72, 1, 3),
    _Pmc2002MonupRmonDropFrameCntErrorPortn_Type()
)
pmc2002MonupRmonDropFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonDropFrameCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonDropFrameCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonDropFrameCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonDropFrameCntOverloadPortn = _Pmc2002MonupRmonDropFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 72, 1, 4),
    _Pmc2002MonupRmonDropFrameCntOverloadPortn_Type()
)
pmc2002MonupRmonDropFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonDropFrameCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonBitsCntTable_Object = MibTable
pmc2002MonupRmonBitsCntTable = _Pmc2002MonupRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 80)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonBitsCntTable.setStatus("current")
_Pmc2002MonupRmonBitsCntEntry_Object = MibTableRow
pmc2002MonupRmonBitsCntEntry = _Pmc2002MonupRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 80, 1)
)
pmc2002MonupRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonBitsCntEntry.setStatus("current")


class _Pmc2002MonupRmonBitsCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonBitsCntIndex_Object = MibTableColumn
pmc2002MonupRmonBitsCntIndex = _Pmc2002MonupRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 80, 1, 1),
    _Pmc2002MonupRmonBitsCntIndex_Type()
)
pmc2002MonupRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBitsCntIndex.setStatus("current")
_Pmc2002MonupRmonBitsCntValuePortn_Type = Counter64
_Pmc2002MonupRmonBitsCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonBitsCntValuePortn = _Pmc2002MonupRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 80, 1, 2),
    _Pmc2002MonupRmonBitsCntValuePortn_Type()
)
pmc2002MonupRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBitsCntValuePortn.setStatus("current")
_Pmc2002MonupRmonBitsCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonBitsCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonBitsCntErrorPortn = _Pmc2002MonupRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 80, 1, 3),
    _Pmc2002MonupRmonBitsCntErrorPortn_Type()
)
pmc2002MonupRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBitsCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonBitsCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonBitsCntOverloadPortn = _Pmc2002MonupRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 80, 1, 4),
    _Pmc2002MonupRmonBitsCntOverloadPortn_Type()
)
pmc2002MonupRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonBitsCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonUnicastCntTable_Object = MibTable
pmc2002MonupRmonUnicastCntTable = _Pmc2002MonupRmonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 88)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonUnicastCntTable.setStatus("current")
_Pmc2002MonupRmonUnicastCntEntry_Object = MibTableRow
pmc2002MonupRmonUnicastCntEntry = _Pmc2002MonupRmonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 88, 1)
)
pmc2002MonupRmonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonUnicastCntEntry.setStatus("current")


class _Pmc2002MonupRmonUnicastCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonUnicastCntIndex_Object = MibTableColumn
pmc2002MonupRmonUnicastCntIndex = _Pmc2002MonupRmonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 88, 1, 1),
    _Pmc2002MonupRmonUnicastCntIndex_Type()
)
pmc2002MonupRmonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonUnicastCntIndex.setStatus("current")
_Pmc2002MonupRmonUnicastCntValuePortn_Type = Counter64
_Pmc2002MonupRmonUnicastCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonUnicastCntValuePortn = _Pmc2002MonupRmonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 88, 1, 2),
    _Pmc2002MonupRmonUnicastCntValuePortn_Type()
)
pmc2002MonupRmonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonUnicastCntValuePortn.setStatus("current")
_Pmc2002MonupRmonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonUnicastCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonUnicastCntErrorPortn = _Pmc2002MonupRmonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 88, 1, 3),
    _Pmc2002MonupRmonUnicastCntErrorPortn_Type()
)
pmc2002MonupRmonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonUnicastCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonUnicastCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonUnicastCntOverloadPortn = _Pmc2002MonupRmonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 88, 1, 4),
    _Pmc2002MonupRmonUnicastCntOverloadPortn_Type()
)
pmc2002MonupRmonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonUnicastCntOverloadPortn.setStatus("current")
_Pmc2002MonupRmonNonUnicastCntTable_Object = MibTable
pmc2002MonupRmonNonUnicastCntTable = _Pmc2002MonupRmonNonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 96)
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonNonUnicastCntTable.setStatus("current")
_Pmc2002MonupRmonNonUnicastCntEntry_Object = MibTableRow
pmc2002MonupRmonNonUnicastCntEntry = _Pmc2002MonupRmonNonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 96, 1)
)
pmc2002MonupRmonNonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MonupRmonNonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MonupRmonNonUnicastCntEntry.setStatus("current")


class _Pmc2002MonupRmonNonUnicastCntIndex_Type(Integer32):
    """Custom type pmc2002MonupRmonNonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MonupRmonNonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MonupRmonNonUnicastCntIndex_Object = MibTableColumn
pmc2002MonupRmonNonUnicastCntIndex = _Pmc2002MonupRmonNonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 96, 1, 1),
    _Pmc2002MonupRmonNonUnicastCntIndex_Type()
)
pmc2002MonupRmonNonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonNonUnicastCntIndex.setStatus("current")
_Pmc2002MonupRmonNonUnicastCntValuePortn_Type = Counter64
_Pmc2002MonupRmonNonUnicastCntValuePortn_Object = MibTableColumn
pmc2002MonupRmonNonUnicastCntValuePortn = _Pmc2002MonupRmonNonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 96, 1, 2),
    _Pmc2002MonupRmonNonUnicastCntValuePortn_Type()
)
pmc2002MonupRmonNonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonNonUnicastCntValuePortn.setStatus("current")
_Pmc2002MonupRmonNonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc2002MonupRmonNonUnicastCntErrorPortn_Object = MibTableColumn
pmc2002MonupRmonNonUnicastCntErrorPortn = _Pmc2002MonupRmonNonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 96, 1, 3),
    _Pmc2002MonupRmonNonUnicastCntErrorPortn_Type()
)
pmc2002MonupRmonNonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonNonUnicastCntErrorPortn.setStatus("current")
_Pmc2002MonupRmonNonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MonupRmonNonUnicastCntOverloadPortn_Object = MibTableColumn
pmc2002MonupRmonNonUnicastCntOverloadPortn = _Pmc2002MonupRmonNonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 96, 1, 4),
    _Pmc2002MonupRmonNonUnicastCntOverloadPortn_Type()
)
pmc2002MonupRmonNonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MonupRmonNonUnicastCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonByteCntTable_Object = MibTable
pmc2002MondwRmonByteCntTable = _Pmc2002MondwRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 112)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonByteCntTable.setStatus("current")
_Pmc2002MondwRmonByteCntEntry_Object = MibTableRow
pmc2002MondwRmonByteCntEntry = _Pmc2002MondwRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 112, 1)
)
pmc2002MondwRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonByteCntEntry.setStatus("current")


class _Pmc2002MondwRmonByteCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonByteCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonByteCntIndex_Object = MibTableColumn
pmc2002MondwRmonByteCntIndex = _Pmc2002MondwRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 112, 1, 1),
    _Pmc2002MondwRmonByteCntIndex_Type()
)
pmc2002MondwRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonByteCntIndex.setStatus("current")
_Pmc2002MondwRmonByteCntValuePortn_Type = Counter64
_Pmc2002MondwRmonByteCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonByteCntValuePortn = _Pmc2002MondwRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 112, 1, 2),
    _Pmc2002MondwRmonByteCntValuePortn_Type()
)
pmc2002MondwRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonByteCntValuePortn.setStatus("current")
_Pmc2002MondwRmonByteCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonByteCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonByteCntErrorPortn = _Pmc2002MondwRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 112, 1, 3),
    _Pmc2002MondwRmonByteCntErrorPortn_Type()
)
pmc2002MondwRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonByteCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonByteCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonByteCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonByteCntOverloadPortn = _Pmc2002MondwRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 112, 1, 4),
    _Pmc2002MondwRmonByteCntOverloadPortn_Type()
)
pmc2002MondwRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonByteCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonCrcErrorCntTable_Object = MibTable
pmc2002MondwRmonCrcErrorCntTable = _Pmc2002MondwRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 120)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonCrcErrorCntTable.setStatus("current")
_Pmc2002MondwRmonCrcErrorCntEntry_Object = MibTableRow
pmc2002MondwRmonCrcErrorCntEntry = _Pmc2002MondwRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 120, 1)
)
pmc2002MondwRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonCrcErrorCntEntry.setStatus("current")


class _Pmc2002MondwRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonCrcErrorCntIndex_Object = MibTableColumn
pmc2002MondwRmonCrcErrorCntIndex = _Pmc2002MondwRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 120, 1, 1),
    _Pmc2002MondwRmonCrcErrorCntIndex_Type()
)
pmc2002MondwRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonCrcErrorCntIndex.setStatus("current")
_Pmc2002MondwRmonCrcErrorCntValuePortn_Type = Counter64
_Pmc2002MondwRmonCrcErrorCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonCrcErrorCntValuePortn = _Pmc2002MondwRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 120, 1, 2),
    _Pmc2002MondwRmonCrcErrorCntValuePortn_Type()
)
pmc2002MondwRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonCrcErrorCntValuePortn.setStatus("current")
_Pmc2002MondwRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonCrcErrorCntErrorPortn = _Pmc2002MondwRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 120, 1, 3),
    _Pmc2002MondwRmonCrcErrorCntErrorPortn_Type()
)
pmc2002MondwRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonCrcErrorCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonCrcErrorCntOverloadPortn = _Pmc2002MondwRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 120, 1, 4),
    _Pmc2002MondwRmonCrcErrorCntOverloadPortn_Type()
)
pmc2002MondwRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonPacketsCntTable_Object = MibTable
pmc2002MondwRmonPacketsCntTable = _Pmc2002MondwRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 128)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonPacketsCntTable.setStatus("current")
_Pmc2002MondwRmonPacketsCntEntry_Object = MibTableRow
pmc2002MondwRmonPacketsCntEntry = _Pmc2002MondwRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 128, 1)
)
pmc2002MondwRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonPacketsCntEntry.setStatus("current")


class _Pmc2002MondwRmonPacketsCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonPacketsCntIndex_Object = MibTableColumn
pmc2002MondwRmonPacketsCntIndex = _Pmc2002MondwRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 128, 1, 1),
    _Pmc2002MondwRmonPacketsCntIndex_Type()
)
pmc2002MondwRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPacketsCntIndex.setStatus("current")
_Pmc2002MondwRmonPacketsCntValuePortn_Type = Counter64
_Pmc2002MondwRmonPacketsCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonPacketsCntValuePortn = _Pmc2002MondwRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 128, 1, 2),
    _Pmc2002MondwRmonPacketsCntValuePortn_Type()
)
pmc2002MondwRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPacketsCntValuePortn.setStatus("current")
_Pmc2002MondwRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonPacketsCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonPacketsCntErrorPortn = _Pmc2002MondwRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 128, 1, 3),
    _Pmc2002MondwRmonPacketsCntErrorPortn_Type()
)
pmc2002MondwRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPacketsCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonPacketsCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonPacketsCntOverloadPortn = _Pmc2002MondwRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 128, 1, 4),
    _Pmc2002MondwRmonPacketsCntOverloadPortn_Type()
)
pmc2002MondwRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPacketsCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonBroadcastCntTable_Object = MibTable
pmc2002MondwRmonBroadcastCntTable = _Pmc2002MondwRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 136)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonBroadcastCntTable.setStatus("current")
_Pmc2002MondwRmonBroadcastCntEntry_Object = MibTableRow
pmc2002MondwRmonBroadcastCntEntry = _Pmc2002MondwRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 136, 1)
)
pmc2002MondwRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonBroadcastCntEntry.setStatus("current")


class _Pmc2002MondwRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonBroadcastCntIndex_Object = MibTableColumn
pmc2002MondwRmonBroadcastCntIndex = _Pmc2002MondwRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 136, 1, 1),
    _Pmc2002MondwRmonBroadcastCntIndex_Type()
)
pmc2002MondwRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBroadcastCntIndex.setStatus("current")
_Pmc2002MondwRmonBroadcastCntValuePortn_Type = Counter64
_Pmc2002MondwRmonBroadcastCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonBroadcastCntValuePortn = _Pmc2002MondwRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 136, 1, 2),
    _Pmc2002MondwRmonBroadcastCntValuePortn_Type()
)
pmc2002MondwRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBroadcastCntValuePortn.setStatus("current")
_Pmc2002MondwRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonBroadcastCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonBroadcastCntErrorPortn = _Pmc2002MondwRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 136, 1, 3),
    _Pmc2002MondwRmonBroadcastCntErrorPortn_Type()
)
pmc2002MondwRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBroadcastCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonBroadcastCntOverloadPortn = _Pmc2002MondwRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 136, 1, 4),
    _Pmc2002MondwRmonBroadcastCntOverloadPortn_Type()
)
pmc2002MondwRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBroadcastCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonMulticastCntTable_Object = MibTable
pmc2002MondwRmonMulticastCntTable = _Pmc2002MondwRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 144)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonMulticastCntTable.setStatus("current")
_Pmc2002MondwRmonMulticastCntEntry_Object = MibTableRow
pmc2002MondwRmonMulticastCntEntry = _Pmc2002MondwRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 144, 1)
)
pmc2002MondwRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonMulticastCntEntry.setStatus("current")


class _Pmc2002MondwRmonMulticastCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonMulticastCntIndex_Object = MibTableColumn
pmc2002MondwRmonMulticastCntIndex = _Pmc2002MondwRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 144, 1, 1),
    _Pmc2002MondwRmonMulticastCntIndex_Type()
)
pmc2002MondwRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonMulticastCntIndex.setStatus("current")
_Pmc2002MondwRmonMulticastCntValuePortn_Type = Counter64
_Pmc2002MondwRmonMulticastCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonMulticastCntValuePortn = _Pmc2002MondwRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 144, 1, 2),
    _Pmc2002MondwRmonMulticastCntValuePortn_Type()
)
pmc2002MondwRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonMulticastCntValuePortn.setStatus("current")
_Pmc2002MondwRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonMulticastCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonMulticastCntErrorPortn = _Pmc2002MondwRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 144, 1, 3),
    _Pmc2002MondwRmonMulticastCntErrorPortn_Type()
)
pmc2002MondwRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonMulticastCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonMulticastCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonMulticastCntOverloadPortn = _Pmc2002MondwRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 144, 1, 4),
    _Pmc2002MondwRmonMulticastCntOverloadPortn_Type()
)
pmc2002MondwRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonMulticastCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonPauseFrameCntTable_Object = MibTable
pmc2002MondwRmonPauseFrameCntTable = _Pmc2002MondwRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 152)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonPauseFrameCntTable.setStatus("current")
_Pmc2002MondwRmonPauseFrameCntEntry_Object = MibTableRow
pmc2002MondwRmonPauseFrameCntEntry = _Pmc2002MondwRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 152, 1)
)
pmc2002MondwRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonPauseFrameCntEntry.setStatus("current")


class _Pmc2002MondwRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonPauseFrameCntIndex_Object = MibTableColumn
pmc2002MondwRmonPauseFrameCntIndex = _Pmc2002MondwRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 152, 1, 1),
    _Pmc2002MondwRmonPauseFrameCntIndex_Type()
)
pmc2002MondwRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPauseFrameCntIndex.setStatus("current")
_Pmc2002MondwRmonPauseFrameCntValuePortn_Type = Counter64
_Pmc2002MondwRmonPauseFrameCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonPauseFrameCntValuePortn = _Pmc2002MondwRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 152, 1, 2),
    _Pmc2002MondwRmonPauseFrameCntValuePortn_Type()
)
pmc2002MondwRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPauseFrameCntValuePortn.setStatus("current")
_Pmc2002MondwRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonPauseFrameCntErrorPortn = _Pmc2002MondwRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 152, 1, 3),
    _Pmc2002MondwRmonPauseFrameCntErrorPortn_Type()
)
pmc2002MondwRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPauseFrameCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonPauseFrameCntOverloadPortn = _Pmc2002MondwRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 152, 1, 4),
    _Pmc2002MondwRmonPauseFrameCntOverloadPortn_Type()
)
pmc2002MondwRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonTimerCntTable_Object = MibTable
pmc2002MondwRmonTimerCntTable = _Pmc2002MondwRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 160)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonTimerCntTable.setStatus("current")
_Pmc2002MondwRmonTimerCntEntry_Object = MibTableRow
pmc2002MondwRmonTimerCntEntry = _Pmc2002MondwRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 160, 1)
)
pmc2002MondwRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonTimerCntEntry.setStatus("current")


class _Pmc2002MondwRmonTimerCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonTimerCntIndex_Object = MibTableColumn
pmc2002MondwRmonTimerCntIndex = _Pmc2002MondwRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 160, 1, 1),
    _Pmc2002MondwRmonTimerCntIndex_Type()
)
pmc2002MondwRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonTimerCntIndex.setStatus("current")
_Pmc2002MondwRmonTimerCntValuePortn_Type = Counter64
_Pmc2002MondwRmonTimerCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonTimerCntValuePortn = _Pmc2002MondwRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 160, 1, 2),
    _Pmc2002MondwRmonTimerCntValuePortn_Type()
)
pmc2002MondwRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonTimerCntValuePortn.setStatus("current")
_Pmc2002MondwRmonTimerCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonTimerCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonTimerCntErrorPortn = _Pmc2002MondwRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 160, 1, 3),
    _Pmc2002MondwRmonTimerCntErrorPortn_Type()
)
pmc2002MondwRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonTimerCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonTimerCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonTimerCntOverloadPortn = _Pmc2002MondwRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 160, 1, 4),
    _Pmc2002MondwRmonTimerCntOverloadPortn_Type()
)
pmc2002MondwRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonTimerCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonBitsCntTable_Object = MibTable
pmc2002MondwRmonBitsCntTable = _Pmc2002MondwRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 168)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonBitsCntTable.setStatus("current")
_Pmc2002MondwRmonBitsCntEntry_Object = MibTableRow
pmc2002MondwRmonBitsCntEntry = _Pmc2002MondwRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 168, 1)
)
pmc2002MondwRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonBitsCntEntry.setStatus("current")


class _Pmc2002MondwRmonBitsCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonBitsCntIndex_Object = MibTableColumn
pmc2002MondwRmonBitsCntIndex = _Pmc2002MondwRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 168, 1, 1),
    _Pmc2002MondwRmonBitsCntIndex_Type()
)
pmc2002MondwRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBitsCntIndex.setStatus("current")
_Pmc2002MondwRmonBitsCntValuePortn_Type = Counter64
_Pmc2002MondwRmonBitsCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonBitsCntValuePortn = _Pmc2002MondwRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 168, 1, 2),
    _Pmc2002MondwRmonBitsCntValuePortn_Type()
)
pmc2002MondwRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBitsCntValuePortn.setStatus("current")
_Pmc2002MondwRmonBitsCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonBitsCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonBitsCntErrorPortn = _Pmc2002MondwRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 168, 1, 3),
    _Pmc2002MondwRmonBitsCntErrorPortn_Type()
)
pmc2002MondwRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBitsCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonBitsCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonBitsCntOverloadPortn = _Pmc2002MondwRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 168, 1, 4),
    _Pmc2002MondwRmonBitsCntOverloadPortn_Type()
)
pmc2002MondwRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonBitsCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonUnicastCntTable_Object = MibTable
pmc2002MondwRmonUnicastCntTable = _Pmc2002MondwRmonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 176)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonUnicastCntTable.setStatus("current")
_Pmc2002MondwRmonUnicastCntEntry_Object = MibTableRow
pmc2002MondwRmonUnicastCntEntry = _Pmc2002MondwRmonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 176, 1)
)
pmc2002MondwRmonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonUnicastCntEntry.setStatus("current")


class _Pmc2002MondwRmonUnicastCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonUnicastCntIndex_Object = MibTableColumn
pmc2002MondwRmonUnicastCntIndex = _Pmc2002MondwRmonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 176, 1, 1),
    _Pmc2002MondwRmonUnicastCntIndex_Type()
)
pmc2002MondwRmonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonUnicastCntIndex.setStatus("current")
_Pmc2002MondwRmonUnicastCntValuePortn_Type = Counter64
_Pmc2002MondwRmonUnicastCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonUnicastCntValuePortn = _Pmc2002MondwRmonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 176, 1, 2),
    _Pmc2002MondwRmonUnicastCntValuePortn_Type()
)
pmc2002MondwRmonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonUnicastCntValuePortn.setStatus("current")
_Pmc2002MondwRmonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonUnicastCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonUnicastCntErrorPortn = _Pmc2002MondwRmonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 176, 1, 3),
    _Pmc2002MondwRmonUnicastCntErrorPortn_Type()
)
pmc2002MondwRmonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonUnicastCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonUnicastCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonUnicastCntOverloadPortn = _Pmc2002MondwRmonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 176, 1, 4),
    _Pmc2002MondwRmonUnicastCntOverloadPortn_Type()
)
pmc2002MondwRmonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonUnicastCntOverloadPortn.setStatus("current")
_Pmc2002MondwRmonNonUnicastCntTable_Object = MibTable
pmc2002MondwRmonNonUnicastCntTable = _Pmc2002MondwRmonNonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 184)
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonNonUnicastCntTable.setStatus("current")
_Pmc2002MondwRmonNonUnicastCntEntry_Object = MibTableRow
pmc2002MondwRmonNonUnicastCntEntry = _Pmc2002MondwRmonNonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 184, 1)
)
pmc2002MondwRmonNonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC2002-MIB", "pmc2002MondwRmonNonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc2002MondwRmonNonUnicastCntEntry.setStatus("current")


class _Pmc2002MondwRmonNonUnicastCntIndex_Type(Integer32):
    """Custom type pmc2002MondwRmonNonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc2002MondwRmonNonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc2002MondwRmonNonUnicastCntIndex_Object = MibTableColumn
pmc2002MondwRmonNonUnicastCntIndex = _Pmc2002MondwRmonNonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 184, 1, 1),
    _Pmc2002MondwRmonNonUnicastCntIndex_Type()
)
pmc2002MondwRmonNonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonNonUnicastCntIndex.setStatus("current")
_Pmc2002MondwRmonNonUnicastCntValuePortn_Type = Counter64
_Pmc2002MondwRmonNonUnicastCntValuePortn_Object = MibTableColumn
pmc2002MondwRmonNonUnicastCntValuePortn = _Pmc2002MondwRmonNonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 184, 1, 2),
    _Pmc2002MondwRmonNonUnicastCntValuePortn_Type()
)
pmc2002MondwRmonNonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonNonUnicastCntValuePortn.setStatus("current")
_Pmc2002MondwRmonNonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc2002MondwRmonNonUnicastCntErrorPortn_Object = MibTableColumn
pmc2002MondwRmonNonUnicastCntErrorPortn = _Pmc2002MondwRmonNonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 184, 1, 3),
    _Pmc2002MondwRmonNonUnicastCntErrorPortn_Type()
)
pmc2002MondwRmonNonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonNonUnicastCntErrorPortn.setStatus("current")
_Pmc2002MondwRmonNonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc2002MondwRmonNonUnicastCntOverloadPortn_Object = MibTableColumn
pmc2002MondwRmonNonUnicastCntOverloadPortn = _Pmc2002MondwRmonNonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 1, 184, 1, 4),
    _Pmc2002MondwRmonNonUnicastCntOverloadPortn_Type()
)
pmc2002MondwRmonNonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc2002MondwRmonNonUnicastCntOverloadPortn.setStatus("current")
_Pmc2002RmonLine_ObjectIdentity = ObjectIdentity
pmc2002RmonLine = _Pmc2002RmonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 2)
)
_Pmc2002RmonOther_ObjectIdentity = ObjectIdentity
pmc2002RmonOther = _Pmc2002RmonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 3)
)
_Pmc2002MonCountersReset_Type = EkiOnOff
_Pmc2002MonCountersReset_Object = MibScalar
pmc2002MonCountersReset = _Pmc2002MonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 3, 359),
    _Pmc2002MonCountersReset_Type()
)
pmc2002MonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002MonCountersReset.setStatus("current")
_Pmc2002MonCountersStop_Type = EkiOnOff
_Pmc2002MonCountersStop_Object = MibScalar
pmc2002MonCountersStop = _Pmc2002MonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 52, 12, 4, 3, 360),
    _Pmc2002MonCountersStop_Type()
)
pmc2002MonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc2002MonCountersStop.setStatus("current")

# Managed Objects groups


# Notification objects

pmc2002LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 30)
)
pmc2002LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmLineDdmWarningPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapLineNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmc2002LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 31)
)
pmc2002LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmLineDdmWarningPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapLineNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmc2002LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 32)
)
pmc2002LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmLineDdmAlmPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapLineNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc2002LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 33)
)
pmc2002LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmLineDdmAlmPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapLineNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmc2002LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 34)
)
pmc2002LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmLineFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002AlmLineHwFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapLineNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002LineTrapCritGoesOn.setStatus(
        "current"
    )

pmc2002LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 35)
)
pmc2002LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmLineFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002AlmLineHwFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapLineNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002LineTrapCritGoesOff.setStatus(
        "current"
    )

pmc2002ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 40)
)
pmc2002ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapClientNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmc2002ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 41)
)
pmc2002ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapClientNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmc2002ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 42)
)
pmc2002ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapClientNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc2002ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 43)
)
pmc2002ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapClientNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmc2002ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 44)
)
pmc2002ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmClientFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002AlmClientHwFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapClientNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002ClientTrapCritGoesOn.setStatus(
        "current"
    )

pmc2002ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 45)
)
pmc2002ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmClientFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002AlmClientHwFailPortn"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapClientNumber"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002ClientTrapCritGoesOff.setStatus(
        "current"
    )

pmc2002PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 50)
)
pmc2002PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmDefFuseB"),
        ("EKINOPS-PMC2002-MIB", "pmc2002AlmDefFuseA"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc2002PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 52, 11, 51)
)
pmc2002PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC2002-MIB", "pmc2002AlmDefFuseB"),
        ("EKINOPS-PMC2002-MIB", "pmc2002AlmDefFuseA"),
        ("EKINOPS-PMC2002-MIB", "pmc2002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc2002PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PMC2002-MIB",
    **{"Pmc2002OtxMode": Pmc2002OtxMode,
       "Pmc2002OtxGrid": Pmc2002OtxGrid,
       "Pmc2002AdjustValue": Pmc2002AdjustValue,
       "Pmc2002OtxChannel": Pmc2002OtxChannel,
       "Pmc2002DccMode": Pmc2002DccMode,
       "Pmc2002Mode": Pmc2002Mode,
       "modulepmc2002": modulepmc2002,
       "pmc2002alarms": pmc2002alarms,
       "pmc2002AlmOther": pmc2002AlmOther,
       "pmc2002AlmOtherNurg": pmc2002AlmOtherNurg,
       "pmc2002AlmsynthAlm2": pmc2002AlmsynthAlm2,
       "pmc2002AlmConfTableSave": pmc2002AlmConfTableSave,
       "pmc2002AlmInvUpload": pmc2002AlmInvUpload,
       "pmc2002AlmConfTableLoad": pmc2002AlmConfTableLoad,
       "pmc2002AlmCorrelatOff": pmc2002AlmCorrelatOff,
       "pmc2002AlmMaintenanceOn": pmc2002AlmMaintenanceOn,
       "pmc2002AlmOtherUrg": pmc2002AlmOtherUrg,
       "pmc2002AlmmodInitFailLevel2": pmc2002AlmmodInitFailLevel2,
       "pmc2002AlmLedFail": pmc2002AlmLedFail,
       "pmc2002AlmNextColdBootForced": pmc2002AlmNextColdBootForced,
       "pmc2002AlmBootUndone": pmc2002AlmBootUndone,
       "pmc2002AlmResetHwInitFail": pmc2002AlmResetHwInitFail,
       "pmc2002AlmSwInitFail": pmc2002AlmSwInitFail,
       "pmc2002AlmmodInitFailLevel3": pmc2002AlmmodInitFailLevel3,
       "pmc2002AlmGwIdentFail": pmc2002AlmGwIdentFail,
       "pmc2002AlmObmTypeReadFail": pmc2002AlmObmTypeReadFail,
       "pmc2002AlmInitModuleFail": pmc2002AlmInitModuleFail,
       "pmc2002AlmXfp1InitFail": pmc2002AlmXfp1InitFail,
       "pmc2002AlmXfp2InitFail": pmc2002AlmXfp2InitFail,
       "pmc2002AlmLine1InitFail": pmc2002AlmLine1InitFail,
       "pmc2002AlmClient1InitFail": pmc2002AlmClient1InitFail,
       "pmc2002AlmOtherCrit": pmc2002AlmOtherCrit,
       "pmc2002AlmsynthAlm0": pmc2002AlmsynthAlm0,
       "pmc2002AlmLineFailSynth": pmc2002AlmLineFailSynth,
       "pmc2002AlmLineLosSynth": pmc2002AlmLineLosSynth,
       "pmc2002AlmModGlobFail": pmc2002AlmModGlobFail,
       "pmc2002AlmDefFuseA": pmc2002AlmDefFuseA,
       "pmc2002AlmDefFuseB": pmc2002AlmDefFuseB,
       "pmc2002AlmClient": pmc2002AlmClient,
       "pmc2002AlmClientNurg": pmc2002AlmClientNurg,
       "pmc2002AlmclientXfpWarningsTable": pmc2002AlmclientXfpWarningsTable,
       "pmc2002AlmclientXfpWarningsEntry": pmc2002AlmclientXfpWarningsEntry,
       "pmc2002AlmclientXfpWarningsIndex": pmc2002AlmclientXfpWarningsIndex,
       "pmc2002AlmClientTxPowerLowWarningPortn": pmc2002AlmClientTxPowerLowWarningPortn,
       "pmc2002AlmClientTxPowerHighWarningPortn": pmc2002AlmClientTxPowerHighWarningPortn,
       "pmc2002AlmClientTxBiasLowWarningPortn": pmc2002AlmClientTxBiasLowWarningPortn,
       "pmc2002AlmClientTxBiasHighWarningPortn": pmc2002AlmClientTxBiasHighWarningPortn,
       "pmc2002AlmClientTempLowWarningPortn": pmc2002AlmClientTempLowWarningPortn,
       "pmc2002AlmClientTempHighWarningPortn": pmc2002AlmClientTempHighWarningPortn,
       "pmc2002AlmClientRxPowerLowWarningPortn": pmc2002AlmClientRxPowerLowWarningPortn,
       "pmc2002AlmClientRxPowerHighWarningPortn": pmc2002AlmClientRxPowerHighWarningPortn,
       "pmc2002AlmClientUrg": pmc2002AlmClientUrg,
       "pmc2002AlmclientXfpAlarm1Table": pmc2002AlmclientXfpAlarm1Table,
       "pmc2002AlmclientXfpAlarm1Entry": pmc2002AlmclientXfpAlarm1Entry,
       "pmc2002AlmclientXfpAlarm1Index": pmc2002AlmclientXfpAlarm1Index,
       "pmc2002AlmClientTxPowerLowAlarmPortn": pmc2002AlmClientTxPowerLowAlarmPortn,
       "pmc2002AlmClientTxPowerHighAlarmPortn": pmc2002AlmClientTxPowerHighAlarmPortn,
       "pmc2002AlmClientTxBiasLowAlarmPortn": pmc2002AlmClientTxBiasLowAlarmPortn,
       "pmc2002AlmClientTxBiasHighAlarmPortn": pmc2002AlmClientTxBiasHighAlarmPortn,
       "pmc2002AlmClientTempLowAlarmPortn": pmc2002AlmClientTempLowAlarmPortn,
       "pmc2002AlmClientTempHighAlarmPortn": pmc2002AlmClientTempHighAlarmPortn,
       "pmc2002AlmClientRxPowerLowAlarmPortn": pmc2002AlmClientRxPowerLowAlarmPortn,
       "pmc2002AlmClientRxPowerHighAlarmPortn": pmc2002AlmClientRxPowerHighAlarmPortn,
       "pmc2002AlmclientXfpSupplyAlarmTable": pmc2002AlmclientXfpSupplyAlarmTable,
       "pmc2002AlmclientXfpSupplyAlarmEntry": pmc2002AlmclientXfpSupplyAlarmEntry,
       "pmc2002AlmclientXfpSupplyAlarmIndex": pmc2002AlmclientXfpSupplyAlarmIndex,
       "pmc2002AlmClientVee5LowAlarmPortn": pmc2002AlmClientVee5LowAlarmPortn,
       "pmc2002AlmClientVee5HighAlarmPortn": pmc2002AlmClientVee5HighAlarmPortn,
       "pmc2002AlmClientVcc2LowAlarmPortn": pmc2002AlmClientVcc2LowAlarmPortn,
       "pmc2002AlmClientVcc2HighAlarmPortn": pmc2002AlmClientVcc2HighAlarmPortn,
       "pmc2002AlmClientVcc3LowAlarmPortn": pmc2002AlmClientVcc3LowAlarmPortn,
       "pmc2002AlmClientVcc3HighAlarmPortn": pmc2002AlmClientVcc3HighAlarmPortn,
       "pmc2002AlmClientVcc5LowAlarmPortn": pmc2002AlmClientVcc5LowAlarmPortn,
       "pmc2002AlmClientVcc5HighAlarmPortn": pmc2002AlmClientVcc5HighAlarmPortn,
       "pmc2002AlmClientVee5LowWarningPortn": pmc2002AlmClientVee5LowWarningPortn,
       "pmc2002AlmClientVee5HighWarningPortn": pmc2002AlmClientVee5HighWarningPortn,
       "pmc2002AlmClientVcc2LowWarningPortn": pmc2002AlmClientVcc2LowWarningPortn,
       "pmc2002AlmClientVcc2HighWarningPortn": pmc2002AlmClientVcc2HighWarningPortn,
       "pmc2002AlmClientVcc3LowWarningPortn": pmc2002AlmClientVcc3LowWarningPortn,
       "pmc2002AlmClientVcc3HighWarningPortn": pmc2002AlmClientVcc3HighWarningPortn,
       "pmc2002AlmClientVcc5LowWarningPortn": pmc2002AlmClientVcc5LowWarningPortn,
       "pmc2002AlmClientVcc5HighWarningPortn": pmc2002AlmClientVcc5HighWarningPortn,
       "pmc2002AlmClientCrit": pmc2002AlmClientCrit,
       "pmc2002AlmsynthAlmPortTable": pmc2002AlmsynthAlmPortTable,
       "pmc2002AlmsynthAlmPortEntry": pmc2002AlmsynthAlmPortEntry,
       "pmc2002AlmsynthAlmPortIndex": pmc2002AlmsynthAlmPortIndex,
       "pmc2002AlmClientSfpAbsentPortn": pmc2002AlmClientSfpAbsentPortn,
       "pmc2002AlmClientDdmAbsentPortn": pmc2002AlmClientDdmAbsentPortn,
       "pmc2002AlmClientHwFailPortn": pmc2002AlmClientHwFailPortn,
       "pmc2002AlmClientDwLsdPortn": pmc2002AlmClientDwLsdPortn,
       "pmc2002AlmClientLocalOosPortn": pmc2002AlmClientLocalOosPortn,
       "pmc2002AlmClientDwCaisPortn": pmc2002AlmClientDwCaisPortn,
       "pmc2002AlmClientSfpDdmWarningPortn": pmc2002AlmClientSfpDdmWarningPortn,
       "pmc2002AlmClientSfpDdmAlmPortn": pmc2002AlmClientSfpDdmAlmPortn,
       "pmc2002AlmClientFailPortn": pmc2002AlmClientFailPortn,
       "pmc2002AlmClientUpCsfPortn": pmc2002AlmClientUpCsfPortn,
       "pmc2002AlmclientAccessioAlmTable": pmc2002AlmclientAccessioAlmTable,
       "pmc2002AlmclientAccessioAlmEntry": pmc2002AlmclientAccessioAlmEntry,
       "pmc2002AlmclientAccessioAlmIndex": pmc2002AlmclientAccessioAlmIndex,
       "pmc2002AlmClientDwLasFailPortn": pmc2002AlmClientDwLasFailPortn,
       "pmc2002AlmClientUpLosPortn": pmc2002AlmClientUpLosPortn,
       "pmc2002AlmclientXfpAlarm2Table": pmc2002AlmclientXfpAlarm2Table,
       "pmc2002AlmclientXfpAlarm2Entry": pmc2002AlmclientXfpAlarm2Entry,
       "pmc2002AlmclientXfpAlarm2Index": pmc2002AlmclientXfpAlarm2Index,
       "pmc2002AlmClientModNrPortn": pmc2002AlmClientModNrPortn,
       "pmc2002AlmClientRxCdrNotLockedPortn": pmc2002AlmClientRxCdrNotLockedPortn,
       "pmc2002AlmClientRxNrPortn": pmc2002AlmClientRxNrPortn,
       "pmc2002AlmClientTxCdrNotLockedPortn": pmc2002AlmClientTxCdrNotLockedPortn,
       "pmc2002AlmClientTxFaultPortn": pmc2002AlmClientTxFaultPortn,
       "pmc2002AlmClientTxNrPortn": pmc2002AlmClientTxNrPortn,
       "pmc2002AlmClientWavelengthUnlockedPortn": pmc2002AlmClientWavelengthUnlockedPortn,
       "pmc2002AlmClientTecFaultPortn": pmc2002AlmClientTecFaultPortn,
       "pmc2002AlmClientApdSupplyFaultPortn": pmc2002AlmClientApdSupplyFaultPortn,
       "pmc2002AlmclientMapperDeAlmTable": pmc2002AlmclientMapperDeAlmTable,
       "pmc2002AlmclientMapperDeAlmEntry": pmc2002AlmclientMapperDeAlmEntry,
       "pmc2002AlmclientMapperDeAlmIndex": pmc2002AlmclientMapperDeAlmIndex,
       "pmc2002AlmClientUpAccOosPortn": pmc2002AlmClientUpAccOosPortn,
       "pmc2002AlmClientUpBufferOvlPortn": pmc2002AlmClientUpBufferOvlPortn,
       "pmc2002AlmClientDwCsfDetPortn": pmc2002AlmClientDwCsfDetPortn,
       "pmc2002AlmClientDwBufferOvlPortn": pmc2002AlmClientDwBufferOvlPortn,
       "pmc2002AlmLine": pmc2002AlmLine,
       "pmc2002AlmLineNurg": pmc2002AlmLineNurg,
       "pmc2002AlmlineXfp1WarningsTable": pmc2002AlmlineXfp1WarningsTable,
       "pmc2002AlmlineXfp1WarningsEntry": pmc2002AlmlineXfp1WarningsEntry,
       "pmc2002AlmlineXfp1WarningsIndex": pmc2002AlmlineXfp1WarningsIndex,
       "pmc2002AlmLineTxPowerLowWarningPortn": pmc2002AlmLineTxPowerLowWarningPortn,
       "pmc2002AlmLineTxPowerHighWarningPortn": pmc2002AlmLineTxPowerHighWarningPortn,
       "pmc2002AlmLineTxBiasLowWarningPortn": pmc2002AlmLineTxBiasLowWarningPortn,
       "pmc2002AlmLineTxBiasHighWarningPortn": pmc2002AlmLineTxBiasHighWarningPortn,
       "pmc2002AlmLineTempLowWarningPortn": pmc2002AlmLineTempLowWarningPortn,
       "pmc2002AlmLineTempHighWarningPortn": pmc2002AlmLineTempHighWarningPortn,
       "pmc2002AlmLineRxPowerLowWarningPortn": pmc2002AlmLineRxPowerLowWarningPortn,
       "pmc2002AlmLineRxPowerHighWarningPortn": pmc2002AlmLineRxPowerHighWarningPortn,
       "pmc2002AlmlineOtx1TlhWarningsTable": pmc2002AlmlineOtx1TlhWarningsTable,
       "pmc2002AlmlineOtx1TlhWarningsEntry": pmc2002AlmlineOtx1TlhWarningsEntry,
       "pmc2002AlmlineOtx1TlhWarningsIndex": pmc2002AlmlineOtx1TlhWarningsIndex,
       "pmc2002AlmLineModulatorAgingHighWarningPortn": pmc2002AlmLineModulatorAgingHighWarningPortn,
       "pmc2002AlmLineAgingHighWarningPortn": pmc2002AlmLineAgingHighWarningPortn,
       "pmc2002AlmLineFreqDevHighWarningPortn": pmc2002AlmLineFreqDevHighWarningPortn,
       "pmc2002AlmLineLaserTempHighWarningPortn": pmc2002AlmLineLaserTempHighWarningPortn,
       "pmc2002AlmLineUrg": pmc2002AlmLineUrg,
       "pmc2002AlmdfrmBerTable": pmc2002AlmdfrmBerTable,
       "pmc2002AlmdfrmBerEntry": pmc2002AlmdfrmBerEntry,
       "pmc2002AlmdfrmBerIndex": pmc2002AlmdfrmBerIndex,
       "pmc2002AlmLineSignalDegradePortn": pmc2002AlmLineSignalDegradePortn,
       "pmc2002AlmLineSignalFailPortn": pmc2002AlmLineSignalFailPortn,
       "pmc2002AlmLineDegradePortn": pmc2002AlmLineDegradePortn,
       "pmc2002AlmlineXfp1AlarmTable": pmc2002AlmlineXfp1AlarmTable,
       "pmc2002AlmlineXfp1AlarmEntry": pmc2002AlmlineXfp1AlarmEntry,
       "pmc2002AlmlineXfp1AlarmIndex": pmc2002AlmlineXfp1AlarmIndex,
       "pmc2002AlmLineTxPowerLowAlarmPortn": pmc2002AlmLineTxPowerLowAlarmPortn,
       "pmc2002AlmLineTxPowerHighAlarmPortn": pmc2002AlmLineTxPowerHighAlarmPortn,
       "pmc2002AlmLineTxBiasLowAlarmPortn": pmc2002AlmLineTxBiasLowAlarmPortn,
       "pmc2002AlmLineTxBiasHighAlarmPortn": pmc2002AlmLineTxBiasHighAlarmPortn,
       "pmc2002AlmLineTempLowAlarmPortn": pmc2002AlmLineTempLowAlarmPortn,
       "pmc2002AlmLineTempHighAlarmPortn": pmc2002AlmLineTempHighAlarmPortn,
       "pmc2002AlmLineRxPowerLowAlarmPortn": pmc2002AlmLineRxPowerLowAlarmPortn,
       "pmc2002AlmLineRxPowerHighAlarmPortn": pmc2002AlmLineRxPowerHighAlarmPortn,
       "pmc2002AlmlineXfp1SupplyAlarmTable": pmc2002AlmlineXfp1SupplyAlarmTable,
       "pmc2002AlmlineXfp1SupplyAlarmEntry": pmc2002AlmlineXfp1SupplyAlarmEntry,
       "pmc2002AlmlineXfp1SupplyAlarmIndex": pmc2002AlmlineXfp1SupplyAlarmIndex,
       "pmc2002AlmLineVee5LowAlarmPortn": pmc2002AlmLineVee5LowAlarmPortn,
       "pmc2002AlmLineVee5HighAlarmPortn": pmc2002AlmLineVee5HighAlarmPortn,
       "pmc2002AlmLineVcc2LowAlarmPortn": pmc2002AlmLineVcc2LowAlarmPortn,
       "pmc2002AlmLineVcc2HighAlarmPortn": pmc2002AlmLineVcc2HighAlarmPortn,
       "pmc2002AlmLineVcc3LowAlarmPortn": pmc2002AlmLineVcc3LowAlarmPortn,
       "pmc2002AlmLineVcc3HighAlarmPortn": pmc2002AlmLineVcc3HighAlarmPortn,
       "pmc2002AlmLineVcc5LowAlarmPortn": pmc2002AlmLineVcc5LowAlarmPortn,
       "pmc2002AlmLineVcc5HighAlarmPortn": pmc2002AlmLineVcc5HighAlarmPortn,
       "pmc2002AlmLineVee5LowLineWarningPortn": pmc2002AlmLineVee5LowLineWarningPortn,
       "pmc2002AlmLineVee5HighWarningPortn": pmc2002AlmLineVee5HighWarningPortn,
       "pmc2002AlmLineVcc2LowWarningPortn": pmc2002AlmLineVcc2LowWarningPortn,
       "pmc2002AlmLineVcc2HighWarningPortn": pmc2002AlmLineVcc2HighWarningPortn,
       "pmc2002AlmLineVcc3LowWarningPortn": pmc2002AlmLineVcc3LowWarningPortn,
       "pmc2002AlmLineVcc3HighWarningPortn": pmc2002AlmLineVcc3HighWarningPortn,
       "pmc2002AlmLineVcc5LowWarningPortn": pmc2002AlmLineVcc5LowWarningPortn,
       "pmc2002AlmLineVcc5HighWarningPortn": pmc2002AlmLineVcc5HighWarningPortn,
       "pmc2002AlmlineOtx1TlhAlarmsTable": pmc2002AlmlineOtx1TlhAlarmsTable,
       "pmc2002AlmlineOtx1TlhAlarmsEntry": pmc2002AlmlineOtx1TlhAlarmsEntry,
       "pmc2002AlmlineOtx1TlhAlarmsIndex": pmc2002AlmlineOtx1TlhAlarmsIndex,
       "pmc2002AlmLineModulatorAgingHighAlaPortn": pmc2002AlmLineModulatorAgingHighAlaPortn,
       "pmc2002AlmLineAgingHighAlaPortn": pmc2002AlmLineAgingHighAlaPortn,
       "pmc2002AlmLineCdrNotReadyPortn": pmc2002AlmLineCdrNotReadyPortn,
       "pmc2002AlmLineFreqDevHighAlaPortn": pmc2002AlmLineFreqDevHighAlaPortn,
       "pmc2002AlmLineLaserTempHighAlaPortn": pmc2002AlmLineLaserTempHighAlaPortn,
       "pmc2002AlmLineCrit": pmc2002AlmLineCrit,
       "pmc2002AlmsynthAlmLineTable": pmc2002AlmsynthAlmLineTable,
       "pmc2002AlmsynthAlmLineEntry": pmc2002AlmsynthAlmLineEntry,
       "pmc2002AlmsynthAlmLineIndex": pmc2002AlmsynthAlmLineIndex,
       "pmc2002AlmLineXfpAbsentPortn": pmc2002AlmLineXfpAbsentPortn,
       "pmc2002AlmLineXfpInitNotComplPortn": pmc2002AlmLineXfpInitNotComplPortn,
       "pmc2002AlmLineHwFailPortn": pmc2002AlmLineHwFailPortn,
       "pmc2002AlmLineXfpTxOffPortn": pmc2002AlmLineXfpTxOffPortn,
       "pmc2002AlmLineLocalOosPortn": pmc2002AlmLineLocalOosPortn,
       "pmc2002AlmLineUpRdiInsPortn": pmc2002AlmLineUpRdiInsPortn,
       "pmc2002AlmLineDdmWarningPortn": pmc2002AlmLineDdmWarningPortn,
       "pmc2002AlmLineDdmAlmPortn": pmc2002AlmLineDdmAlmPortn,
       "pmc2002AlmLineFailPortn": pmc2002AlmLineFailPortn,
       "pmc2002AlmdfrmAlmTable": pmc2002AlmdfrmAlmTable,
       "pmc2002AlmdfrmAlmEntry": pmc2002AlmdfrmAlmEntry,
       "pmc2002AlmdfrmAlmIndex": pmc2002AlmdfrmAlmIndex,
       "pmc2002AlmLineDwAisDetPortn": pmc2002AlmLineDwAisDetPortn,
       "pmc2002AlmLineDwRdiDetPortn": pmc2002AlmLineDwRdiDetPortn,
       "pmc2002AlmLineDwOofPortn": pmc2002AlmLineDwOofPortn,
       "pmc2002AlmLineDwLofPortn": pmc2002AlmLineDwLofPortn,
       "pmc2002AlmLineFecFailPortn": pmc2002AlmLineFecFailPortn,
       "pmc2002AlmlineSyncAlarmsTable": pmc2002AlmlineSyncAlarmsTable,
       "pmc2002AlmlineSyncAlarmsEntry": pmc2002AlmlineSyncAlarmsEntry,
       "pmc2002AlmlineSyncAlarmsIndex": pmc2002AlmlineSyncAlarmsIndex,
       "pmc2002AlmLineDwLockerrPortn": pmc2002AlmLineDwLockerrPortn,
       "pmc2002AlmLineUpLockerrPortn": pmc2002AlmLineUpLockerrPortn,
       "pmc2002AlmLineDwLosPortn": pmc2002AlmLineDwLosPortn,
       "pmc2002AlmlineXfp1AlarmsTable": pmc2002AlmlineXfp1AlarmsTable,
       "pmc2002AlmlineXfp1AlarmsEntry": pmc2002AlmlineXfp1AlarmsEntry,
       "pmc2002AlmlineXfp1AlarmsIndex": pmc2002AlmlineXfp1AlarmsIndex,
       "pmc2002AlmLineModNrPortn": pmc2002AlmLineModNrPortn,
       "pmc2002AlmLineRxCdrNotLockedPortn": pmc2002AlmLineRxCdrNotLockedPortn,
       "pmc2002AlmLineRxNrPortn": pmc2002AlmLineRxNrPortn,
       "pmc2002AlmLineTxCdrNotLockedPortn": pmc2002AlmLineTxCdrNotLockedPortn,
       "pmc2002AlmLineTxFaultPortn": pmc2002AlmLineTxFaultPortn,
       "pmc2002AlmLineTxNrPortn": pmc2002AlmLineTxNrPortn,
       "pmc2002AlmLineWavelengthUnlockedPortn": pmc2002AlmLineWavelengthUnlockedPortn,
       "pmc2002AlmLineTecFaultPortn": pmc2002AlmLineTecFaultPortn,
       "pmc2002AlmLineApdSupplyFaultPortn": pmc2002AlmLineApdSupplyFaultPortn,
       "pmc2002measures": pmc2002measures,
       "pmc2002MesrOther": pmc2002MesrOther,
       "pmc2002Mesrsynth0": pmc2002Mesrsynth0,
       "pmc2002Mesrsynth1": pmc2002Mesrsynth1,
       "pmc2002MesrClient": pmc2002MesrClient,
       "pmc2002MesrclientModTempMeasTable": pmc2002MesrclientModTempMeasTable,
       "pmc2002MesrclientModTempMeasEntry": pmc2002MesrclientModTempMeasEntry,
       "pmc2002MesrclientModTempMeasIndex": pmc2002MesrclientModTempMeasIndex,
       "pmc2002MesrclientModTempMeasPortn": pmc2002MesrclientModTempMeasPortn,
       "pmc2002MesrclientBiasCurrentMeasTable": pmc2002MesrclientBiasCurrentMeasTable,
       "pmc2002MesrclientBiasCurrentMeasEntry": pmc2002MesrclientBiasCurrentMeasEntry,
       "pmc2002MesrclientBiasCurrentMeasIndex": pmc2002MesrclientBiasCurrentMeasIndex,
       "pmc2002MesrclientBiasCurrentMeasPortn": pmc2002MesrclientBiasCurrentMeasPortn,
       "pmc2002MesrclientTxPowerMeasTable": pmc2002MesrclientTxPowerMeasTable,
       "pmc2002MesrclientTxPowerMeasEntry": pmc2002MesrclientTxPowerMeasEntry,
       "pmc2002MesrclientTxPowerMeasIndex": pmc2002MesrclientTxPowerMeasIndex,
       "pmc2002MesrclientTxPowerMeasPortn": pmc2002MesrclientTxPowerMeasPortn,
       "pmc2002MesrclientRxPowerMeasTable": pmc2002MesrclientRxPowerMeasTable,
       "pmc2002MesrclientRxPowerMeasEntry": pmc2002MesrclientRxPowerMeasEntry,
       "pmc2002MesrclientRxPowerMeasIndex": pmc2002MesrclientRxPowerMeasIndex,
       "pmc2002MesrclientRxPowerMeasPortn": pmc2002MesrclientRxPowerMeasPortn,
       "pmc2002MesrLine": pmc2002MesrLine,
       "pmc2002Mesrline1ModTempMeasTable": pmc2002Mesrline1ModTempMeasTable,
       "pmc2002Mesrline1ModTempMeasEntry": pmc2002Mesrline1ModTempMeasEntry,
       "pmc2002Mesrline1ModTempMeasIndex": pmc2002Mesrline1ModTempMeasIndex,
       "pmc2002Mesrline1ModTempMeasPortn": pmc2002Mesrline1ModTempMeasPortn,
       "pmc2002Mesrline1ReservedTable": pmc2002Mesrline1ReservedTable,
       "pmc2002Mesrline1ReservedEntry": pmc2002Mesrline1ReservedEntry,
       "pmc2002Mesrline1ReservedIndex": pmc2002Mesrline1ReservedIndex,
       "pmc2002Mesrline1ReservedPortn": pmc2002Mesrline1ReservedPortn,
       "pmc2002Mesrline1BiasCurrentMeasTable": pmc2002Mesrline1BiasCurrentMeasTable,
       "pmc2002Mesrline1BiasCurrentMeasEntry": pmc2002Mesrline1BiasCurrentMeasEntry,
       "pmc2002Mesrline1BiasCurrentMeasIndex": pmc2002Mesrline1BiasCurrentMeasIndex,
       "pmc2002Mesrline1BiasCurrentMeasPortn": pmc2002Mesrline1BiasCurrentMeasPortn,
       "pmc2002Mesrline1TxPowerMeasTable": pmc2002Mesrline1TxPowerMeasTable,
       "pmc2002Mesrline1TxPowerMeasEntry": pmc2002Mesrline1TxPowerMeasEntry,
       "pmc2002Mesrline1TxPowerMeasIndex": pmc2002Mesrline1TxPowerMeasIndex,
       "pmc2002Mesrline1TxPowerMeasPortn": pmc2002Mesrline1TxPowerMeasPortn,
       "pmc2002Mesrline1RxPowerMeasTable": pmc2002Mesrline1RxPowerMeasTable,
       "pmc2002Mesrline1RxPowerMeasEntry": pmc2002Mesrline1RxPowerMeasEntry,
       "pmc2002Mesrline1RxPowerMeasIndex": pmc2002Mesrline1RxPowerMeasIndex,
       "pmc2002Mesrline1RxPowerMeasPortn": pmc2002Mesrline1RxPowerMeasPortn,
       "pmc2002Mesrline1Aux1MeasTable": pmc2002Mesrline1Aux1MeasTable,
       "pmc2002Mesrline1Aux1MeasEntry": pmc2002Mesrline1Aux1MeasEntry,
       "pmc2002Mesrline1Aux1MeasIndex": pmc2002Mesrline1Aux1MeasIndex,
       "pmc2002Mesrline1Aux1MeasPortn": pmc2002Mesrline1Aux1MeasPortn,
       "pmc2002Mesrline1Aux2MeasTable": pmc2002Mesrline1Aux2MeasTable,
       "pmc2002Mesrline1Aux2MeasEntry": pmc2002Mesrline1Aux2MeasEntry,
       "pmc2002Mesrline1Aux2MeasIndex": pmc2002Mesrline1Aux2MeasIndex,
       "pmc2002Mesrline1Aux2MeasPortn": pmc2002Mesrline1Aux2MeasPortn,
       "pmc2002Mesrline1AgingTable": pmc2002Mesrline1AgingTable,
       "pmc2002Mesrline1AgingEntry": pmc2002Mesrline1AgingEntry,
       "pmc2002Mesrline1AgingIndex": pmc2002Mesrline1AgingIndex,
       "pmc2002Mesrline1AgingPortn": pmc2002Mesrline1AgingPortn,
       "pmc2002Mesrline1LaserTemperatureTable": pmc2002Mesrline1LaserTemperatureTable,
       "pmc2002Mesrline1LaserTemperatureEntry": pmc2002Mesrline1LaserTemperatureEntry,
       "pmc2002Mesrline1LaserTemperatureIndex": pmc2002Mesrline1LaserTemperatureIndex,
       "pmc2002Mesrline1LaserTemperaturePortn": pmc2002Mesrline1LaserTemperaturePortn,
       "pmc2002Mesrline1FreqDeviationTable": pmc2002Mesrline1FreqDeviationTable,
       "pmc2002Mesrline1FreqDeviationEntry": pmc2002Mesrline1FreqDeviationEntry,
       "pmc2002Mesrline1FreqDeviationIndex": pmc2002Mesrline1FreqDeviationIndex,
       "pmc2002Mesrline1FreqDeviationPortn": pmc2002Mesrline1FreqDeviationPortn,
       "pmc2002Mesrline1LaserWvlengthTable": pmc2002Mesrline1LaserWvlengthTable,
       "pmc2002Mesrline1LaserWvlengthEntry": pmc2002Mesrline1LaserWvlengthEntry,
       "pmc2002Mesrline1LaserWvlengthIndex": pmc2002Mesrline1LaserWvlengthIndex,
       "pmc2002Mesrline1LaserWvlengthPortn": pmc2002Mesrline1LaserWvlengthPortn,
       "pmc2002counters": pmc2002counters,
       "pmc2002CntOther": pmc2002CntOther,
       "pmc2002CntClient": pmc2002CntClient,
       "pmc2002CntclientUpErrCntTable": pmc2002CntclientUpErrCntTable,
       "pmc2002CntclientUpErrCntEntry": pmc2002CntclientUpErrCntEntry,
       "pmc2002CntclientUpErrCntIndex": pmc2002CntclientUpErrCntIndex,
       "pmc2002CntclientUpErrCntValuePortn": pmc2002CntclientUpErrCntValuePortn,
       "pmc2002CntclientUpErrCntErrorPortn": pmc2002CntclientUpErrCntErrorPortn,
       "pmc2002CntclientUpErrCntOverloadPortn": pmc2002CntclientUpErrCntOverloadPortn,
       "pmc2002CntclientUpTimCntTable": pmc2002CntclientUpTimCntTable,
       "pmc2002CntclientUpTimCntEntry": pmc2002CntclientUpTimCntEntry,
       "pmc2002CntclientUpTimCntIndex": pmc2002CntclientUpTimCntIndex,
       "pmc2002CntclientUpTimCntValuePortn": pmc2002CntclientUpTimCntValuePortn,
       "pmc2002CntclientUpTimCntErrorPortn": pmc2002CntclientUpTimCntErrorPortn,
       "pmc2002CntclientUpTimCntOverloadPortn": pmc2002CntclientUpTimCntOverloadPortn,
       "pmc2002CntclientDwErrCntTable": pmc2002CntclientDwErrCntTable,
       "pmc2002CntclientDwErrCntEntry": pmc2002CntclientDwErrCntEntry,
       "pmc2002CntclientDwErrCntIndex": pmc2002CntclientDwErrCntIndex,
       "pmc2002CntclientDwErrCntValuePortn": pmc2002CntclientDwErrCntValuePortn,
       "pmc2002CntclientDwErrCntErrorPortn": pmc2002CntclientDwErrCntErrorPortn,
       "pmc2002CntclientDwErrCntOverloadPortn": pmc2002CntclientDwErrCntOverloadPortn,
       "pmc2002CntclientDwTimCntTable": pmc2002CntclientDwTimCntTable,
       "pmc2002CntclientDwTimCntEntry": pmc2002CntclientDwTimCntEntry,
       "pmc2002CntclientDwTimCntIndex": pmc2002CntclientDwTimCntIndex,
       "pmc2002CntclientDwTimCntValuePortn": pmc2002CntclientDwTimCntValuePortn,
       "pmc2002CntclientDwTimCntErrorPortn": pmc2002CntclientDwTimCntErrorPortn,
       "pmc2002CntclientDwTimCntOverloadPortn": pmc2002CntclientDwTimCntOverloadPortn,
       "pmc2002CntLine": pmc2002CntLine,
       "pmc2002CntlineDfrmErrCntTable": pmc2002CntlineDfrmErrCntTable,
       "pmc2002CntlineDfrmErrCntEntry": pmc2002CntlineDfrmErrCntEntry,
       "pmc2002CntlineDfrmErrCntIndex": pmc2002CntlineDfrmErrCntIndex,
       "pmc2002CntlineDfrmErrCntValuePortn": pmc2002CntlineDfrmErrCntValuePortn,
       "pmc2002CntlineDfrmErrCntErrorPortn": pmc2002CntlineDfrmErrCntErrorPortn,
       "pmc2002CntlineDfrmErrCntOverloadPortn": pmc2002CntlineDfrmErrCntOverloadPortn,
       "pmc2002CntlineDfrmTimCntTable": pmc2002CntlineDfrmTimCntTable,
       "pmc2002CntlineDfrmTimCntEntry": pmc2002CntlineDfrmTimCntEntry,
       "pmc2002CntlineDfrmTimCntIndex": pmc2002CntlineDfrmTimCntIndex,
       "pmc2002CntlineDfrmTimCntValuePortn": pmc2002CntlineDfrmTimCntValuePortn,
       "pmc2002CntlineDfrmTimCntErrorPortn": pmc2002CntlineDfrmTimCntErrorPortn,
       "pmc2002CntlineDfrmTimCntOverloadPortn": pmc2002CntlineDfrmTimCntOverloadPortn,
       "pmc2002CntlineDfrmPrimErrCntTable": pmc2002CntlineDfrmPrimErrCntTable,
       "pmc2002CntlineDfrmPrimErrCntEntry": pmc2002CntlineDfrmPrimErrCntEntry,
       "pmc2002CntlineDfrmPrimErrCntIndex": pmc2002CntlineDfrmPrimErrCntIndex,
       "pmc2002CntlineDfrmPrimErrCntValuePortn": pmc2002CntlineDfrmPrimErrCntValuePortn,
       "pmc2002CntlineDfrmPrimErrCntErrorPortn": pmc2002CntlineDfrmPrimErrCntErrorPortn,
       "pmc2002CntlineDfrmPrimErrCntOverloadPortn": pmc2002CntlineDfrmPrimErrCntOverloadPortn,
       "pmc2002CntCountersReset": pmc2002CntCountersReset,
       "pmc2002CntCountersStop": pmc2002CntCountersStop,
       "pmc2002controlsWrite": pmc2002controlsWrite,
       "pmc2002CtrlOther": pmc2002CtrlOther,
       "pmc2002CtrlconfMgnt1": pmc2002CtrlconfMgnt1,
       "pmc2002CtrlConf1Load1": pmc2002CtrlConf1Load1,
       "pmc2002CtrlConf2Load1": pmc2002CtrlConf2Load1,
       "pmc2002CtrlConf2Flash1": pmc2002CtrlConf2Flash1,
       "pmc2002CtrlConf2Clear1": pmc2002CtrlConf2Clear1,
       "pmc2002Ctrlsynth4": pmc2002Ctrlsynth4,
       "pmc2002CtrlCorrelatOn": pmc2002CtrlCorrelatOn,
       "pmc2002CtrlCorrelatOff": pmc2002CtrlCorrelatOff,
       "pmc2002CtrlswMgnt": pmc2002CtrlswMgnt,
       "pmc2002CtrlColdReset": pmc2002CtrlColdReset,
       "pmc2002CtrlWarmReset": pmc2002CtrlWarmReset,
       "pmc2002CtrlLoadSwBank1": pmc2002CtrlLoadSwBank1,
       "pmc2002CtrlLoadSwBank2": pmc2002CtrlLoadSwBank2,
       "pmc2002CtrlgwMgnt": pmc2002CtrlgwMgnt,
       "pmc2002CtrlCurrentGwReset": pmc2002CtrlCurrentGwReset,
       "pmc2002CtrlLoadGwBank1": pmc2002CtrlLoadGwBank1,
       "pmc2002CtrlLoadGwBank2": pmc2002CtrlLoadGwBank2,
       "pmc2002CtrlLoadGwBank3": pmc2002CtrlLoadGwBank3,
       "pmc2002CtrlLoadGwBank4": pmc2002CtrlLoadGwBank4,
       "pmc2002CtrlledTest": pmc2002CtrlledTest,
       "pmc2002CtrlGreenLed": pmc2002CtrlGreenLed,
       "pmc2002CtrlRedLed": pmc2002CtrlRedLed,
       "pmc2002CtrlLedOff": pmc2002CtrlLedOff,
       "pmc2002CtrlmoduleOosMode": pmc2002CtrlmoduleOosMode,
       "pmc2002CtrlModuleOosMode": pmc2002CtrlModuleOosMode,
       "pmc2002CtrlmoduleDccMgnt": pmc2002CtrlmoduleDccMgnt,
       "pmc2002CtrlmaintenanceMode": pmc2002CtrlmaintenanceMode,
       "pmc2002CtrlMaintenanceMode": pmc2002CtrlMaintenanceMode,
       "pmc2002CtrlClient": pmc2002CtrlClient,
       "pmc2002CtrlaccessLoopTable": pmc2002CtrlaccessLoopTable,
       "pmc2002CtrlaccessLoopEntry": pmc2002CtrlaccessLoopEntry,
       "pmc2002CtrlaccessLoopIndex": pmc2002CtrlaccessLoopIndex,
       "pmc2002CtrlaccessLoopPortn": pmc2002CtrlaccessLoopPortn,
       "pmc2002CtrlportOosModeTable": pmc2002CtrlportOosModeTable,
       "pmc2002CtrlportOosModeEntry": pmc2002CtrlportOosModeEntry,
       "pmc2002CtrlportOosModeIndex": pmc2002CtrlportOosModeIndex,
       "pmc2002CtrlportOosModePortn": pmc2002CtrlportOosModePortn,
       "pmc2002CtrlsfpOffCtrlTable": pmc2002CtrlsfpOffCtrlTable,
       "pmc2002CtrlsfpOffCtrlEntry": pmc2002CtrlsfpOffCtrlEntry,
       "pmc2002CtrlsfpOffCtrlIndex": pmc2002CtrlsfpOffCtrlIndex,
       "pmc2002CtrlsfpOffCtrlPortn": pmc2002CtrlsfpOffCtrlPortn,
       "pmc2002CtrlcsfUpInsTable": pmc2002CtrlcsfUpInsTable,
       "pmc2002CtrlcsfUpInsEntry": pmc2002CtrlcsfUpInsEntry,
       "pmc2002CtrlcsfUpInsIndex": pmc2002CtrlcsfUpInsIndex,
       "pmc2002CtrlcsfUpInsPortn": pmc2002CtrlcsfUpInsPortn,
       "pmc2002CtrlcaisDwInsTable": pmc2002CtrlcaisDwInsTable,
       "pmc2002CtrlcaisDwInsEntry": pmc2002CtrlcaisDwInsEntry,
       "pmc2002CtrlcaisDwInsIndex": pmc2002CtrlcaisDwInsIndex,
       "pmc2002CtrlcaisDwInsPortn": pmc2002CtrlcaisDwInsPortn,
       "pmc2002CtrlclientAccessTermLoopTable": pmc2002CtrlclientAccessTermLoopTable,
       "pmc2002CtrlclientAccessTermLoopEntry": pmc2002CtrlclientAccessTermLoopEntry,
       "pmc2002CtrlclientAccessTermLoopIndex": pmc2002CtrlclientAccessTermLoopIndex,
       "pmc2002CtrlclientAccessTermLoopPortn": pmc2002CtrlclientAccessTermLoopPortn,
       "pmc2002CtrlprotocolTable": pmc2002CtrlprotocolTable,
       "pmc2002CtrlprotocolEntry": pmc2002CtrlprotocolEntry,
       "pmc2002CtrlprotocolIndex": pmc2002CtrlprotocolIndex,
       "pmc2002CtrlprotocolPortn": pmc2002CtrlprotocolPortn,
       "pmc2002CtrlclientResetAllCountTable": pmc2002CtrlclientResetAllCountTable,
       "pmc2002CtrlclientResetAllCountEntry": pmc2002CtrlclientResetAllCountEntry,
       "pmc2002CtrlclientResetAllCountIndex": pmc2002CtrlclientResetAllCountIndex,
       "pmc2002CtrlclientResetAllCountsPortn": pmc2002CtrlclientResetAllCountsPortn,
       "pmc2002CtrlLine": pmc2002CtrlLine,
       "pmc2002CtrlcommAccessLoopTable": pmc2002CtrlcommAccessLoopTable,
       "pmc2002CtrlcommAccessLoopEntry": pmc2002CtrlcommAccessLoopEntry,
       "pmc2002CtrlcommAccessLoopIndex": pmc2002CtrlcommAccessLoopIndex,
       "pmc2002CtrlcommAccessLoopPortn": pmc2002CtrlcommAccessLoopPortn,
       "pmc2002CtrllineLoopTable": pmc2002CtrllineLoopTable,
       "pmc2002CtrllineLoopEntry": pmc2002CtrllineLoopEntry,
       "pmc2002CtrllineLoopIndex": pmc2002CtrllineLoopIndex,
       "pmc2002CtrllineLoopPortn": pmc2002CtrllineLoopPortn,
       "pmc2002CtrlmsAisTable": pmc2002CtrlmsAisTable,
       "pmc2002CtrlmsAisEntry": pmc2002CtrlmsAisEntry,
       "pmc2002CtrlmsAisIndex": pmc2002CtrlmsAisIndex,
       "pmc2002CtrlmsAisPortn": pmc2002CtrlmsAisPortn,
       "pmc2002CtrlfecDisableTable": pmc2002CtrlfecDisableTable,
       "pmc2002CtrlfecDisableEntry": pmc2002CtrlfecDisableEntry,
       "pmc2002CtrlfecDisableIndex": pmc2002CtrlfecDisableIndex,
       "pmc2002CtrlfecDisablePortn": pmc2002CtrlfecDisablePortn,
       "pmc2002CtrllineOosModeTable": pmc2002CtrllineOosModeTable,
       "pmc2002CtrllineOosModeEntry": pmc2002CtrllineOosModeEntry,
       "pmc2002CtrllineOosModeIndex": pmc2002CtrllineOosModeIndex,
       "pmc2002CtrllineOosModePortn": pmc2002CtrllineOosModePortn,
       "pmc2002CtrlxfpOnoffTable": pmc2002CtrlxfpOnoffTable,
       "pmc2002CtrlxfpOnoffEntry": pmc2002CtrlxfpOnoffEntry,
       "pmc2002CtrlxfpOnoffIndex": pmc2002CtrlxfpOnoffIndex,
       "pmc2002CtrlxfpOnoffPortn": pmc2002CtrlxfpOnoffPortn,
       "pmc2002CtrlxfpLineLoopTable": pmc2002CtrlxfpLineLoopTable,
       "pmc2002CtrlxfpLineLoopEntry": pmc2002CtrlxfpLineLoopEntry,
       "pmc2002CtrlxfpLineLoopIndex": pmc2002CtrlxfpLineLoopIndex,
       "pmc2002CtrlxfpLineLoopPortn": pmc2002CtrlxfpLineLoopPortn,
       "pmc2002CtrlxfpLineXfiLoopTable": pmc2002CtrlxfpLineXfiLoopTable,
       "pmc2002CtrlxfpLineXfiLoopEntry": pmc2002CtrlxfpLineXfiLoopEntry,
       "pmc2002CtrlxfpLineXfiLoopIndex": pmc2002CtrlxfpLineXfiLoopIndex,
       "pmc2002CtrlxfpLineXfiLoopPortn": pmc2002CtrlxfpLineXfiLoopPortn,
       "pmc2002CtrllineTunableChannelTable": pmc2002CtrllineTunableChannelTable,
       "pmc2002CtrllineTunableChannelEntry": pmc2002CtrllineTunableChannelEntry,
       "pmc2002CtrllineTunableChannelIndex": pmc2002CtrllineTunableChannelIndex,
       "pmc2002CtrllineTunableChannelPortn": pmc2002CtrllineTunableChannelPortn,
       "pmc2002CtrllinePhotodiodeModeTable": pmc2002CtrllinePhotodiodeModeTable,
       "pmc2002CtrllinePhotodiodeModeEntry": pmc2002CtrllinePhotodiodeModeEntry,
       "pmc2002CtrllinePhotodiodeModeIndex": pmc2002CtrllinePhotodiodeModeIndex,
       "pmc2002CtrllinePhotodiodeModePortn": pmc2002CtrllinePhotodiodeModePortn,
       "pmc2002CtrllinePhotodiodeValueTable": pmc2002CtrllinePhotodiodeValueTable,
       "pmc2002CtrllinePhotodiodeValueEntry": pmc2002CtrllinePhotodiodeValueEntry,
       "pmc2002CtrllinePhotodiodeValueIndex": pmc2002CtrllinePhotodiodeValueIndex,
       "pmc2002CtrllinePhotodiodeValuePortn": pmc2002CtrllinePhotodiodeValuePortn,
       "pmc2002CtrllinePowerLaserTable": pmc2002CtrllinePowerLaserTable,
       "pmc2002CtrllinePowerLaserEntry": pmc2002CtrllinePowerLaserEntry,
       "pmc2002CtrllinePowerLaserIndex": pmc2002CtrllinePowerLaserIndex,
       "pmc2002CtrllinePowerLaserPortn": pmc2002CtrllinePowerLaserPortn,
       "pmc2002CtrlotxVlhResetTable": pmc2002CtrlotxVlhResetTable,
       "pmc2002CtrlotxVlhResetEntry": pmc2002CtrlotxVlhResetEntry,
       "pmc2002CtrlotxVlhResetIndex": pmc2002CtrlotxVlhResetIndex,
       "pmc2002CtrlotxVlhResetPortn": pmc2002CtrlotxVlhResetPortn,
       "pmc2002CtrllineLoopTransceiverTable": pmc2002CtrllineLoopTransceiverTable,
       "pmc2002CtrllineLoopTransceiverEntry": pmc2002CtrllineLoopTransceiverEntry,
       "pmc2002CtrllineLoopTransceiverIndex": pmc2002CtrllineLoopTransceiverIndex,
       "pmc2002CtrllineLoopTransceiverPortn": pmc2002CtrllineLoopTransceiverPortn,
       "pmc2002CtrllineResetAllCountTable": pmc2002CtrllineResetAllCountTable,
       "pmc2002CtrllineResetAllCountEntry": pmc2002CtrllineResetAllCountEntry,
       "pmc2002CtrllineResetAllCountIndex": pmc2002CtrllineResetAllCountIndex,
       "pmc2002CtrllineResetAllCountsPortn": pmc2002CtrllineResetAllCountsPortn,
       "pmc2002ri": pmc2002ri,
       "pmc2002riTable": pmc2002riTable,
       "pmc2002RinvClientTable": pmc2002RinvClientTable,
       "pmc2002RinvClientEntry": pmc2002RinvClientEntry,
       "pmc2002RinvClientIndex": pmc2002RinvClientIndex,
       "pmc2002RinvClient": pmc2002RinvClient,
       "pmc2002RinvLineTable": pmc2002RinvLineTable,
       "pmc2002RinvLineEntry": pmc2002RinvLineEntry,
       "pmc2002RinvLineIndex": pmc2002RinvLineIndex,
       "pmc2002RinvxfpLine": pmc2002RinvxfpLine,
       "pmc2002RinvReloadInventory": pmc2002RinvReloadInventory,
       "pmc2002RinvHwPlatform": pmc2002RinvHwPlatform,
       "pmc2002RinvModulePlatform": pmc2002RinvModulePlatform,
       "pmc2002RinvSwPlatform": pmc2002RinvSwPlatform,
       "pmc2002RinvGwPlatform": pmc2002RinvGwPlatform,
       "pmc2002download": pmc2002download,
       "pmc2002DwlOther": pmc2002DwlOther,
       "pmc2002DwlrestartProcess": pmc2002DwlrestartProcess,
       "pmc2002DwlWarmRestartProcessed": pmc2002DwlWarmRestartProcessed,
       "pmc2002DwlColdRestartProcessed": pmc2002DwlColdRestartProcessed,
       "pmc2002DwlswBanksUsed": pmc2002DwlswBanksUsed,
       "pmc2002DwlSwBank1Used": pmc2002DwlSwBank1Used,
       "pmc2002DwlSwBank2Used": pmc2002DwlSwBank2Used,
       "pmc2002DwlSwBank1Notempty": pmc2002DwlSwBank1Notempty,
       "pmc2002DwlSwBank2Notempty": pmc2002DwlSwBank2Notempty,
       "pmc2002DwlgwBanksUsed": pmc2002DwlgwBanksUsed,
       "pmc2002DwlGwBank1Used": pmc2002DwlGwBank1Used,
       "pmc2002DwlGwBank2Used": pmc2002DwlGwBank2Used,
       "pmc2002DwlGwBank3Used": pmc2002DwlGwBank3Used,
       "pmc2002DwlGwBank4Used": pmc2002DwlGwBank4Used,
       "pmc2002DwlGwBank1Notempty": pmc2002DwlGwBank1Notempty,
       "pmc2002DwlGwBank2Notempty": pmc2002DwlGwBank2Notempty,
       "pmc2002DwlGwBank3Notempty": pmc2002DwlGwBank3Notempty,
       "pmc2002DwlGwBank4Notempty": pmc2002DwlGwBank4Notempty,
       "pmc2002DwlClient": pmc2002DwlClient,
       "pmc2002DwlLine": pmc2002DwlLine,
       "pmc2002Config": pmc2002Config,
       "pmc2002CfgAccessCAisCsf": pmc2002CfgAccessCAisCsf,
       "pmc2002CfgClientcaiscsfTable": pmc2002CfgClientcaiscsfTable,
       "pmc2002CfgClientcaiscsfEntry": pmc2002CfgClientcaiscsfEntry,
       "pmc2002CfgClientcaiscsfIndex": pmc2002CfgClientcaiscsfIndex,
       "pmc2002CfgCAisModePortn": pmc2002CfgCAisModePortn,
       "pmc2002CfgUpAccessioAlmPortn": pmc2002CfgUpAccessioAlmPortn,
       "pmc2002CfgUpMapperDeAlmPortn": pmc2002CfgUpMapperDeAlmPortn,
       "pmc2002CfgDownAccessioAlmPortn": pmc2002CfgDownAccessioAlmPortn,
       "pmc2002CfgDownMapperDeAlmPortn": pmc2002CfgDownMapperDeAlmPortn,
       "pmc2002CfgDownDfrmAlmPortn": pmc2002CfgDownDfrmAlmPortn,
       "pmc2002CfgDownLineSyncAlarmsPortn": pmc2002CfgDownLineSyncAlarmsPortn,
       "pmc2002CfgStartup": pmc2002CfgStartup,
       "pmc2002CfgClientStartupTable": pmc2002CfgClientStartupTable,
       "pmc2002CfgClientStartupEntry": pmc2002CfgClientStartupEntry,
       "pmc2002CfgClientStartupIndex": pmc2002CfgClientStartupIndex,
       "pmc2002CfgSystConfPortPortn": pmc2002CfgSystConfPortPortn,
       "pmc2002CfgNetConfPortPortn": pmc2002CfgNetConfPortPortn,
       "pmc2002CfgPortsOptionsPortn": pmc2002CfgPortsOptionsPortn,
       "pmc2002tablelineStartup": pmc2002tablelineStartup,
       "pmc2002CfgsynthTransLine1": pmc2002CfgsynthTransLine1,
       "pmc2002CfgnetConfMod": pmc2002CfgnetConfMod,
       "pmc2002CfglineOptions1": pmc2002CfglineOptions1,
       "pmc2002CfgsystTransLine2": pmc2002CfgsystTransLine2,
       "pmc2002CfglineSelection": pmc2002CfglineSelection,
       "pmc2002CfgXfpTable": pmc2002CfgXfpTable,
       "pmc2002CfgXfpEntry": pmc2002CfgXfpEntry,
       "pmc2002CfgXfpIndex": pmc2002CfgXfpIndex,
       "pmc2002CfgSystConfXfpPortn": pmc2002CfgSystConfXfpPortn,
       "pmc2002CfgDataRateConfXfpPortn": pmc2002CfgDataRateConfXfpPortn,
       "pmc2002CfgOtxtlhTable": pmc2002CfgOtxtlhTable,
       "pmc2002CfgOtxtlhEntry": pmc2002CfgOtxtlhEntry,
       "pmc2002CfgOtxtlhIndex": pmc2002CfgOtxtlhIndex,
       "pmc2002CfgLineDitherRatePortn": pmc2002CfgLineDitherRatePortn,
       "pmc2002CfgLineDitherFhzPortn": pmc2002CfgLineDitherFhzPortn,
       "pmc2002CfgLinePwrLaserPortn": pmc2002CfgLinePwrLaserPortn,
       "pmc2002CfgFPortn": pmc2002CfgFPortn,
       "pmc2002CfgReservedPortn": pmc2002CfgReservedPortn,
       "pmc2002CfgLinePhotodiodeModePortn": pmc2002CfgLinePhotodiodeModePortn,
       "pmc2002CfgLinePhotodiodeValuePortn": pmc2002CfgLinePhotodiodeValuePortn,
       "pmc2002CfgOtxtlhCommonTable": pmc2002CfgOtxtlhCommonTable,
       "pmc2002CfgOtxtlhCommonEntry": pmc2002CfgOtxtlhCommonEntry,
       "pmc2002CfgOtxtlhCommonIndex": pmc2002CfgOtxtlhCommonIndex,
       "pmc2002CfgLineFCurrentPortn": pmc2002CfgLineFCurrentPortn,
       "pmc2002CfgLineGridCurrentPortn": pmc2002CfgLineGridCurrentPortn,
       "pmc2002CfgLabels": pmc2002CfgLabels,
       "pmc2002CfgLabelclientTable": pmc2002CfgLabelclientTable,
       "pmc2002CfgLabelclientEntry": pmc2002CfgLabelclientEntry,
       "pmc2002CfgLabelclientIndex": pmc2002CfgLabelclientIndex,
       "pmc2002CfgLabelclientPortn": pmc2002CfgLabelclientPortn,
       "pmc2002CfgLabellineTable": pmc2002CfgLabellineTable,
       "pmc2002CfgLabellineEntry": pmc2002CfgLabellineEntry,
       "pmc2002CfgLabellineIndex": pmc2002CfgLabellineIndex,
       "pmc2002CfgLabellinePortn": pmc2002CfgLabellinePortn,
       "pmc2002CfgOther": pmc2002CfgOther,
       "pmc2002tablemoduleOther": pmc2002tablemoduleOther,
       "pmc2002Cfgmode": pmc2002Cfgmode,
       "pmc2002CfgStartuptablefive": pmc2002CfgStartuptablefive,
       "pmc2002CfgOtxtlhcapabilitiesTable": pmc2002CfgOtxtlhcapabilitiesTable,
       "pmc2002CfgOtxtlhcapabilitiesEntry": pmc2002CfgOtxtlhcapabilitiesEntry,
       "pmc2002CfgOtxtlhcapabilitiesIndex": pmc2002CfgOtxtlhcapabilitiesIndex,
       "pmc2002CfgComponentTypePortn": pmc2002CfgComponentTypePortn,
       "pmc2002CfgMiscellaneousPortn": pmc2002CfgMiscellaneousPortn,
       "pmc2002CfgFirstChannelPortn": pmc2002CfgFirstChannelPortn,
       "pmc2002CfgLastChannelPortn": pmc2002CfgLastChannelPortn,
       "pmc2002CfgGridPortn": pmc2002CfgGridPortn,
       "pmc2002CfgWriteConfiguration": pmc2002CfgWriteConfiguration,
       "pmc2002traps": pmc2002traps,
       "pmc2002trapBoardNumber": pmc2002trapBoardNumber,
       "pmc2002trapClientNumber": pmc2002trapClientNumber,
       "pmc2002trapLineNumber": pmc2002trapLineNumber,
       "pmc2002LineTrapNotUrgentGoesOn": pmc2002LineTrapNotUrgentGoesOn,
       "pmc2002LineTrapNotUrgentGoesOff": pmc2002LineTrapNotUrgentGoesOff,
       "pmc2002LineTrapUrgentGoesOn": pmc2002LineTrapUrgentGoesOn,
       "pmc2002LineTrapUrgentGoesOff": pmc2002LineTrapUrgentGoesOff,
       "pmc2002LineTrapCritGoesOn": pmc2002LineTrapCritGoesOn,
       "pmc2002LineTrapCritGoesOff": pmc2002LineTrapCritGoesOff,
       "pmc2002ClientTrapNotUrgentGoesOn": pmc2002ClientTrapNotUrgentGoesOn,
       "pmc2002ClientTrapNotUrgentGoesOff": pmc2002ClientTrapNotUrgentGoesOff,
       "pmc2002ClientTrapUrgentGoesOn": pmc2002ClientTrapUrgentGoesOn,
       "pmc2002ClientTrapUrgentGoesOff": pmc2002ClientTrapUrgentGoesOff,
       "pmc2002ClientTrapCritGoesOn": pmc2002ClientTrapCritGoesOn,
       "pmc2002ClientTrapCritGoesOff": pmc2002ClientTrapCritGoesOff,
       "pmc2002PowerTrapUrgentGoesOn": pmc2002PowerTrapUrgentGoesOn,
       "pmc2002PowerTrapUrgentGoesOff": pmc2002PowerTrapUrgentGoesOff,
       "pmc2002Monitoring": pmc2002Monitoring,
       "pmc2002MonOther": pmc2002MonOther,
       "pmc2002MonSync": pmc2002MonSync,
       "pmc2002PerfEnable": pmc2002PerfEnable,
       "pmc2002Perf15minSync": pmc2002Perf15minSync,
       "pmc2002Perf24hSync": pmc2002Perf24hSync,
       "pmc2002MonTimeStamp": pmc2002MonTimeStamp,
       "pmc2002Perf15MinShort": pmc2002Perf15MinShort,
       "pmc2002Perf15MinLong": pmc2002Perf15MinLong,
       "pmc2002Perf24HoursShort": pmc2002Perf24HoursShort,
       "pmc2002Perf24HoursLong": pmc2002Perf24HoursLong,
       "pmc2002PerfCurrent15MinElapsedTime": pmc2002PerfCurrent15MinElapsedTime,
       "pmc2002PerfCurrent24HoursElapsedTime": pmc2002PerfCurrent24HoursElapsedTime,
       "pmc2002MonClient": pmc2002MonClient,
       "pmc2002PerfTelecomClientCurrent15StatTable": pmc2002PerfTelecomClientCurrent15StatTable,
       "pmc2002PerfTelecomClientCurrent15StatEntry": pmc2002PerfTelecomClientCurrent15StatEntry,
       "pmc2002PerfTelecomClientCurrent15StatIndex": pmc2002PerfTelecomClientCurrent15StatIndex,
       "pmc2002PerfTelecomClientCurrent15StatInvCvPortn": pmc2002PerfTelecomClientCurrent15StatInvCvPortn,
       "pmc2002PerfTelecomClientCurrent15StatCvValuePortn": pmc2002PerfTelecomClientCurrent15StatCvValuePortn,
       "pmc2002PerfTelecomClientCurrent15StatInvEsPortn": pmc2002PerfTelecomClientCurrent15StatInvEsPortn,
       "pmc2002PerfTelecomClientCurrent15StatEsValuePortn": pmc2002PerfTelecomClientCurrent15StatEsValuePortn,
       "pmc2002PerfTelecomClientCurrent15StatInvSesPortn": pmc2002PerfTelecomClientCurrent15StatInvSesPortn,
       "pmc2002PerfTelecomClientCurrent15StatSesValuePortn": pmc2002PerfTelecomClientCurrent15StatSesValuePortn,
       "pmc2002PerfTelecomClientCurrent15StatInvSefsPortn": pmc2002PerfTelecomClientCurrent15StatInvSefsPortn,
       "pmc2002PerfTelecomClientCurrent15StatSefsValuePortn": pmc2002PerfTelecomClientCurrent15StatSefsValuePortn,
       "pmc2002PerfTelecomClientCurrent15StatInvUasPortn": pmc2002PerfTelecomClientCurrent15StatInvUasPortn,
       "pmc2002PerfTelecomClientCurrent15StatUasValuePortn": pmc2002PerfTelecomClientCurrent15StatUasValuePortn,
       "pmc2002PerfTelecomClientPast15StatHistoryPort1Table": pmc2002PerfTelecomClientPast15StatHistoryPort1Table,
       "pmc2002PerfTelecomClientPast15StatHistoryPort1Entry": pmc2002PerfTelecomClientPast15StatHistoryPort1Entry,
       "pmc2002PerfTelecomClientPast15StatHistoryPort1Index": pmc2002PerfTelecomClientPast15StatHistoryPort1Index,
       "pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1": pmc2002PerfTelecomClientPast15StatHistoryInvCvPort1,
       "pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1": pmc2002PerfTelecomClientPast15StatHistoryCvValuePort1,
       "pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1": pmc2002PerfTelecomClientPast15StatHistoryInvEsPort1,
       "pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1": pmc2002PerfTelecomClientPast15StatHistoryEsValuePort1,
       "pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1": pmc2002PerfTelecomClientPast15StatHistoryInvSesPort1,
       "pmc2002PerfTelecomClientPast15StatHistorySesValuePort1": pmc2002PerfTelecomClientPast15StatHistorySesValuePort1,
       "pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1": pmc2002PerfTelecomClientPast15StatHistoryInvSefsPort1,
       "pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1": pmc2002PerfTelecomClientPast15StatHistorySefsValuePort1,
       "pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1": pmc2002PerfTelecomClientPast15StatHistoryInvUasPort1,
       "pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1": pmc2002PerfTelecomClientPast15StatHistoryUasValuePort1,
       "pmc2002PerfTelecomClientCurrent24StatTable": pmc2002PerfTelecomClientCurrent24StatTable,
       "pmc2002PerfTelecomClientCurrent24StatEntry": pmc2002PerfTelecomClientCurrent24StatEntry,
       "pmc2002PerfTelecomClientCurrent24StatIndex": pmc2002PerfTelecomClientCurrent24StatIndex,
       "pmc2002PerfTelecomClientCurrent24StatInvCvPortn": pmc2002PerfTelecomClientCurrent24StatInvCvPortn,
       "pmc2002PerfTelecomClientCurrent24StatCvValuePortn": pmc2002PerfTelecomClientCurrent24StatCvValuePortn,
       "pmc2002PerfTelecomClientCurrent24StatInvEsPortn": pmc2002PerfTelecomClientCurrent24StatInvEsPortn,
       "pmc2002PerfTelecomClientCurrent24StatEsValuePortn": pmc2002PerfTelecomClientCurrent24StatEsValuePortn,
       "pmc2002PerfTelecomClientCurrent24StatInvSesPortn": pmc2002PerfTelecomClientCurrent24StatInvSesPortn,
       "pmc2002PerfTelecomClientCurrent24StatSesValuePortn": pmc2002PerfTelecomClientCurrent24StatSesValuePortn,
       "pmc2002PerfTelecomClientCurrent24StatInvSefsPortn": pmc2002PerfTelecomClientCurrent24StatInvSefsPortn,
       "pmc2002PerfTelecomClientCurrent24StatSefsValuePortn": pmc2002PerfTelecomClientCurrent24StatSefsValuePortn,
       "pmc2002PerfTelecomClientCurrent24StatInvUasPortn": pmc2002PerfTelecomClientCurrent24StatInvUasPortn,
       "pmc2002PerfTelecomClientCurrent24StatUasValuePortn": pmc2002PerfTelecomClientCurrent24StatUasValuePortn,
       "pmc2002PerfTelecomClientPast24StatHistoryPort1Table": pmc2002PerfTelecomClientPast24StatHistoryPort1Table,
       "pmc2002PerfTelecomClientPast24StatHistoryPort1Entry": pmc2002PerfTelecomClientPast24StatHistoryPort1Entry,
       "pmc2002PerfTelecomClientPast24StatHistoryPort1Index": pmc2002PerfTelecomClientPast24StatHistoryPort1Index,
       "pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1": pmc2002PerfTelecomClientPast24StatHistoryInvCvPort1,
       "pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1": pmc2002PerfTelecomClientPast24StatHistoryCvValuePort1,
       "pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1": pmc2002PerfTelecomClientPast24StatHistoryInvEsPort1,
       "pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1": pmc2002PerfTelecomClientPast24StatHistoryEsValuePort1,
       "pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1": pmc2002PerfTelecomClientPast24StatHistoryInvSesPort1,
       "pmc2002PerfTelecomClientPast24StatHistorySesValuePort1": pmc2002PerfTelecomClientPast24StatHistorySesValuePort1,
       "pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1": pmc2002PerfTelecomClientPast24StatHistoryInvSefsPort1,
       "pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1": pmc2002PerfTelecomClientPast24StatHistorySefsValuePort1,
       "pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1": pmc2002PerfTelecomClientPast24StatHistoryInvUasPort1,
       "pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1": pmc2002PerfTelecomClientPast24StatHistoryUasValuePort1,
       "pmc2002PerfDatacomClientCurrent15StatTable": pmc2002PerfDatacomClientCurrent15StatTable,
       "pmc2002PerfDatacomClientCurrent15StatEntry": pmc2002PerfDatacomClientCurrent15StatEntry,
       "pmc2002PerfDatacomClientCurrent15StatIndex": pmc2002PerfDatacomClientCurrent15StatIndex,
       "pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn": pmc2002perfdatacomclientCurrent15StatInBytesCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatInBytesCountPortn": pmc2002perfdatacomclientCurrent15StatInBytesCountPortn,
       "pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn": pmc2002perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatInCrcCountPortn": pmc2002perfdatacomclientCurrent15StatInCrcCountPortn,
       "pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn": pmc2002perfdatacomclientCurrent15StatInBroadcastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn": pmc2002perfdatacomclientCurrent15StatInBroadcastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn": pmc2002perfdatacomclientCurrent15StatInMulticastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn": pmc2002perfdatacomclientCurrent15StatInMulticastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn": pmc2002perfdatacomclientCurrent15StatInUnicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn": pmc2002perfdatacomclientCurrent15StatInUnicastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn": pmc2002perfdatacomclientCurrent15StatInNonunicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn": pmc2002perfdatacomclientCurrent15StatInNonunicastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn": pmc2002perfdatacomclientCurrent15StatOutBytesCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn": pmc2002perfdatacomclientCurrent15StatOutBytesCountPortn,
       "pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn": pmc2002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn": pmc2002perfdatacomclientCurrent15StatOutBroadcastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn": pmc2002perfdatacomclientCurrent15StatOutMulticastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn": pmc2002perfdatacomclientCurrent15StatOutMulticastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn": pmc2002perfdatacomclientCurrent15StatOutUnicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn": pmc2002perfdatacomclientCurrent15StatOutUnicastCountPortn,
       "pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn": pmc2002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn": pmc2002perfdatacomclientCurrent15StatOutNonunicastCountPortn,
       "pmc2002PerfDatacomClientPast15StatHistoryPort1Table": pmc2002PerfDatacomClientPast15StatHistoryPort1Table,
       "pmc2002PerfDatacomClientPast15StatHistoryPort1Entry": pmc2002PerfDatacomClientPast15StatHistoryPort1Entry,
       "pmc2002PerfDatacomClientPast15StatHistoryPort1Index": pmc2002PerfDatacomClientPast15StatHistoryPort1Index,
       "pmc2002perfdatacomclientPast15StatInBytesCountInvPort1": pmc2002perfdatacomclientPast15StatInBytesCountInvPort1,
       "pmc2002perfdatacomclientPast15StatInBytesCountPort1": pmc2002perfdatacomclientPast15StatInBytesCountPort1,
       "pmc2002perfdatacomclientPast15StatInCrcCountInvPort1": pmc2002perfdatacomclientPast15StatInCrcCountInvPort1,
       "pmc2002perfdatacomclientPast15StatInCrcCountPort1": pmc2002perfdatacomclientPast15StatInCrcCountPort1,
       "pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1": pmc2002perfdatacomclientPast15StatInBroadcastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatInBroadcastCountPort1": pmc2002perfdatacomclientPast15StatInBroadcastCountPort1,
       "pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1": pmc2002perfdatacomclientPast15StatInMulticastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatInMulticastCountPort1": pmc2002perfdatacomclientPast15StatInMulticastCountPort1,
       "pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1": pmc2002perfdatacomclientPast15StatInUnicastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatInUnicastCountPort1": pmc2002perfdatacomclientPast15StatInUnicastCountPort1,
       "pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1": pmc2002perfdatacomclientPast15StatInNonunicastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatInNonunicastCountPort1": pmc2002perfdatacomclientPast15StatInNonunicastCountPort1,
       "pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1": pmc2002perfdatacomclientPast15StatOutBytesCountInvPort1,
       "pmc2002perfdatacomclientPast15StatOutBytesCountPort1": pmc2002perfdatacomclientPast15StatOutBytesCountPort1,
       "pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1": pmc2002perfdatacomclientPast15StatOutBroadcastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1": pmc2002perfdatacomclientPast15StatOutBroadcastCountPort1,
       "pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1": pmc2002perfdatacomclientPast15StatOutMulticastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatOutMulticastCountPort1": pmc2002perfdatacomclientPast15StatOutMulticastCountPort1,
       "pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1": pmc2002perfdatacomclientPast15StatOutUnicastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatOutUnicastCountPort1": pmc2002perfdatacomclientPast15StatOutUnicastCountPort1,
       "pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1": pmc2002perfdatacomclientPast15StatOutNonunicastCountInvPort1,
       "pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1": pmc2002perfdatacomclientPast15StatOutNonunicastCountPort1,
       "pmc2002PerfDatacomClientCurrent24StatTable": pmc2002PerfDatacomClientCurrent24StatTable,
       "pmc2002PerfDatacomClientCurrent24StatEntry": pmc2002PerfDatacomClientCurrent24StatEntry,
       "pmc2002PerfDatacomClientCurrent24StatIndex": pmc2002PerfDatacomClientCurrent24StatIndex,
       "pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn": pmc2002perfdatacomclientCurrent24StatInBytesCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatInBytesCountPortn": pmc2002perfdatacomclientCurrent24StatInBytesCountPortn,
       "pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn": pmc2002perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatInCrcCountPortn": pmc2002perfdatacomclientCurrent24StatInCrcCountPortn,
       "pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn": pmc2002perfdatacomclientCurrent24StatInBroadcastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn": pmc2002perfdatacomclientCurrent24StatInBroadcastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn": pmc2002perfdatacomclientCurrent24StatInMulticastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn": pmc2002perfdatacomclientCurrent24StatInMulticastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn": pmc2002perfdatacomclientCurrent24StatInUnicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn": pmc2002perfdatacomclientCurrent24StatInUnicastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn": pmc2002perfdatacomclientCurrent24StatInNonunicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn": pmc2002perfdatacomclientCurrent24StatInNonunicastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn": pmc2002perfdatacomclientCurrent24StatOutBytesCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn": pmc2002perfdatacomclientCurrent24StatOutBytesCountPortn,
       "pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn": pmc2002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn": pmc2002perfdatacomclientCurrent24StatOutBroadcastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn": pmc2002perfdatacomclientCurrent24StatOutMulticastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn": pmc2002perfdatacomclientCurrent24StatOutMulticastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn": pmc2002perfdatacomclientCurrent24StatOutUnicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn": pmc2002perfdatacomclientCurrent24StatOutUnicastCountPortn,
       "pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn": pmc2002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn,
       "pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn": pmc2002perfdatacomclientCurrent24StatOutNonunicastCountPortn,
       "pmc2002PerfDatacomClientPast24StatHistoryPort1Table": pmc2002PerfDatacomClientPast24StatHistoryPort1Table,
       "pmc2002PerfDatacomClientPast24StatHistoryPort1Entry": pmc2002PerfDatacomClientPast24StatHistoryPort1Entry,
       "pmc2002PerfDatacomClientPast24StatHistoryPort1Index": pmc2002PerfDatacomClientPast24StatHistoryPort1Index,
       "pmc2002perfdatacomclientPast24StatInBytesCountInvPort1": pmc2002perfdatacomclientPast24StatInBytesCountInvPort1,
       "pmc2002perfdatacomclientPast24StatInBytesCountPort1": pmc2002perfdatacomclientPast24StatInBytesCountPort1,
       "pmc2002perfdatacomclientPast24StatInCrcCountInvPort1": pmc2002perfdatacomclientPast24StatInCrcCountInvPort1,
       "pmc2002perfdatacomclientPast24StatInCrcCountPort1": pmc2002perfdatacomclientPast24StatInCrcCountPort1,
       "pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1": pmc2002perfdatacomclientPast24StatInBroadcastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatInBroadcastCountPort1": pmc2002perfdatacomclientPast24StatInBroadcastCountPort1,
       "pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1": pmc2002perfdatacomclientPast24StatInMulticastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatInMulticastCountPort1": pmc2002perfdatacomclientPast24StatInMulticastCountPort1,
       "pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1": pmc2002perfdatacomclientPast24StatInUnicastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatInUnicastCountPort1": pmc2002perfdatacomclientPast24StatInUnicastCountPort1,
       "pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1": pmc2002perfdatacomclientPast24StatInNonunicastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatInNonunicastCountPort1": pmc2002perfdatacomclientPast24StatInNonunicastCountPort1,
       "pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1": pmc2002perfdatacomclientPast24StatOutBytesCountInvPort1,
       "pmc2002perfdatacomclientPast24StatOutBytesCountPort1": pmc2002perfdatacomclientPast24StatOutBytesCountPort1,
       "pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1": pmc2002perfdatacomclientPast24StatOutBroadcastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1": pmc2002perfdatacomclientPast24StatOutBroadcastCountPort1,
       "pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1": pmc2002perfdatacomclientPast24StatOutMulticastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatOutMulticastCountPort1": pmc2002perfdatacomclientPast24StatOutMulticastCountPort1,
       "pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1": pmc2002perfdatacomclientPast24StatOutUnicastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatOutUnicastCountPort1": pmc2002perfdatacomclientPast24StatOutUnicastCountPort1,
       "pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1": pmc2002perfdatacomclientPast24StatOutNonunicastCountInvPort1,
       "pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1": pmc2002perfdatacomclientPast24StatOutNonunicastCountPort1,
       "pmc2002MonLine": pmc2002MonLine,
       "pmc2002PerfTelecomLineCurrent15StatTable": pmc2002PerfTelecomLineCurrent15StatTable,
       "pmc2002PerfTelecomLineCurrent15StatEntry": pmc2002PerfTelecomLineCurrent15StatEntry,
       "pmc2002PerfTelecomLineCurrent15StatIndex": pmc2002PerfTelecomLineCurrent15StatIndex,
       "pmc2002PerfTelecomLineCurrent15StatInvCvPortn": pmc2002PerfTelecomLineCurrent15StatInvCvPortn,
       "pmc2002PerfTelecomLineCurrent15StatCvValuePortn": pmc2002PerfTelecomLineCurrent15StatCvValuePortn,
       "pmc2002PerfTelecomLineCurrent15StatInvEsPortn": pmc2002PerfTelecomLineCurrent15StatInvEsPortn,
       "pmc2002PerfTelecomLineCurrent15StatEsValuePortn": pmc2002PerfTelecomLineCurrent15StatEsValuePortn,
       "pmc2002PerfTelecomLineCurrent15StatInvSesPortn": pmc2002PerfTelecomLineCurrent15StatInvSesPortn,
       "pmc2002PerfTelecomLineCurrent15StatSesValuePortn": pmc2002PerfTelecomLineCurrent15StatSesValuePortn,
       "pmc2002PerfTelecomLineCurrent15StatInvSefsPortn": pmc2002PerfTelecomLineCurrent15StatInvSefsPortn,
       "pmc2002PerfTelecomLineCurrent15StatSefsValuePortn": pmc2002PerfTelecomLineCurrent15StatSefsValuePortn,
       "pmc2002PerfTelecomLineCurrent15StatInvUasPortn": pmc2002PerfTelecomLineCurrent15StatInvUasPortn,
       "pmc2002PerfTelecomLineCurrent15StatUasValuePortn": pmc2002PerfTelecomLineCurrent15StatUasValuePortn,
       "pmc2002PerfTelecomLinePast15StatHistoryPort1Table": pmc2002PerfTelecomLinePast15StatHistoryPort1Table,
       "pmc2002PerfTelecomLinePast15StatHistoryPort1Entry": pmc2002PerfTelecomLinePast15StatHistoryPort1Entry,
       "pmc2002PerfTelecomLinePast15StatHistoryPort1Index": pmc2002PerfTelecomLinePast15StatHistoryPort1Index,
       "pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1": pmc2002PerfTelecomLinePast15StatHistoryInvCvPort1,
       "pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1": pmc2002PerfTelecomLinePast15StatHistoryCvValuePort1,
       "pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1": pmc2002PerfTelecomLinePast15StatHistoryInvEsPort1,
       "pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1": pmc2002PerfTelecomLinePast15StatHistoryEsValuePort1,
       "pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1": pmc2002PerfTelecomLinePast15StatHistoryInvSesPort1,
       "pmc2002PerfTelecomLinePast15StatHistorySesValuePort1": pmc2002PerfTelecomLinePast15StatHistorySesValuePort1,
       "pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1": pmc2002PerfTelecomLinePast15StatHistoryInvSefsPort1,
       "pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1": pmc2002PerfTelecomLinePast15StatHistorySefsValuePort1,
       "pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1": pmc2002PerfTelecomLinePast15StatHistoryInvUasPort1,
       "pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1": pmc2002PerfTelecomLinePast15StatHistoryUasValuePort1,
       "pmc2002PerfTelecomLineCurrent24StatTable": pmc2002PerfTelecomLineCurrent24StatTable,
       "pmc2002PerfTelecomLineCurrent24StatEntry": pmc2002PerfTelecomLineCurrent24StatEntry,
       "pmc2002PerfTelecomLineCurrent24StatIndex": pmc2002PerfTelecomLineCurrent24StatIndex,
       "pmc2002PerfTelecomLineCurrent24StatInvCvPortn": pmc2002PerfTelecomLineCurrent24StatInvCvPortn,
       "pmc2002PerfTelecomLineCurrent24StatCvValuePortn": pmc2002PerfTelecomLineCurrent24StatCvValuePortn,
       "pmc2002PerfTelecomLineCurrent24StatInvEsPortn": pmc2002PerfTelecomLineCurrent24StatInvEsPortn,
       "pmc2002PerfTelecomLineCurrent24StatEsValuePortn": pmc2002PerfTelecomLineCurrent24StatEsValuePortn,
       "pmc2002PerfTelecomLineCurrent24StatInvSesPortn": pmc2002PerfTelecomLineCurrent24StatInvSesPortn,
       "pmc2002PerfTelecomLineCurrent24StatSesValuePortn": pmc2002PerfTelecomLineCurrent24StatSesValuePortn,
       "pmc2002PerfTelecomLineCurrent24StatInvSefsPortn": pmc2002PerfTelecomLineCurrent24StatInvSefsPortn,
       "pmc2002PerfTelecomLineCurrent24StatSefsValuePortn": pmc2002PerfTelecomLineCurrent24StatSefsValuePortn,
       "pmc2002PerfTelecomLineCurrent24StatInvUasPortn": pmc2002PerfTelecomLineCurrent24StatInvUasPortn,
       "pmc2002PerfTelecomLineCurrent24StatUasValuePortn": pmc2002PerfTelecomLineCurrent24StatUasValuePortn,
       "pmc2002PerfTelecomLinePast24StatHistoryPort1Table": pmc2002PerfTelecomLinePast24StatHistoryPort1Table,
       "pmc2002PerfTelecomLinePast24StatHistoryPort1Entry": pmc2002PerfTelecomLinePast24StatHistoryPort1Entry,
       "pmc2002PerfTelecomLinePast24StatHistoryPort1Index": pmc2002PerfTelecomLinePast24StatHistoryPort1Index,
       "pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1": pmc2002PerfTelecomLinePast24StatHistoryInvCvPort1,
       "pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1": pmc2002PerfTelecomLinePast24StatHistoryCvValuePort1,
       "pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1": pmc2002PerfTelecomLinePast24StatHistoryInvEsPort1,
       "pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1": pmc2002PerfTelecomLinePast24StatHistoryEsValuePort1,
       "pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1": pmc2002PerfTelecomLinePast24StatHistoryInvSesPort1,
       "pmc2002PerfTelecomLinePast24StatHistorySesValuePort1": pmc2002PerfTelecomLinePast24StatHistorySesValuePort1,
       "pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1": pmc2002PerfTelecomLinePast24StatHistoryInvSefsPort1,
       "pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1": pmc2002PerfTelecomLinePast24StatHistorySefsValuePort1,
       "pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1": pmc2002PerfTelecomLinePast24StatHistoryInvUasPort1,
       "pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1": pmc2002PerfTelecomLinePast24StatHistoryUasValuePort1,
       "pmc2002Rmon": pmc2002Rmon,
       "pmc2002RmonClient": pmc2002RmonClient,
       "pmc2002MonupRmonByteCntTable": pmc2002MonupRmonByteCntTable,
       "pmc2002MonupRmonByteCntEntry": pmc2002MonupRmonByteCntEntry,
       "pmc2002MonupRmonByteCntIndex": pmc2002MonupRmonByteCntIndex,
       "pmc2002MonupRmonByteCntValuePortn": pmc2002MonupRmonByteCntValuePortn,
       "pmc2002MonupRmonByteCntErrorPortn": pmc2002MonupRmonByteCntErrorPortn,
       "pmc2002MonupRmonByteCntOverloadPortn": pmc2002MonupRmonByteCntOverloadPortn,
       "pmc2002MonupRmonCrcErrorCntTable": pmc2002MonupRmonCrcErrorCntTable,
       "pmc2002MonupRmonCrcErrorCntEntry": pmc2002MonupRmonCrcErrorCntEntry,
       "pmc2002MonupRmonCrcErrorCntIndex": pmc2002MonupRmonCrcErrorCntIndex,
       "pmc2002MonupRmonCrcErrorCntValuePortn": pmc2002MonupRmonCrcErrorCntValuePortn,
       "pmc2002MonupRmonCrcErrorCntErrorPortn": pmc2002MonupRmonCrcErrorCntErrorPortn,
       "pmc2002MonupRmonCrcErrorCntOverloadPortn": pmc2002MonupRmonCrcErrorCntOverloadPortn,
       "pmc2002MonupRmonPacketsCntTable": pmc2002MonupRmonPacketsCntTable,
       "pmc2002MonupRmonPacketsCntEntry": pmc2002MonupRmonPacketsCntEntry,
       "pmc2002MonupRmonPacketsCntIndex": pmc2002MonupRmonPacketsCntIndex,
       "pmc2002MonupRmonPacketsCntValuePortn": pmc2002MonupRmonPacketsCntValuePortn,
       "pmc2002MonupRmonPacketsCntErrorPortn": pmc2002MonupRmonPacketsCntErrorPortn,
       "pmc2002MonupRmonPacketsCntOverloadPortn": pmc2002MonupRmonPacketsCntOverloadPortn,
       "pmc2002MonupRmonBroadcastCntTable": pmc2002MonupRmonBroadcastCntTable,
       "pmc2002MonupRmonBroadcastCntEntry": pmc2002MonupRmonBroadcastCntEntry,
       "pmc2002MonupRmonBroadcastCntIndex": pmc2002MonupRmonBroadcastCntIndex,
       "pmc2002MonupRmonBroadcastCntValuePortn": pmc2002MonupRmonBroadcastCntValuePortn,
       "pmc2002MonupRmonBroadcastCntErrorPortn": pmc2002MonupRmonBroadcastCntErrorPortn,
       "pmc2002MonupRmonBroadcastCntOverloadPortn": pmc2002MonupRmonBroadcastCntOverloadPortn,
       "pmc2002MonupRmonMulticastCntTable": pmc2002MonupRmonMulticastCntTable,
       "pmc2002MonupRmonMulticastCntEntry": pmc2002MonupRmonMulticastCntEntry,
       "pmc2002MonupRmonMulticastCntIndex": pmc2002MonupRmonMulticastCntIndex,
       "pmc2002MonupRmonMulticastCntValuePortn": pmc2002MonupRmonMulticastCntValuePortn,
       "pmc2002MonupRmonMulticastCntErrorPortn": pmc2002MonupRmonMulticastCntErrorPortn,
       "pmc2002MonupRmonMulticastCntOverloadPortn": pmc2002MonupRmonMulticastCntOverloadPortn,
       "pmc2002MonupRmonTimerCntTable": pmc2002MonupRmonTimerCntTable,
       "pmc2002MonupRmonTimerCntEntry": pmc2002MonupRmonTimerCntEntry,
       "pmc2002MonupRmonTimerCntIndex": pmc2002MonupRmonTimerCntIndex,
       "pmc2002MonupRmonTimerCntValuePortn": pmc2002MonupRmonTimerCntValuePortn,
       "pmc2002MonupRmonTimerCntErrorPortn": pmc2002MonupRmonTimerCntErrorPortn,
       "pmc2002MonupRmonTimerCntOverloadPortn": pmc2002MonupRmonTimerCntOverloadPortn,
       "pmc2002MonupRmonPauseFrameCntTable": pmc2002MonupRmonPauseFrameCntTable,
       "pmc2002MonupRmonPauseFrameCntEntry": pmc2002MonupRmonPauseFrameCntEntry,
       "pmc2002MonupRmonPauseFrameCntIndex": pmc2002MonupRmonPauseFrameCntIndex,
       "pmc2002MonupRmonPauseFrameCntValuePortn": pmc2002MonupRmonPauseFrameCntValuePortn,
       "pmc2002MonupRmonPauseFrameCntErrorPortn": pmc2002MonupRmonPauseFrameCntErrorPortn,
       "pmc2002MonupRmonPauseFrameCntOverloadPortn": pmc2002MonupRmonPauseFrameCntOverloadPortn,
       "pmc2002MonupRmonDropFrameCntTable": pmc2002MonupRmonDropFrameCntTable,
       "pmc2002MonupRmonDropFrameCntEntry": pmc2002MonupRmonDropFrameCntEntry,
       "pmc2002MonupRmonDropFrameCntIndex": pmc2002MonupRmonDropFrameCntIndex,
       "pmc2002MonupRmonDropFrameCntValuePortn": pmc2002MonupRmonDropFrameCntValuePortn,
       "pmc2002MonupRmonDropFrameCntErrorPortn": pmc2002MonupRmonDropFrameCntErrorPortn,
       "pmc2002MonupRmonDropFrameCntOverloadPortn": pmc2002MonupRmonDropFrameCntOverloadPortn,
       "pmc2002MonupRmonBitsCntTable": pmc2002MonupRmonBitsCntTable,
       "pmc2002MonupRmonBitsCntEntry": pmc2002MonupRmonBitsCntEntry,
       "pmc2002MonupRmonBitsCntIndex": pmc2002MonupRmonBitsCntIndex,
       "pmc2002MonupRmonBitsCntValuePortn": pmc2002MonupRmonBitsCntValuePortn,
       "pmc2002MonupRmonBitsCntErrorPortn": pmc2002MonupRmonBitsCntErrorPortn,
       "pmc2002MonupRmonBitsCntOverloadPortn": pmc2002MonupRmonBitsCntOverloadPortn,
       "pmc2002MonupRmonUnicastCntTable": pmc2002MonupRmonUnicastCntTable,
       "pmc2002MonupRmonUnicastCntEntry": pmc2002MonupRmonUnicastCntEntry,
       "pmc2002MonupRmonUnicastCntIndex": pmc2002MonupRmonUnicastCntIndex,
       "pmc2002MonupRmonUnicastCntValuePortn": pmc2002MonupRmonUnicastCntValuePortn,
       "pmc2002MonupRmonUnicastCntErrorPortn": pmc2002MonupRmonUnicastCntErrorPortn,
       "pmc2002MonupRmonUnicastCntOverloadPortn": pmc2002MonupRmonUnicastCntOverloadPortn,
       "pmc2002MonupRmonNonUnicastCntTable": pmc2002MonupRmonNonUnicastCntTable,
       "pmc2002MonupRmonNonUnicastCntEntry": pmc2002MonupRmonNonUnicastCntEntry,
       "pmc2002MonupRmonNonUnicastCntIndex": pmc2002MonupRmonNonUnicastCntIndex,
       "pmc2002MonupRmonNonUnicastCntValuePortn": pmc2002MonupRmonNonUnicastCntValuePortn,
       "pmc2002MonupRmonNonUnicastCntErrorPortn": pmc2002MonupRmonNonUnicastCntErrorPortn,
       "pmc2002MonupRmonNonUnicastCntOverloadPortn": pmc2002MonupRmonNonUnicastCntOverloadPortn,
       "pmc2002MondwRmonByteCntTable": pmc2002MondwRmonByteCntTable,
       "pmc2002MondwRmonByteCntEntry": pmc2002MondwRmonByteCntEntry,
       "pmc2002MondwRmonByteCntIndex": pmc2002MondwRmonByteCntIndex,
       "pmc2002MondwRmonByteCntValuePortn": pmc2002MondwRmonByteCntValuePortn,
       "pmc2002MondwRmonByteCntErrorPortn": pmc2002MondwRmonByteCntErrorPortn,
       "pmc2002MondwRmonByteCntOverloadPortn": pmc2002MondwRmonByteCntOverloadPortn,
       "pmc2002MondwRmonCrcErrorCntTable": pmc2002MondwRmonCrcErrorCntTable,
       "pmc2002MondwRmonCrcErrorCntEntry": pmc2002MondwRmonCrcErrorCntEntry,
       "pmc2002MondwRmonCrcErrorCntIndex": pmc2002MondwRmonCrcErrorCntIndex,
       "pmc2002MondwRmonCrcErrorCntValuePortn": pmc2002MondwRmonCrcErrorCntValuePortn,
       "pmc2002MondwRmonCrcErrorCntErrorPortn": pmc2002MondwRmonCrcErrorCntErrorPortn,
       "pmc2002MondwRmonCrcErrorCntOverloadPortn": pmc2002MondwRmonCrcErrorCntOverloadPortn,
       "pmc2002MondwRmonPacketsCntTable": pmc2002MondwRmonPacketsCntTable,
       "pmc2002MondwRmonPacketsCntEntry": pmc2002MondwRmonPacketsCntEntry,
       "pmc2002MondwRmonPacketsCntIndex": pmc2002MondwRmonPacketsCntIndex,
       "pmc2002MondwRmonPacketsCntValuePortn": pmc2002MondwRmonPacketsCntValuePortn,
       "pmc2002MondwRmonPacketsCntErrorPortn": pmc2002MondwRmonPacketsCntErrorPortn,
       "pmc2002MondwRmonPacketsCntOverloadPortn": pmc2002MondwRmonPacketsCntOverloadPortn,
       "pmc2002MondwRmonBroadcastCntTable": pmc2002MondwRmonBroadcastCntTable,
       "pmc2002MondwRmonBroadcastCntEntry": pmc2002MondwRmonBroadcastCntEntry,
       "pmc2002MondwRmonBroadcastCntIndex": pmc2002MondwRmonBroadcastCntIndex,
       "pmc2002MondwRmonBroadcastCntValuePortn": pmc2002MondwRmonBroadcastCntValuePortn,
       "pmc2002MondwRmonBroadcastCntErrorPortn": pmc2002MondwRmonBroadcastCntErrorPortn,
       "pmc2002MondwRmonBroadcastCntOverloadPortn": pmc2002MondwRmonBroadcastCntOverloadPortn,
       "pmc2002MondwRmonMulticastCntTable": pmc2002MondwRmonMulticastCntTable,
       "pmc2002MondwRmonMulticastCntEntry": pmc2002MondwRmonMulticastCntEntry,
       "pmc2002MondwRmonMulticastCntIndex": pmc2002MondwRmonMulticastCntIndex,
       "pmc2002MondwRmonMulticastCntValuePortn": pmc2002MondwRmonMulticastCntValuePortn,
       "pmc2002MondwRmonMulticastCntErrorPortn": pmc2002MondwRmonMulticastCntErrorPortn,
       "pmc2002MondwRmonMulticastCntOverloadPortn": pmc2002MondwRmonMulticastCntOverloadPortn,
       "pmc2002MondwRmonPauseFrameCntTable": pmc2002MondwRmonPauseFrameCntTable,
       "pmc2002MondwRmonPauseFrameCntEntry": pmc2002MondwRmonPauseFrameCntEntry,
       "pmc2002MondwRmonPauseFrameCntIndex": pmc2002MondwRmonPauseFrameCntIndex,
       "pmc2002MondwRmonPauseFrameCntValuePortn": pmc2002MondwRmonPauseFrameCntValuePortn,
       "pmc2002MondwRmonPauseFrameCntErrorPortn": pmc2002MondwRmonPauseFrameCntErrorPortn,
       "pmc2002MondwRmonPauseFrameCntOverloadPortn": pmc2002MondwRmonPauseFrameCntOverloadPortn,
       "pmc2002MondwRmonTimerCntTable": pmc2002MondwRmonTimerCntTable,
       "pmc2002MondwRmonTimerCntEntry": pmc2002MondwRmonTimerCntEntry,
       "pmc2002MondwRmonTimerCntIndex": pmc2002MondwRmonTimerCntIndex,
       "pmc2002MondwRmonTimerCntValuePortn": pmc2002MondwRmonTimerCntValuePortn,
       "pmc2002MondwRmonTimerCntErrorPortn": pmc2002MondwRmonTimerCntErrorPortn,
       "pmc2002MondwRmonTimerCntOverloadPortn": pmc2002MondwRmonTimerCntOverloadPortn,
       "pmc2002MondwRmonBitsCntTable": pmc2002MondwRmonBitsCntTable,
       "pmc2002MondwRmonBitsCntEntry": pmc2002MondwRmonBitsCntEntry,
       "pmc2002MondwRmonBitsCntIndex": pmc2002MondwRmonBitsCntIndex,
       "pmc2002MondwRmonBitsCntValuePortn": pmc2002MondwRmonBitsCntValuePortn,
       "pmc2002MondwRmonBitsCntErrorPortn": pmc2002MondwRmonBitsCntErrorPortn,
       "pmc2002MondwRmonBitsCntOverloadPortn": pmc2002MondwRmonBitsCntOverloadPortn,
       "pmc2002MondwRmonUnicastCntTable": pmc2002MondwRmonUnicastCntTable,
       "pmc2002MondwRmonUnicastCntEntry": pmc2002MondwRmonUnicastCntEntry,
       "pmc2002MondwRmonUnicastCntIndex": pmc2002MondwRmonUnicastCntIndex,
       "pmc2002MondwRmonUnicastCntValuePortn": pmc2002MondwRmonUnicastCntValuePortn,
       "pmc2002MondwRmonUnicastCntErrorPortn": pmc2002MondwRmonUnicastCntErrorPortn,
       "pmc2002MondwRmonUnicastCntOverloadPortn": pmc2002MondwRmonUnicastCntOverloadPortn,
       "pmc2002MondwRmonNonUnicastCntTable": pmc2002MondwRmonNonUnicastCntTable,
       "pmc2002MondwRmonNonUnicastCntEntry": pmc2002MondwRmonNonUnicastCntEntry,
       "pmc2002MondwRmonNonUnicastCntIndex": pmc2002MondwRmonNonUnicastCntIndex,
       "pmc2002MondwRmonNonUnicastCntValuePortn": pmc2002MondwRmonNonUnicastCntValuePortn,
       "pmc2002MondwRmonNonUnicastCntErrorPortn": pmc2002MondwRmonNonUnicastCntErrorPortn,
       "pmc2002MondwRmonNonUnicastCntOverloadPortn": pmc2002MondwRmonNonUnicastCntOverloadPortn,
       "pmc2002RmonLine": pmc2002RmonLine,
       "pmc2002RmonOther": pmc2002RmonOther,
       "pmc2002MonCountersReset": pmc2002MonCountersReset,
       "pmc2002MonCountersStop": pmc2002MonCountersStop}
)
